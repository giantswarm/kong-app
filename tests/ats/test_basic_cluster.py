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
from pytest_helm_charts.clusters import Cluster
from pytest_helm_charts.k8s.deployment import wait_for_deployments_to_run

logger = logging.getLogger(__name__)

deployment_name = "kong-app-kong-app"
namespace_name = "kong"

timeout: int = 560


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


# scope "module" means this is run only once, for the first test case requesting! It might be tricky
# if you want to assert this multiple times
@pytest.fixture(scope="module")
def ic_deployment(request, kube_cluster: Cluster) -> List[pykube.Deployment]:
    logger.info("Waiting for postgres pods")
    kube_cluster.kubectl(
        "rollout status --watch statefulset/kong-app-postgresql",
        timeout="120s",
        output_format="",
        namespace=namespace_name,
    )
    logger.info("Postgres pods look ready")

    logger.info("Waiting for kong deployment..")

    deployment_ready = wait_for_ic_deployment(kube_cluster)

    logger.info("kong deployment looks satisfied..")

    return deployment_ready


def wait_for_ic_deployment(kube_cluster: Cluster) -> List[pykube.Deployment]:
    deployments = wait_for_deployments_to_run(
        kube_cluster.kube_client,
        [deployment_name],
        namespace_name,
        timeout,
    )
    return deployments

@pytest.fixture(scope="module")
def pods(kube_cluster: Cluster) -> List[pykube.Pod]:
    pods = pykube.Pod.objects(kube_cluster.kube_client)

    pods = pods.filter(namespace=namespace_name, selector={'app.kubernetes.io/name': 'kong-app', 'app.kubernetes.io/component': 'app'})

    return pods

# when we start the tests on circleci, we have to wait for pods to be available, hence
# this additional delay and retries
@pytest.mark.smoke
@pytest.mark.upgrade
@pytest.mark.flaky(reruns=5, reruns_delay=10)
def test_pods_available(kube_cluster: Cluster, ic_deployment: List[pykube.Deployment]):
    for s in ic_deployment:
        assert int(s.obj["status"]["readyReplicas"]) == int(s.obj["spec"]["replicas"])

# when we start the tests on circleci, we have to wait for pods to be available, hence
# this additional delay and retries
@pytest.mark.smoke
@pytest.mark.upgrade
def test_pods_spread(kube_cluster: Cluster, ic_deployment: List[pykube.Deployment], pods: List[pykube.Pod]):
    assert len(ic_deployment) == 1
    assert len(pods) == 2

    node_names = set()

    for pod in pods:
        node_names.add(pod.obj["spec"]["nodeName"])

    # make node_names unique, check if its length is the same as the number of pods
    assert len(node_names) == len(pods)
