#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

repo_dir=$(git rev-parse --show-toplevel) ; readonly repo_dir

cd "${repo_dir}"

set -x
sed -i \
        -e '/^icon:/c\icon: https://s.giantswarm.io/app-icons/kong/1/light.svg' \
        -e '/^home:/c\home: https://github.com/giantswarm/kong-app' \
        -e '/^version:/c\version: 4.1.0' \
        -e '/^appVersion:/c\appVersion: "3.6.1.4"' \
        -e '/^    repository:/c\    repository: oci://registry-1.docker.io/bitnamicharts' \
        -e '/^sources:/a\  - https://github.com/giantswarm/kong-app' \
        -e '$akubeVersion: ">=1.22.0-0"\nannotations:\n  application.giantswarm.io/team: "cabbage"' \
        "./vendor/kong/charts/kong/Chart.yaml"

{ set +x; } 2>/dev/null
