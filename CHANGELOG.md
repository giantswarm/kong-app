# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project's packages adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [4.0.0] - 2024-04-22

### BREAKING CHANGES

This is a major release because it changes the default behaviour of the Chart.
- For Kong Enterprise deployment the flag `.Values.image.repository` and `.Values.image.tag` can now be omitted.
- For Kong OSS deployment the flag `.Values.image.repository` and `.Values.image.tag` now have to be set to the respective OSS values.

For further instructions please refer to the [README.md](./README.md).

### Changes

- Align with upstream chart commit [07ddc3d](https://github.com/Kong/charts/commit/07ddc3d3ac28f6313d705e5339520d2cdf22e725) (ahead of release [2.38.0](https://github.com/Kong/charts/releases/tag/kong-2.38.0)) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.35.1...07ddc3d))
- Updated handling of `session_conf_secret` to accommodate Kong 3.6 - [Ref](https://docs.konghq.com/gateway/3.6.x/kong-manager/auth/oidc/migrate/)
- Configure Chart for Kong Gateway Enterprise deployment by default. Please check the README.md to see how to run kong OSS.
- Update README.md to reflect default deployment Changes.

## [3.8.0] - 2024-03-27

### Added

- Add Vertical Pod Autoscaler resource. It is disabled by default.

### Changes

- Disable anonymous reports in kong default values for proxy and ingress controller.
- Align with upstream chart version [2.35.1](https://github.com/Kong/charts/releases/tag/kong-2.35.1) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.33.3...kong-2.35.1))
  - Kong listens now use both IPv4 and IPv6 addresses. [kong/charts#986](https://github.com/Kong/charts/pull/986)

## [3.7.0] - 2024-01-16

### Changes

- Update kong ingress controller to [3.0.2](https://github.com/Kong/kubernetes-ingress-controller/blob/v3.0.2/CHANGELOG.md#302)
- Align with upstream chart version [2.33.3](https://github.com/Kong/charts/releases/tag/kong-2.33.3) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.33.1...kong-2.33.3))
- Execute enterprise tests with kong-gateway container image version [3.5.0.2-debian](https://docs.konghq.com/gateway/changelog/#3502)

### Fixed

- Remove the default nodeAffinity as it had old restricted labels conflicting with `karpenter` restrictions. The functionality should be covered wtih control plane taints.

## [3.6.2] - 2023-12-13

### Changes

- Configure `gsoci.azurecr.io` as the default container image registry.
- Update kubectl-apply-job to 0.7.0 for `gsoci.azurecr.io` container image registry.

## [3.6.1] - 2023-12-11

### Changes

- Align with upstream chart version [2.33.1](https://github.com/Kong/charts/releases/tag/kong-2.33.1) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.33.0...kong-2.33.1))

## [3.6.0] - 2023-12-07

### Changes

- Align with upstream chart version [2.33.0](https://github.com/Kong/charts/releases/tag/kong-2.33.0) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.29.0...kong-2.33.0))
- Update kong to [3.5.0](https://github.com/Kong/kong/blob/3.5.0/changelog/3.5.0/3.5.0.md)
- Update kong ingress controller to [3.0.1](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#301)
- Execute enterprise tests with kong-gateway container image version [3.5.0.1-debian](https://docs.konghq.com/gateway/changelog/#3501)

## [3.5.0] - 2023-10-16

This version contains fixes for HTTP/2 stream reset attacks ([CVE-2023-44487](https://nvd.nist.gov/vuln/detail/CVE-2023-44487)).

### Changes

- Align with upstream chart version [2.29.0](https://github.com/Kong/charts/releases/tag/kong-2.29.0) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.23.0...kong-2.29.0))
- Update kong to [3.4.2](https://github.com/Kong/kong/blob/3.4.2/CHANGELOG.md#342)
- Update kong ingress controller to [2.12.0](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#2120)
- Execute enterprise tests with kong-gateway container image version [3.4.1.1-debian](https://docs.konghq.com/gateway/changelog/#3411)
- Add `Values.global.podSecurityStandards.enforced` flag in preparation of PSP to PSS migration
- Prevent installation of PodDisruptionBudget with `replicaCount: 1` or `autoscaling.minReplicas: 1`

## [3.4.0] - 2023-08-22

### Changes

- Align with upstream chart version [2.23.0](https://github.com/Kong/charts/releases/tag/kong-2.23.0) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.21.0...kong-2.23.0))
- Update kong to [3.3.1](https://github.com/Kong/kong/blob/3.3.1/CHANGELOG.md#331)
- Update kong ingress controller to [2.10.4](https://github.com/Kong/kubernetes-ingress-controller/blob/v2.10.4/CHANGELOG.md#2103)
- Execute enterprise tests with kong-gateway container image version [3.3.1.0-debian](https://docs.konghq.com/gateway/changelog/#3310)

## [3.3.0] - 2023-05-17

### Changes

- Do not enable custom Giant Swarm monitoring Service if ServiceMonitor is enabled.
- Align with upstream chart version [2.21.0](https://github.com/Kong/charts/releases/tag/kong-2.21.0) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.20.1...kong-2.21.0))
- Ignore linkerd namespace in ValidatingWebhookConfiguration.

## [3.2.0] - 2023-05-04

### Changes

- Align with upstream chart version [2.20.1](https://github.com/Kong/charts/releases/tag/kong-2.20.1) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.19.1...kong-2.20.1))
- Update kubectl-apply-job to 0.4.0

## [3.1.1] - 2023-04-24

### Changes

- Align with upstream chart version [2.19.1](https://github.com/Kong/charts/releases/tag/kong-2.19.1) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.19.0...kong-2.19.1))
- Fix `webhook-cert` being mounted regardless if `.Values.ingressController.enabled` is set.  [kong/charts#779](https://github.com/Kong/charts/pull/779)

## [3.1.0] - 2023-04-20

If you are upgrading from chart version lower than 3.0.0, it is neccessary to perform an intermediate upgrade to chart version 3.0.0 as this version contains a required migration process for enabling the use of seccompProfiles.

### Changes

- Align with upstream chart version [2.19.0](https://github.com/Kong/charts/releases/tag/kong-2.19.0) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.16.4...kong-2.19.0))
- Update kong to [3.2.2](https://github.com/Kong/kong/blob/3.2.2/CHANGELOG.md#322)
- Update kong ingress controller to [2.9.3](https://github.com/Kong/kubernetes-ingress-controller/blob/v2.9.3/CHANGELOG.md#293)
- Execute enterprise tests with kong-gateway container image version [3.2.2.1-debian](https://docs.konghq.com/gateway/changelog/#3221)
- Update kubectl-apply-job to 0.3.1 for compatibility with Giant Swarm release v19

## [3.0.1] - 2023-02-14

If you are upgrading from chart version lower than 3.0.0, it is neccessary to perform an intermediate upgrade to chart version 3.0.0 as this version contains a required migration process for enabling the use of seccompProfiles.

### Changes

- Align with upstream chart version [2.16.4](https://github.com/Kong/charts/releases/tag/kong-2.16.4) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.16.2...kong-2.16.4))
  - Fix template issue preventing custom dblessconfig volume from being mounted.
    [#741](https://github.com/Kong/charts/pull/741)
  - HorizontalPodAutoscaler's API version is detected properly.
    [#744](https://github.com/Kong/charts/pull/744)
- Change default `PodDisruptionBudget` to move from `maxUnavailable: 1` to `maxUnavailable: 25%` for better scaling

## [3.0.0] - 2023-02-09

This release upgrades kong to release [3.1.1](https://github.com/Kong/kong/blob/3.1.1/CHANGELOG.md#311) which contains breaking changes. Please consider reading the upstream [Breaking changes](https://github.com/Kong/kong/blob/3.1.1/CHANGELOG.md#breaking-changes) documentation before upgrading. Users of the kong enterprise should read the [Kong Gateway changelogs of releases 3.0.0.0 onwards](https://docs.konghq.com/gateway/changelog/#3000) up to 3.1.1.3.

### Updates

- Align with upstream chart version [2.16.2](https://github.com/Kong/charts/releases/tag/kong-2.16.2) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.13.0...kong-2.16.2))
- Update kong/kong to [3.1.1](https://github.com/Kong/kong/blob/3.1.1/CHANGELOG.md#311). Please read [Breaking changes](https://github.com/Kong/kong/blob/3.1.1/CHANGELOG.md#breaking-changes) notes
- Execute enterprise tests with kong-gateway container image version 3.1.1.3-debian
- Update kong ingress controller to [2.8.1](https://github.com/Kong/kong/blob/2.8.1/CHANGELOG.md#281)
- Update custom resource definitions to those used by kong ingress controller [2.8.1]

### Changes

- **Breaking** The `minReadySeconds` value previous found at `deployment.kong.minReadySeconds` is now configured at path `deployment.minReadySeconds`.
- Increase default requests/limits to 1 cpu and 2G memory
- Remove startupProbe from kong ingress controller. [More information](https://github.com/Kong/charts/pull/527#issuecomment-1014782921)

## [2.14.0] - 2023-02-01

### Changes

- Add instance label to default topologySpreadConstraints label selector
- Update kong/kubernetes-ingress-controller to [2.8.1](https://github.com/Kong/kubernetes-ingress-controller/releases/tag/v2.8.1).
- Suggest using giantswarm/kong-gateway:2.8.2.3-debian as enterprise container image.
- Use `/readyz` path for ingress controller readiness check.
- Update kubernetes api token secret with projected volume. This should fix problems with empty or expired ServiceAccount tokens.

## [2.13.0] - 2022-10-25

This version drops support for kubernetes versions below 1.22.0.

### Updates

- Update kong/kubernetes-ingress-controller to [2.7.0](https://github.com/Kong/kubernetes-ingress-controller/releases/tag/v2.7.0). More information can be found in the [Changelog entry](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#breaking-changes) of the kong kubernetes Ingress controller.

## [2.12.0] - 2022-09-20

### Added

- Service for scraping metrics from ingress controller

### Updates

- Align with upstream chart version [2.13.0](https://github.com/Kong/charts/releases/tag/kong-2.13.0) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.11.0...kong-2.13.0)). Please note this release does not contain kong 3.0.0 yet.
- Update kong/kubernetes-ingress-controller to [2.6.0](https://github.com/Kong/kubernetes-ingress-controller/releases/tag/v2.6.0)

## [2.11.0] - 2022-08-03

### Updates

- Align with upstream chart version [2.11.0](https://github.com/Kong/charts/releases/tag/kong-2.11.0) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.8.2...kong-2.11.0))
- Update kong/kubernetes-ingress-controller to [2.5.0](https://github.com/Kong/kubernetes-ingress-controller/releases/tag/v2.5.0)

## [2.10.1] - 2022-07-29

### Updates

- Update kubectl container image to 1.24.2 in CRD install job.

### Fixes

- Make sure all container images use the same container registry.

## [2.10.0] - 2022-06-02

### Updates

- Enable PodDisruptionBudget to require at least one pod running.
- Increase default replica count to two.
- Change default affinity to prevent scheduling on the same node.
- Align with upstream chart version [2.8.2](https://github.com/Kong/charts/releases/tag/kong-2.8.2) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.7.0...kong-2.8.2))

## [2.9.0] - 2022-04-14

This release contains a breaking change introduced by a change to the `spec.controller` value of the `IngressClass` installed by this Helm chart.

Before upgrading to this version, you'll need to manually delete the `IngressClass` managed by this Helm chart.

```
kubectl delete ingressclass <class name, "kong" by default>
```

More information in the [upstream "Upgrade considerations" documentation](https://github.com/Kong/charts/blob/main/charts/kong/UPGRADE.md#ingressclass-controller-name-change-requires-manual-delete).

### Updates

- Align with upstream chart version [2e89647](https://github.com/Kong/charts/tree/2e89647d86ec7c8fa2a2a1697a325e6679b18d08) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.7.0...2e89647))
- Update kong/kubernetes-ingress-controller to [2.3.1](https://github.com/Kong/kubernetes-ingress-controller/releases/tag/v2.3.1)
- Update kong/kong to [2.8.1](https://github.com/Kong/kong/blob/2.8.1/CHANGELOG.md#281). This fixes OpenSSL [CVE-2022-0778](https://nvd.nist.gov/vuln/detail/CVE-2022-0778).
- Execute enterprise tests with container image version 2.8.1.0-alpine

## [2.8.0] - 2022-03-28

### Added

- Added team ownership to default labels.
- Default `affinity` and `topologySpreadConstraints` to make sure pods are spread evenly across zones.

## [2.7.2] - 2022-03-10

### Fixes

- Pin user and group ID to 1000 in CRD install helm hook job

## [2.7.1] - 2022-02-16

### Fixes

- Handle empty `image.registry` in CRD install job

## [2.7.0] - 2022-02-16

### Added

- CRD update job via helm hooks

### Updates

- Align with upstream chart version [2.7.0](https://github.com/Kong/charts/releases/tag/kong-2.7.0)
- Update kong/kubernetes-ingress-controller to [2.2.1](https://github.com/Kong/kubernetes-ingress-controller/releases/tag/v2.2.1)

## [2.6.0] - 2022-02-11

### Fixes

- Disable Secrets creation validation in ValidatingWebhookConfiguration. This fixes deployments with `ingressController.admissionWebhook.enabled` in values.

### Updates

- Align with upstream chart version [26eff4f](https://github.com/Kong/charts/tree/26eff4f94d23f272a64efdfff3a5d109d923b6df) ([Changes in upstream repository](https://github.com/Kong/charts/compare/kong-2.6.4...26eff4f))
- Update kong/kubernetes-ingress-controller to [2.1.1](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#211)
- Update kong/kong to [2.7.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#271)

## [2.5.0] - 2022-01-18

### Added

- Adds KIC startupProbes to allow longer boot times in big clusters. As stated in [upstream docs](https://github.com/Kong/kubernetes-ingress-controller/pull/1742/files#diff-4c367c8cb3b51bfff330a4004032f813e7c5a4f309d0d2a07b8010bc4fee69d3R25), during boot time it gathers all Services, Endpoints and Secrets on the cluster, which can take longer than the liveness probe threshold.

## [2.4.0] - 2022-01-12

### Breaking Changes

- KIC now defaults to version 2.1. If you use a database, you must first perform a temporary intermediate upgrade to disable KIC before upgrading it to 2.x and re-enabling it. See the [upgrade guide](https://github.com/giantswarm/kong-app/blob/master/helm/kong-app/UPGRADE.md#disable-ingress-controller-prior-to-2x-upgrade-when-using-postgresql) for detailed instructions.
- ServiceAccount are now always created by default unless explicitly disabled. ServiceAccount customization has [moved under the `deployment` section of configuration](https://github.com/giantswarm/kong-app/blob/master/helm/kong-app/UPGRADE.md#changed-serviceaccount-configuration-location) to reflect this. This accommodates configurations that need a ServiceAccount but that do not use the ingress controller. ([#455](https://github.com/Kong/charts/pull/455))

### Updates

- Align with upstream chart [2.6.4](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#264)
- Default Kong IC version updated to 2.1
- Default Kong proxy version updated to 2.7

**Note** chart versions 2.3.0 through 2.5.0 contained an incorrect KongIngress CRD. The proxy.path field was missing. Helm will not fix this automatically on upgrade. You can fix it by running:
```
kubectl apply -f https://raw.githubusercontent.com/Kong/charts/main/charts/kong/crds/custom-resource-definitions.yaml
```

For a detailed description of all the changes please check the [upstream changelog](https://github.com/giantswarm/kong-app/blob/master/helm/kong-app/CHANGELOG.md)

## [2.3.5] - 2021-12-14

### Added

- Adds annotation `giantswarm.io/monitoring-app-label` to metrics (status) service as a persistent identifier for monitoring

## [2.3.4] - 2021-12-02

### Fixed

- metricsService template and default values to align with chart design
- remove un-required podAnnotations from values.yaml

### Added

- required serviceAnnotations to values.yaml
- label `giantswarm.io/service-type: "managed"` so managed app monitoring rules are applied

## [2.3.3] - 2021-11-24

### Added

- Add monitoring label so Kong is scraped by monitoring infrastructure.

## [2.3.2] - 2021-10-05

### Added

- Option to specify [Min Ready Seconds](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#min-ready-seconds) to kong deployment to mitigate kong dropping traffic during upgrades.

## [2.3.1] - 2021-09-14

### Fixed

- Fix lookup for CA secret for admission webhook.

## [2.3.0] - 2021-08-25

### Breaking Changes

**Please check ["Breaking Changes" paragraph](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#changelog) of upstream changelog for details**

Overview:
- Upgraded CRDs to V1 from the previous deprecated v1beta1.
- Added support for controller metrics ot the Prometheus resources.

### Updates

- Align with upstream chart [2.3.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#230) which includes updates for kong to [2.5](https://github.com/Kong/kong/blob/master/CHANGELOG.md#250) and kong ingress controller [1.3.0](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#130---20210527). For more information check the linked changelogs.

## [2.1.0] - 2021-06-15

### Updates

- Update to align with upstream chart [2.1.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#210) which includes updates for kong to [2.4.1](https://github.com/Kong/kong/blob/master/CHANGELOG.md#241) and kong ingress controller [1.2.0](https://github.com/Kong/kubernetes-ingress-controller/blob/main/CHANGELOG.md#120---20210324). For more information check the linked changelogs.

## [2.0.0] - 2021-05-07

2.0.0 marks the stable release of synchronization with upstream [2.0.0](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#200).

Make sure to review the upstream [changelog](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#200) and the [upgrade documentation](https://github.com/giantswarm/kong-app/blob/master/helm/kong-app/UPGRADE.md).

## [1.2.0] - 2021-03-04

### IMPORTANT

>1.15.0 is an interim release before the planned release of 2.0.0. There were
several feature changes we wanted to release prior to the removal of deprecated
functionality for 2.0. The original planned deprecations covered in the [1.14.0
changelog](#1140) are still planned for 2.0.0.

This update bundles all changes since upstream chart version [1.12.0](https://github.com/Kong/charts/tree/kong-1.12.0)

Make sure to review the upstream [changelog](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#200) and the [upgrade documentation](https://github.com/giantswarm/kong-app/blob/master/helm/kong-app/UPGRADE.md).

### Updates

- architect-orb 0.18.1 --> 2.1.0
- Kong 2.2 --> 2.3
- upstream chart 1.12.0 --> 1.15.0

See [upgrade documentation](https://github.com/giantswarm/kong-app/blob/master/helm/kong-app/UPGRADE.md) for detailed list of changes and improvements.

## [1.1.4] - 2021-04-15

### Updated

- Update kong image version to 2.2.3

Reference:
- https://github.com/Kong/kong/issues/6739

## [.1.1.3] - 2021-04-14

### Added

- Fix for golang 1.15 deprecation of "legacy Common Name field"

Reference:
- https://github.com/golang/go/issues/39568#issuecomment-671424481

## [1.1.2] - 2021-03-02

### Changed

- Do not set `waitImage.repository` in alignment with upstream.

## [1.1.1] - 2021-03-02

### Added
- Added values.schema.json for validation of default values

### Fixed

- Change `waitImage` values to make migration pods work. [#100](https://github.com/giantswarm/kong-app/pull/100)

## [v1.1.0] - 2020-12-02

### Updated

- Update architect-orb to 0.18.1
- Sync with upstream chart [1.12.0](https://github.com/Kong/charts/tree/kong-1.12.0). Please check the upstream [changelog](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#1120).

## [v1.0.0] - 2020-10-13

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
- Please check the upstream [CHANGELOG.md](https://github.com/Kong/charts/blob/main/charts/kong/CHANGELOG.md#1110)

### Changed

- Change upstream default branch in upstream-sync script

## [v0.9.2] - 2020-10-29

### Added

- Add minReadySeconds to deployment template as optional parameter

### Updated

- architect-orb 0.11.0 -> 0.14.0
- github workflow

## [v0.9.1] - 2020-09-07

### Changed

- Split registry value to allow switching registry.

## [v0.9.0] - 2020-08-25

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

[Unreleased]: https://github.com/giantswarm/kong-app/compare/v4.0.0...HEAD
[4.0.0]: https://github.com/giantswarm/kong-app/compare/v3.8.0...v4.0.0
[3.8.0]: https://github.com/giantswarm/kong-app/compare/v3.7.0...v3.8.0
[3.7.0]: https://github.com/giantswarm/kong-app/compare/v3.6.2...v3.7.0
[3.6.2]: https://github.com/giantswarm/kong-app/compare/v3.6.1...v3.6.2
[3.6.1]: https://github.com/giantswarm/kong-app/compare/v3.6.0...v3.6.1
[3.6.0]: https://github.com/giantswarm/kong-app/compare/v3.5.0...v3.6.0
[3.5.0]: https://github.com/giantswarm/kong-app/compare/v3.4.0...v3.5.0
[3.4.0]: https://github.com/giantswarm/kong-app/compare/v3.3.0...v3.4.0
[3.3.0]: https://github.com/giantswarm/kong-app/compare/v3.2.0...v3.3.0
[3.2.0]: https://github.com/giantswarm/kong-app/compare/v3.1.1...v3.2.0
[3.1.1]: https://github.com/giantswarm/kong-app/compare/v3.1.0...v3.1.1
[3.1.0]: https://github.com/giantswarm/kong-app/compare/v3.0.1...v3.1.0
[3.0.1]: https://github.com/giantswarm/kong-app/compare/v3.0.0...v3.0.1
[3.0.0]: https://github.com/giantswarm/kong-app/compare/v2.14.0...v3.0.0
[2.14.0]: https://github.com/giantswarm/kong-app/compare/v2.13.0...v2.14.0
[2.12.0]: https://github.com/giantswarm/kong-app/compare/v2.11.0...v2.12.0
[2.11.0]: https://github.com/giantswarm/kong-app/compare/v2.10.1...v2.11.0
[2.10.1]: https://github.com/giantswarm/kong-app/compare/v2.10.0...v2.10.1
[2.10.0]: https://github.com/giantswarm/kong-app/compare/v2.9.0...v2.10.0
[2.9.0]: https://github.com/giantswarm/kong-app/compare/v2.8.0...v2.9.0
[2.8.0]: https://github.com/giantswarm/kong-app/compare/v2.7.2...v2.8.0
[2.7.2]: https://github.com/giantswarm/kong-app/compare/v2.7.1...v2.7.2
[2.7.1]: https://github.com/giantswarm/kong-app/compare/v2.7.0...v2.7.1
[2.7.0]: https://github.com/giantswarm/kong-app/compare/v2.6.0...v2.7.0
[2.6.0]: https://github.com/giantswarm/kong-app/compare/v2.5.0...v2.6.0
[2.5.0]: https://github.com/giantswarm/kong-app/compare/v2.4.0...v2.5.0
[2.4.0]: https://github.com/giantswarm/kong-app/compare/v2.3.5...v2.4.0
[2.3.5]: https://github.com/giantswarm/kong-app/compare/v2.3.4...v2.3.5
[2.3.4]: https://github.com/giantswarm/kong-app/compare/v2.3.3...v2.3.4
[2.3.3]: https://github.com/giantswarm/kong-app/compare/v2.3.2...v2.3.3
[2.3.2]: https://github.com/giantswarm/kong-app/compare/v2.3.1...v2.3.2
[2.3.1]: https://github.com/giantswarm/kong-app/compare/v2.3.0...v2.3.1
[2.3.0]: https://github.com/giantswarm/kong-app/compare/v2.1.0...v2.3.0
[2.1.0]: https://github.com/giantswarm/kong-app/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/giantswarm/kong-app/compare/v1.2.0...v2.0.0
[1.2.0]: https://github.com/giantswarm/kong-app/compare/v1.1.4...v1.2.0
[1.1.4]: https://github.com/giantswarm/kong-app/compare/v1.1.3...v1.1.4
[1.1.3]: https://github.com/giantswarm/kong-app/compare/v1.1.2...v1.1.3
[1.1.2]: https://github.com/giantswarm/kong-app/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/giantswarm/kong-app/compare/v1.1.0...v1.1.1
[v1.1.0]: https://github.com/giantswarm/kong-app/compare/v1.0.0...v1.1.0
[v1.0.0]: https://github.com/giantswarm/kong-app/compare/v0.9.2...v1.0.0
[v0.9.2]: https://github.com/giantswarm/kong-app/compare/v0.9.1...v0.9.2
[v0.9.1]: https://github.com/giantswarm/kong-app/compare/v0.9.0...v0.9.1
[v0.9.0]: https://github.com/giantswarm/kong-app/compare/v0.8.3...v0.9.0
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
