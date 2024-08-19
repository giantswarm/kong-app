Remove `service-kong-metrics.yaml.patch` after figuring out if the legacy way of scraping metrics using services with `giantswarm.io/monitoring` labels is already gone

```
git --no-pager diff --no-index -R --no-color helm/kong-app/templates/service-kong-metrics.yaml /dev/null > sync/patches/servicemonitor/service-kong-metrics.yaml.patch

# Replace all `/helm/kong-app/` with `/vendor/kong/charts/kong/`.
sed -i 's#/helm/kong-app/#/vendor/kong/charts/kong/#g' \
        sync/patches/servicemonitor/service-kong-metrics.yaml.patch
```
