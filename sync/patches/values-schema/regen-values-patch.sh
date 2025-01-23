#!/bin/bash

set -x

git --no-pager diff -R --no-color --no-index helm/kong-app/values.yaml vendor/kong/charts/kong/values.yaml > sync/patches/values-schema/values.yaml.patch
set -e
sed -i 's|b/vendor/kong/charts/kong/values.yaml|b/helm/kong-app/values.yaml|' sync/patches/values-schema/values.yaml.patch
