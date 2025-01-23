#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

repo_dir=$(git rev-parse --show-toplevel) ; readonly repo_dir
script_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) ; readonly script_dir

cd "${repo_dir}"

readonly script_dir_rel=".${script_dir#"${repo_dir}"}"

set -x
# Copy our custom VPA template
cp "${script_dir_rel}/vpa.yaml" ./helm/kong-app/templates/vpa.yaml
mkdir -p ./vendor/kong/charts/kong/templates
touch ./vendor/kong/charts/kong/templates/vpa.yaml

{ set +x; } 2>/dev/null
