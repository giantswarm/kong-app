- **This repository allows merge commits, if you're creating a Release, make sure to select 'Squash and merge'**
- **When merging subtree updates, it is important to select 'Create a merge commit' when merging.**

<!--
@giantswarm/team-cabbage will be automatically requested for review once
this PR has been submitted.
-->

<!--
Please update after a release:
- the version matrix in README.md
- the kong-gateway tag in tests/test-values-enterprise.yaml
-->

This PR...

## Checklist

- [ ] Automated test are working (for chart changes)
- [ ] Changelog entry has been added

### Manual tests on workload clusters

For plain installations (default values) and database mode (deploy `tests/manual/postgres.yaml`, then install with `tests/manual/values-database.yaml`), execute these tests. If you have additional configuration, make sure your existing deployments with custom values still work.

- [ ] Upgrade from previous version works
- [ ] Existing Ingress resources are reconciled correctly (change domain, see if its available)
- [ ] Fresh install works
- [ ] Fresh Ingress resources are reconciled correctly
