The schema is a mixture of running

```
$ helm plugin install https://github.com/karuppiah7890/helm-schema-gen
$ helm schema-gen <values-yaml-file>
```

and by-hand editing.

Remove `null` and and replace it with `["null", "<the-right-type>"]`
