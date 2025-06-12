#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

repo_dir=$(git rev-parse --show-toplevel) ; readonly repo_dir
script_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) ; readonly script_dir

cd "${repo_dir}"

versions="v3.0.2 v3.1.6 v3.2.4 v3.3.1 v3.4.3 v3.4.6"

for version in $versions; do
    crds_file="./helm/kong-app/crds/custom-resource-definitions-${version}.yaml"
    # Fetch CRDs file
    echo "# generated using: kubectl kustomize 'github.com/kong/kubernetes-ingress-controller/config/crd?ref=${version}'" > "$crds_file"
    kubectl kustomize "github.com/kong/kubernetes-ingress-controller/config/crd?ref=${version}" >> "$crds_file"
done

# Add kubectl-apply-job call to CRDs template
readonly script_dir_rel=".${script_dir#"${repo_dir}"}"

set -x
git apply "${script_dir_rel}/custom-resource-definitions.yaml.patch"

{ set +x; } 2>/dev/null
