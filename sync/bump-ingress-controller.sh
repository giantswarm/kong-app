#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

repo_dir=$(git rev-parse --show-toplevel) ; readonly repo_dir
script_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) ; readonly script_dir

cd "${repo_dir}"

readonly script_dir_rel=".${script_dir#"${repo_dir}"}"
values_file="helm/kong-app/values.yaml"

new_tag="3.2.5"

set -x

vendir sync

sed -i "/ingressController:/,/tag:/s/tag: \".*\"/tag: \"$new_tag\"/" "$values_file"

git --no-pager diff -R --no-color --no-index "$values_file" vendor/kong/charts/kong/values.yaml > \
        "$script_dir/patches/values-schema/values.yaml.patch"
sed -i "s|b/vendor/kong/charts/kong/values.yaml|b/$value_file|" \
        "$script_dir/patches/values-schema/values.yaml.patch"

{ set +x; } 2>/dev/null
