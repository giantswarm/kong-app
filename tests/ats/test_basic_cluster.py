import logging
import requests
import time
from contextlib import contextmanager
from functools import partial
from json import dumps
from pathlib import Path
from typing import Dict, List, Optional

import pykube
import pytest
from pytest_helm_charts.fixtures import Cluster
from pytest_helm_charts.utils import wait_for_deployments_to_run

logger = logging.getLogger(__name__)

deployment_name = "kong-app-kong-app"
namespace_name = "kong"

timeout: int = 360


@pytest.mark.smoke
def test_api_working(kube_cluster: Cluster) -> None:
    """Very minimalistic example of using the [kube_cluster](pytest_helm_charts.fixtures.kube_cluster)
    fixture to get an instance of [Cluster](pytest_helm_charts.clusters.Cluster) under test
    and access its [kube_client](pytest_helm_charts.clusters.Cluster.kube_client) property
    to get access to Kubernetes API of cluster under test.
    Please refer to [pykube](https://pykube.readthedocs.io/en/latest/api/pykube.html) to get docs
    for [HTTPClient](https://pykube.readthedocs.io/en/latest/api/pykube.html#pykube.http.HTTPClient).
    """
    assert kube_cluster.kube_client is not None
    assert len(pykube.Node.objects(kube_cluster.kube_client)) >= 1


@pytest.mark.smoke
def test_cluster_info(
    kube_cluster: Cluster,
    cluster_type: str,
    chart_extra_info: Dict[str, str],
    chart_version: str,
) -> None:
    """Example shows how you can access additional information about the cluster the tests are running on"""
    logger.info(f"Running on cluster type {cluster_type}")
    for key, value in chart_extra_info.items():
        logger.info(f"chart_extra_info '{key}': '{value}'")

    logger.info(f"chart_version '{chart_version}'")
    assert kube_cluster.kube_client is not None
    assert cluster_type != ""


# scope "module" means this is run only once, for the first test case requesting! It might be tricky
# if you want to assert this multiple times
@pytest.fixture(scope="module")
def ic_deployment(request, kube_cluster: Cluster) -> List[pykube.Deployment]:
    logger.info("Deploying postgres for kong db mode")
    kube_cluster.kubectl(
        "apply",
        filename=Path(request.fspath.dirname) / "postgres.yaml",
        output_format="",
    )

    kube_cluster.kubectl(
        "rollout status --watch statefulset/postgres",
        timeout="60s",
        output_format="",
        namespace="postgres",
    )
    logger.info("Postgres pods look ready")

    logger.info("Waiting for kong deployment..")

    return wait_for_ic_deployment(kube_cluster)


def wait_for_ic_deployment(kube_cluster: Cluster) -> List[pykube.Deployment]:
    deployments = wait_for_deployments_to_run(
        kube_cluster.kube_client,
        [deployment_name],
        namespace_name,
        timeout,
    )
    return deployments


# when we start the tests on circleci, we have to wait for pods to be available, hence
# this additional delay and retries
@pytest.mark.smoke
@pytest.mark.upgrade
@pytest.mark.flaky(reruns=5, reruns_delay=10)
def test_pods_available(kube_cluster: Cluster, ic_deployment: List[pykube.Deployment]):
    for s in ic_deployment:
        assert int(s.obj["status"]["readyReplicas"]) > 0


def try_ingress():
    # try the ingress
    retries = 10
    last_status = 0
    while last_status != 200:
        r = requests.get(
            "http://127.0.0.1:8080/",
            headers={
                "Host": "helloworld",
                "Authorization": "Basic YmFzaWMtYXV0aC11c2VyOmJhc2ljLWF1dGgtcGFzc3dvcmQ=",
            },
        )
        last_status = r.status_code

        if last_status == 200 or retries == 0:
            break

        retries = retries - 1
        time.sleep(5)

    return last_status == 200


@pytest.mark.functional
@pytest.mark.upgrade
def test_ingress_creation(
    request,
    kube_cluster: Cluster,
    ic_deployment: List[pykube.Deployment],
    chart_version: str,
):
    # Wait again for kong deployment
    kube_cluster.kubectl(
        f"wait deployment {deployment_name} --for=condition=Available",
        timeout="60s",
        output_format="",
        namespace=namespace_name,
    )

    kube_cluster.kubectl(
        "apply",
        filename=Path(request.fspath.dirname) / "global-plugins.yaml",
        output_format="",
    )
    kube_cluster.kubectl(
        "apply",
        filename=Path(request.fspath.dirname) / "test-ingress.yaml",
        output_format="",
    )

    # time.sleep(9223372036)

    kube_cluster.kubectl(
        "wait deployment helloworld --for=condition=Available",
        timeout="60s",
        output_format="",
        namespace="helloworld",
    )

    # is it even available?
    assert try_ingress()

    # test some plugins
    # we're not testing every plugin
    r = requests.get(
        "http://127.0.0.1:8080/",
        headers={
            "Host": "helloworld",
            "Authorization": "Basic YmFzaWMtYXV0aC11c2VyOmJhc2ljLWF1dGgtcGFzc3dvcmQ=",
        },
    )
    r.raise_for_status()
    logger.info("basic-auth plugin works")

    # global-response-transformer
    assert r.headers["global-reponse-headers"] == "enabled"
    logger.info("response-transformer plugin works")

    # cache plugin
    assert "x-cache-status" in r.headers
    logger.info("cache plugin works")

    # keyauth + cors
    r = requests.get(
        "http://127.0.0.1:8080/",
        headers={
            "Host": "helloworld-keyauth",
            "test-api-key": "123-secret-api-key",
            "Access-Control-Request-Method": "GET",
        },
    )
    r.raise_for_status()
    logger.info("Key-auth plugin works")

    # cors plugin
    assert r.headers["access-control-allow-origin"] == "*"
    logger.info("Cors plugin works")

    # clean up
    kube_cluster.kubectl(
        "delete",
        filename=Path(request.fspath.dirname) / "test-ingress.yaml",
        output_format="",
    )
    kube_cluster.kubectl(
        "delete",
        filename=Path(request.fspath.dirname) / "global-plugins.yaml",
        output_format="",
    )
