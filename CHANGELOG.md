# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project's packages adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Added values.schema.json for validation of default values

## [1.1.0] - 2020-12-02

### Updated

- Update architect-orb to 0.18.1
- Sync with upstream chart [1.12.0](https://github.com/Kong/charts/tree/kong-1.12.0). Please check the upstream [changelog](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#1120).

## [1.0.0] - 2020-10-13

### Breaking changes

* Kong Ingress Controller 1.0 removes support for several deprecated flags and
  the KongCredential custom resource. Please see the [controller changelog](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#breaking-changes)
  for details. Note that Helm 3 will not remove the KongCredential CRD by
  default: you should delete it manually after converting KongCredentials to
  [credential Secrets](https://github.com/Kong/kubernetes-ingress-controller/blob/next/docs/guides/using-consumer-credential-resource.md#provision-a-consumer).
  If you manage CRDs using Helm (check to see if your KongCredential CRD has a
  `app.kubernetes.io/managed-by: Helm` label), perform the credential Secret
  conversion **before** upgrading to chart 1.11.0 to avoid losing credential
  configuration.
* The chart no longer uses the `extensions` API for PodSecurityPolicy, and now
  uses the modern `policy` API. This breaks compatibility with Kubernetes
  versions 1.11 and older.
  ([#195](https://github.com/Kong/charts/pull/195))

### Updated

- Update architect-orb to 0.11.0
- Sync with upstream chart [1.11.0](https://github.com/Kong/charts/tree/kong-1.11.0)
- Please check the upstream [CHANGELOG.md](/helm/kong-app/CHANGELOG.md)

### Changed

- Change upstream default branch in upstream-sync script

## [0.9.1] - 2020-09-07

### Changed

- Split registry value to allow switching registry.

## [0.9.0] - 2020-08-25

### Updated
 
- Upgraded architect-orb to 0.10.0
- Add github workflows for release automation
- Sync with upstream chart [v1.8.0](https://github.com/Kong/charts/tree/kong-1.8.0)
- Update busybox 1.31.0 -> 1.32.0

### Improvements
From upstream CHANGELOG:
>* Update default Kong version to 2.1.
>* Update Kong Enterprise images to 1.5.0.4 (kong-enterprise-edition) and
>  2.0.4.2 (kong-enterprise-k8s).
>* Updated default controller version to 0.9.1.
>  ([#150](https://github.com/Kong/charts/pull/150))
>* Added support for ServiceMonitor targetLabels (for use with the Prometheus
>  Operator).
>  ([#162](https://github.com/Kong/charts/pull/162))
>* Automatically handle the [new port_maps
>  setting](https://github.com/Kong/kong/pull/5861) for the proxy service.
>  ([#169](https://github.com/Kong/charts/pull/169))
>* Add support for [hybrid mode
>  deployments](https://docs.konghq.com/latest/hybrid-mode/).
>  ([#160](https://github.com/Kong/charts/pull/160))

### Fixed

- Uses fix from upstream-branch next to resolve issue "CONTROLLER_ADMISSION_WEBHOOK_LISTEN" which overwrites our fix below.
    - Force cast to string for Admission Webhook port [#59](https://github.com/giantswarm/kong-app/pull/59)

## [v0.8.3] - 2020-06-17

### Fixed

- Fix template helpers issue converting port number for the webhook endpoint.

## [v0.8.2] - 2020-06-02

### Added

- Added dates to CHANELOG entries.

### Info
- Existing v0.8.2 git tag got updated by mistake in attempt to make next release. This changelog entry was added to avoid any confusion, even though change made in the release is not so much customer relevant.

## [v0.8.1] - 2020-06-02

- Sync with upstream - [v1.6.1](https://github.com/Kong/charts/blob/master/charts/kong/CHANGELOG.md#161)
- Bump version of Kong Ingress Controller - [0.9.0](https://github.com/Kong/kubernetes-ingress-controller/blob/master/CHANGELOG.md#090---20200526)
- `ingressController.installCRDs` default set to `false`

## [v0.8.0] - 2020-05-26

- Sync with upstream - [v1.5.0](https://github.com/Kong/charts/blob/master/charts/kong/CHANGELOG.md#150)
- Bump Kong version - [v2.0.4](https://github.com/Kong/kong/blob/master/CHANGELOG.md#204)
- Bump Kong Ingress Controller version - [v0.8.1](https://github.com/Kong/kubernetes-ingress-controller/blob/master/CHANGELOG.md#081---20200415)

## [v0.7.2] - 2020-03-31

### Updated

- Enable Giant Swarm monitoring
- Set default `ingressClass` to `kong-app`. See #48

## [v0.7.1]

### Updated

- Fix chart `apiVersion`

## [v0.7.0]

### Updated

- Sync with upstream [v1.3.0](https://github.com/Kong/charts/blob/master/charts/kong/CHANGELOG.md#130)
- Kong version bumped to 2.0.1
- Kong Ingress controller bumped to 0.7.1

## [v0.6.2]

### Add

- Refactor how plugins are mounted, now support multiple subdirectories.

## [v0.6.1]

### Fix

- Issue #41 : Helm upgrade causes service account to be recreated (recreating service token)

## [v0.6.0]

### Updated

- Pull upstream v1.1.1

### Fixed

- Issue #38 : Migration init job hangs when using your own DB
- PR #40 : Fix Helm upgrade failing

## [v0.5.3]

### Updated

- Pull in changes from upstream v1.0.1

## [v0.5.2]

### Updated

- Bump Kong version, 1.4.3 contains [security - fix](https://github.com/Kong/kong/blob/master/CHANGELOG.md#143)

## [v0.5.1]

### Changed

- Remove `registry` from values

## [v0.5.0]

### Changed

- Update the chart to latest [upstream version 1.0.0](https://github.com/Kong/charts) (#043c2c2)

### Updated

- README contains some more information

## [v0.4.6]

### Added

- Bump versions (#31), Fix giantswarm/kong-app/issues/29

## [v0.4.5]

### Added

- Add support for plugins which require multiple configmaps.

## [v0.4.4]

### Removed

- Remove the stale custom plugin configmap.

## [v0.4.3]

### Added

- Add Postgres user and database name as environment variables in the proper templates.

## [v0.4.2]

### Changed

- Change wait container image for kong to init properly DB deployment

## [v0.4.1]

### Changed

- Add registry in all wait images entries to make it deployable in all regions
- Use a fixed busybox version for wait images to make it deterministic

## [v0.4.0]

### Added

- Add support for validation controller as optional.
- Add option to configure a horizontal pod autoscaler.

## [v0.3.0]

### Updated

- Add new version of Kong and Kong ingress controller.
- Add option to deploy redis for rate limiting plugin.
- Add support to configure custom plugins.

## [v0.2.0]

### Updated

- Use retagged images.
- Use ClusterIP for all services except proxy which uses LoadBalancer.
- Add support for an external PostgreSQL database.

## [v0.1.0]

### Added

- Add first version of the kong-app chart based on the community Kong chart.

### Updated

- Enable Kong Ingress Controller mode.
- Use service of type Load Balancer for the Kong proxy service.
- Disable using Postgres and use Kubernetes resources for storing state.

[Unreleased]: https://github.com/giantswarm/kong-app/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/giantswarm/kong-app/compare/v0.9.1...v1.0.0
[0.9.1]: https://github.com/giantswarm/kong-app/compare/v0.9.0...v0.9.1
[0.9.0]: https://github.com/giantswarm/kong-app/compare/v0.8.3...v0.9.0
[v0.8.3]: https://github.com/giantswarm/kong-app/compare/v0.8.2..v0.8.3
[v0.8.2]: https://github.com/giantswarm/kong-app/compare/v0.8.1..v0.8.2
[v0.8.1]: https://github.com/giantswarm/kong-app/compare/v0.8.0..v0.8.1
[v0.8.0]: https://github.com/giantswarm/kong-app/compare/v0.7.2..v0.8.0
[v0.7.2]: https://github.com/giantswarm/kong-app/compare/v0.7.1..v0.7.2
[v0.7.1]: https://github.com/giantswarm/kong-app/compare/v0.7.0..v0.7.1
[v0.7.0]: https://github.com/giantswarm/kong-app/compare/v0.6.2..v0.7.0
[v0.6.2]: https://github.com/giantswarm/kong-app/compare/v0.6.1..v0.6.2
[v0.6.1]: https://github.com/giantswarm/kong-app/compare/v0.6.0..v0.6.1
[v0.6.0]: https://github.com/giantswarm/kong-app/compare/v0.5.3..v0.6.0
[v0.5.3]: https://github.com/giantswarm/kong-app/compare/v0.5.2..v0.5.3
[v0.5.2]: https://github.com/giantswarm/kong-app/compare/v0.5.1..v0.5.2
[v0.5.1]: https://github.com/giantswarm/kong-app/compare/v0.5.0..v0.5.1
[v0.5.0]: https://github.com/giantswarm/kong-app/compare/v0.4.6..v0.5.0
[v0.4.6]: https://github.com/giantswarm/kong-app/compare/v0.4.5..v0.4.6
[v0.4.5]: https://github.com/giantswarm/kong-app/compare/v0.4.4..v0.4.5
[v0.4.4]: https://github.com/giantswarm/kong-app/compare/v0.4.3..v0.4.4
[v0.4.3]: https://github.com/giantswarm/kong-app/compare/v0.4.2..v0.4.3
[v0.4.2]: https://github.com/giantswarm/kong-app/compare/v0.4.1..v0.4.2
[v0.4.1]: https://github.com/giantswarm/kong-app/compare/v0.4.0..v0.4.1
[v0.4.0]: https://github.com/giantswarm/kong-app/compare/v0.3.0..v0.4.0
[v0.3.0]: https://github.com/giantswarm/kong-app/compare/v0.2.0..v0.3.0
[v0.2.0]: https://github.com/giantswarm/kong-app/compare/v0.1.0..v0.2.0
[v0.1.0]: https://github.com/giantswarm/kong-app/releases/tag/v0.1.0
