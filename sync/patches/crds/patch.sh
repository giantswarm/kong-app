#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

repo_dir=$(git rev-parse --show-toplevel) ; readonly repo_dir
script_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) ; readonly script_dir

cd "${repo_dir}"

kong_ingress_controller_version="v3.1.3"
crds_file="./helm/kong-app/crds/custom-resource-definitions.yaml"

# Fetch right CRDs file
echo "# generated using: kubectl kustomize 'github.com/kong/kubernetes-ingress-controller/config/crd?ref=${kong_ingress_controller_version}'" > "$crds_file"
kubectl kustomize "github.com/kong/kubernetes-ingress-controller/config/crd?ref=${kong_ingress_controller_version}" >> "$crds_file"

# Add kubectl-apply-job call to CRDs template
readonly script_dir_rel=".${script_dir#"${repo_dir}"}"

set -x
git apply "${script_dir_rel}/custom-resource-definitions.yaml.patch"

sed -i \
    -e '/^dependencies:/a\  - name: kubectl-apply-job\n    version: "0.7.0"\n    repository: oci://giantswarmpublic.azurecr.io/giantswarm-playground-catalog' \
    "./helm/kong-app/Chart.yaml"

# Instead of running `helm dependency update` which will change the
# `digest` and `generated` fields in the `Chart.lock`, we're copying
# a static version which needs manual update if something changes in
# the `dependencies` of `Chart.yaml`
# $ helm dependency update "./vendor/kong/charts/kong"
cp "${script_dir_rel}/Chart.lock" "./helm/kong-app/Chart.lock"

{ set +x; } 2>/dev/null
