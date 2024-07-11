# The Giant Swarm default values for kong

In case you run into `error: helm/kong-app/values.yaml: patch does not apply`, do the following:

- Obtain the upstream `values.yaml` by executing `vendir sync`
- Restore the current `values.yaml` to its state before the patch (`git restore --source=HEAD --staged --worktree helm/kong-app/values.yaml`)
- Edit Giant Swarm values in `helm/kong-app/values.yaml` until `git diff -R --no-index helm/kong-app/values.yaml vendor/kong/charts/kong/values.yaml` looks good. **Do not stage (`git add`) the changes**!
- Re-generate the patch file

      git --no-pager diff -R --no-color --no-index helm/kong-app/values.yaml vendor/kong/charts/kong/values.yaml > \
        sync/patches/values-schema/values.yaml.patch
      sed -i 's|b/vendor/kong/charts/kong/values.yaml|b/helm/kong-app/values.yaml|' \
         sync/patches/values-schema/values.yaml.patch

- Once the patch looks good, do `git add sync/patches/values-schema/values.yaml.patch`

In case of changes (additions, removals or type changes) in the `values.yaml`, read on

The `values.schema.json` is a mixture of running

```
$ helm plugin install https://github.com/karuppiah7890/helm-schema-gen
$ helm schema-gen helm/kong-app/values.yaml > sync/patches/values-schema/values.schema.json
```

and by-hand editing.

Remove `null` and and replace it with `["null", "<the-right-type>"]`
