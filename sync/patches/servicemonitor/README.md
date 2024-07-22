Remove `servicemonitor.yaml.patch` once https://github.com/Kong/charts/pull/1095 is released in kong chart


Remove `service-kong-metrics.yaml.patch` after figuring out if the legacy way of scraping metrics using services with `giantswarm.io/monitoring` labels is already gone

```
git --no-pager diff --no-index -R --no-color helm/kong-app/templates/service-kong-metrics.yaml /dev/null > customization/patches/servicemonitor/service-kong-metrics.yaml.patch

# Replace all `/helm/kong-app/` with `/vendor/cilium/install/kubernetes/cilium/`.
sed -i 's#/helm/kong-app/#/vendor/kong/charts/kong/#g' \
        customization/patches/servicemonitor/service-kong-metrics.yaml.patch
```
