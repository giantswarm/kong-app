#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) ; readonly dir
cd "${dir}/.."

set -x
# Sync using vendir
vendir sync
{ set +x; } 2>/dev/null

# Patches
./sync/patches/crds/patch.sh
./sync/patches/values-schema/patch.sh
./sync/patches/affinity-topologyspreadconstraints/patch.sh
./sync/patches/psp/patch.sh
./sync/patches/servicemonitor/patch.sh
./sync/patches/gs-helpers/patch.sh
./sync/patches/vpa/patch.sh
./sync/patches/helmignore/patch.sh
./sync/patches/kube-linter/patch.sh

# Store diffs
rm -f ./diffs/*
for f in $(git --no-pager diff --no-exit-code --no-color --no-index vendor/kong/charts/kong helm/kong-app --name-only) ; do
        set +e
        set -x
        git --no-pager diff --no-exit-code --no-color --no-index "vendor/kong/charts/kong/${f#"helm/kong-app/"}" "${f}" \
                > "./diffs/${f//\//__}.patch" # ${f//\//__} replaces all "/" with "__"
        ret=$?
        { set +x; } 2>/dev/null
        set -e
        if [ $ret -ne 0 ] && [ $ret -ne 1 ] ; then
                exit $ret
        fi
done