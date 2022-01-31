- **This repository allows merge commits, if you're creating a Release, make sure to select 'Squash and merge'**
- **When merging subtree updates, it is important to select 'Create a merge commit' when merging.**

<!--
@giantswarm/team-cabbage will be automatically requested for review once
this PR has been submitted.
-->

This PR...

## Checklist

- [ ] Automated test are working
- [ ] Changelog entry has been added

### Manual tests on workload clusters (not always required)

- [ ] Upgrade from previous version works
- [ ] Existing Ingress resources are reconciled correctly (change domain, see if its available)
- [ ] Fresh install works
- [ ] Fresh Ingress resources are reconciled correctly
