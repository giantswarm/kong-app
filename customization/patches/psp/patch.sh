#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

repo_dir=$(git rev-parse --show-toplevel) ; readonly repo_dir

cd "${repo_dir}"

psp_template="./vendor/kong/charts/kong/templates/psp.yaml"

set -x

sed -i '1c{{- if and (not .Values.global.podSecurityStandards.enforced) (.Values.podSecurityPolicy.enabled) (.Capabilities.APIVersions.Has "policy/v1beta1") }}' "$psp_template"

{ set +x; } 2>/dev/null
