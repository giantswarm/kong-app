Remove this patch once https://github.com/Kong/charts/pull/1244 is merged and released upstream

### Regenerate patch

- `vendir sync`
- Re-add line `unhealthyPodEvictionPolicy: {{ .Values.podDisruptionBudget.unhealthyPodEvictionPolicy }}` to `templates/pdb.yaml`
- `git --no-pager diff -R --no-color --no-index helm/kong-app/templates/pdb.yaml vendor/kong/charts/kong/templates/pdb.yaml > sync/patches/pdb-unhealthypodevictionpolicy/pdb.yaml.patch`
- `sed -i 's|b/vendor/kong/charts/kong/templates/pdb.yaml|b/helm/kong-app/templates/pdb.yaml|' sync/patches/pdb-unhealthypodevictionpolicy/pdb.yaml.patch`
