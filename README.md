[![CircleCI](https://circleci.com/gh/giantswarm/kong-app.svg?style=shield)](https://circleci.com/gh/giantswarm/kong-app)

# kong-app chart

[Kong for Kubernetes](https://github.com/Kong/kubernetes-ingress-controller) is
an open-source Ingress Controller for Kubernetes that offers API management capabilities
with a plugin architecture.

Giant Swarm offers a Kong Managed App which can be installed in tenant clusters.

## Available Versions

| Giant Swarm Chart Release | Upstream Chart Release | Kong Version | Kong IC Version | Kong-Gateway Enterprise container tag |
| --- | --- | --- | --- | --- |
| [v2.7.2](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#272---2022-03-10) | [2.7.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#270) | [2.7.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#271) | [2.2.1](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#221) | 2.7.1.1-alpine |
| [v2.7.1](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#271---2022-02-16) | [2.7.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#270) | [2.7.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#271) | [2.2.1](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#221) | 2.7.1.1-alpine |
| [v2.7.0](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#270---2022-02-16) | [2.7.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#270) | [2.7.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#271) | [2.2.1](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#221) | 2.7.1.1-alpine |
| [v2.6.0](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#260---2022-02-11) | [26eff4f](https://github.com/Kong/charts/compare/kong-2.6.4...26eff4f) | [2.7.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#271) | [2.1.1](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#211) | 2.7.1.1-alpine |
| [v2.5.0](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#250---2022-01-18) | [2.6.4](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#264) | [2.7.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#271) | [2.1.1](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#211) | 2.7.1.1-alpine |
| [v2.4.0](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#240---2022-01-12) | [2.6.4](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#264) | [2.7.0](https://github.com/Kong/kong/blob/master/CHANGELOG.md#270) | [2.1.0](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#210) | 2.7.1.1-alpine |
| [v2.3.5](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#235---2021-12-14) | [2.3.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#230) | [2.5.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#251) | [1.3.4](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#134) | 2.5.1.2-alpine |
| [v2.3.4](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#234---2021-12-02) | [2.3.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#230) | [2.5.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#251) | [1.3.4](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#134) | 2.5.1.2-alpine |
| [v2.3.3](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#233---2021-11-24) | [2.3.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#230) | [2.5.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#251) | [1.3.4](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#134) | 2.5.1.2-alpine |
| [v2.3.2](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#232---2021-10-05) | [2.3.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#230) | [2.5.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#251) | [1.3.4](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#134) | 2.5.1.2-alpine |
| [v2.3.1](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#231---2021-09-14) | [2.3.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#230) | [2.5.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#251) | [1.3.4](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#134) | 2.5.1.2-alpine |
| [v2.3.0](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#230---2021-08-25) | [2.3.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#230) | [2.5.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#251) | [1.3.4](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#134) | 2.5.1.2-alpine |
| [v2.1.0](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md#210---2021-06-15) | [2.1.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#210) | [2.4.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#241) | [1.2.0](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#120) | 2.3.3.2-alpine |

For older versions, please refer to the [changelog](https://github.com/giantswarm/kong-app/blob/master/CHANGELOG.md)

## Configuration
There are 3 ways that Kong can be configured in Kubernetes:

1. Using a Database (PostgreSQL or Cassandra)
1. Kong Kubernetes Ingress Controller (with CRDs)
1. DBless (no databases and static Configuration file)

The recommended and supported way is to use Ingress Controller (which works
alongside DBless).

This app does not by default provide a database and if a database is required,
then you will need to BYOD (Bring Your Own Database). For testing purposes, it
is possible launch postgres alongside this App (described below).

For detailed configuration options, please refer to the [configuration list](helm/kong-app/README.md#configuration)
also the [`values.yaml` file](helm/kong-app/values.yaml)

Any key value put under the `env` section translates to environment variables
used to control Kong's configuration. Every key is prefixed with KONG_ and
upper-cased before setting the environment variable.

### Kong Ingress Controller (Recommended)
The default installation of the App will use Kong Ingress Controller. This
method uses CRDs to configure various aspects of Kong. Please refer to Kong
Ingress Controller
[documentation](https://github.com/Kong/kubernetes-ingress-controller/tree/master/docs)
for more detailed explanation and usage.

### DBLess Kong
The [official documentation](https://docs.konghq.com/1.4.x/db-less-and-declarative-config/)
explains how DBLess Kong works and the possible limitations. To use this method
of operation with this App, you will need to include the following you your
values YAML:

Using an existing ConfigMap
---------------------------
```YAML
env:
  database: "off"
ingressController:
  enabled: false
dblessConfig:
  configMap: nameOfExistingConfigMap
```

Inline configuration
--------------------
```YAML
env:
  database: "off"
ingressController:
  enabled: false
dblessConfig:
  config:
    _format_version: "1.1"
    services:
      - name: example.com
        url: http://example.com
        routes:
        - name: example
          paths:
          - "/example"
```

### Using your own Database
Kong supports two databases:

- PostgreSQL: 9.5 and above.
- Cassandra: 2.2 and above.

This section will focus on PostgreSQL, however the same process can be equally
applied to Cassandra.

Example database configuration:
```YAML
ingressController:
  enabled: false
env:
  database: "postgress" # can be "off" or "cassandra"
  pg_host: 127.0.0.1
  pg_port: 12345
  pg_user: postgres
  pg_password: # This can also be a string value, but not recommended
    valueFrom:
           secretKeyRef:
              key: kong
              name: postgres
```
You can use any valid database configuration option inside `env`. This is also
how Cassandra can be configured.

_note_: If `pg_port` is not set then it will default to `5432`

#### Installing a database alongside the App
For testing purposes, it is possible to install a PostgreSQL server alongside
the App. To do this:

```YAML
postgresql:
  enabled: true
  postgresqlUsername: kong
  postgresqlDatabase: kong
  service:
    port: 5432
```
(There is no need to add PostgreSQL configuration data to `env`)

Please note: This configuration should only really be used for testing and it
not something we can support

### Using Kong Ingress Controller with a Database
When using Kong Ingress Controller, their shouldn't be a need to use a Database.
However in some cases (for example, plugin support) a data store is
required. In these situations, it is possible to use a mixture of Kong Ingress
Controller and a database.

Like in the case of using a database, Giant Swarm do not support the database and
can only provide best efforts support with this configuration.

To configure, please see ['Using your own Database'](#using-your-own-database).
But ensure that that `ingressController.enabled` is set to `true`.

Note:
> Is it possible to create consumers using the Admin API?
>
> From version 0.5.0 onwards, Kong Ingress Controller tags each entity that it
> manages inside Kong's database and only manages the entities that it creates.
> This means that if consumers and credentials are created dynamically,
> they won't be deleted by the Ingress Controller.
(Taken from https://github.com/Kong/kubernetes-ingress-controller/blob/master/docs/faq.md#is-it-possible-to-create-consumers-using-the-admin-api)

### Kong Ingress Controller CRDs
If you wish to use the Kong Ingress Controller and use Helm 2, please be aware
that by default the CRDs will not be installed. If you wish to add them at
install time, please set the following:

  - In values file
    ```
    ingressController:
      installCRDs: true
    ```
  - On command line
    ```
    --set ingressController.installCRDs=true
    ```

This is not required for Helm 3, as CRDs will be installed automatically.

## Known Issues

## Credit

* https://github.com/Kong/charts/

## Automatic and manual testing

The helm chart in this repository undergoes [a series of automated tests](tests/ats/test_basic_cluster.py) running on a [kind](https://kind.sigs.k8s.io/) cluster ([kind cluster config](tests/kind_config.yaml)) executed by [app-test-suite](https://github.com/giantswarm/app-test-suite). ([chart values used for tests](tests/test-values.yaml))

Testing includes creation of `Deployment`, `Service`, and `Ingress` resources to check if reconciliation works as intended.

To execute tests on your machine, obtain a copy of the [dats.sh](https://github.com/giantswarm/app-test-suite/releases/download/v0.2.2/dats.sh) helper script and a chart archive (`helm pull https://giantswarm.github.io/giantswarm-catalog/kong-app-2.5.0.tgz` or build an archive with your changes using [`app-build-suite`](http://github.com/giantswarm/app-build-suite)), then execute

```
./dats.sh -c kong-app-2.5.0.tgz
```

## Security Policy

### Reporting a Vulnerability

Please visit https://www.giantswarm.io/responsible-disclosure for information on
reporting security issues.
