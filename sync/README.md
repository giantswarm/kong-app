# Sync chart from upstream

We're trying to align the chart in this repository as closely as possible to the [kong upstream chart](https://github.com/Kong/charts/tree/main/charts/kong).

For this, [vendir](https://github.com/carvel-dev/vendir) and a series of [patches](https://github.com/giantswarm/kong-app/tree/main/sync/patches) are being used. See the `README.md` and `patch.sh` files inside the patch directories for more information about each patch.

**To sync the chart from upstream install `vendir` and execute `./sync/sync.sh` in the root of the repository.**

## Sync from upstream

Scenario: Upstream released a new chart version and you want to update our chart.

- In `vendir.yml`: Change the `directories[0].contents[0].git.ref` field to the new git tag or sha
- Run `./sync/sync.sh`
- Fix syncing errors by changing the patches in `sync/patches`
- In case of container image version changes:
  - Update the container image references by following instructions in [Changes to default `values.yaml`](#changes-to-default-valuesyaml)
  - Update the `appVersion` field in `helm/kong-app/Chart.yaml`
- Commit your changes in directories `sync`, `diffs` and `helm`

## Changes to default `values.yaml`

The default values file `helm/kong-app/values.yaml` is the source of truth for creating the patch to restore itself to the state held in this repository after syncing.

Follow instructions in [`sync/patches/values-schema/README.md`](sync/patches/values-schema/README.md) and dont' forget to run `./sync/sync.sh` once the patch looks good.

## General chart changes

Changes to chart templates or helpers follow the approach of maintaining patches or scripts that can be applied to the upstream chart.

Each change should have its own patch directory in `sync/patches` and have an executable `patch.sh` script.

The `patch.sh` script is being called by `sync/sync.sh` and contains code to transform the upstream chart in `vendor/kong/charts/kong` into the desired version in `helm/kong-app`.
