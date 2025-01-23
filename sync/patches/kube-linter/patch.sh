#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

repo_dir=$(git rev-parse --show-toplevel) ; readonly repo_dir
script_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) ; readonly script_dir

cd "${repo_dir}"

readonly script_dir_rel=".${script_dir#"${repo_dir}"}"

set -x
# Only try to copy if the source file exists
mkdir -p ./vendor/kong/charts/kong
if [ -f ./vendor/kong/charts/kong/.kube-linter.yaml ]; then
  cp ./vendor/kong/charts/kong/.kube-linter.yaml ./helm/kong-app/.kube-linter.yaml
  git apply "${script_dir_rel}/kube-linter.yaml.patch"
else
  # If source doesn't exist, just copy our version
  cp "${script_dir_rel}/.kube-linter.yaml" ./helm/kong-app/.kube-linter.yaml
  touch ./vendor/kong/charts/kong/.kube-linter.yaml
fi

{ set +x; } 2>/dev/null
