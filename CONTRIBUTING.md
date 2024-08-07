# How to contribute

This project is Apache 2.0 licensed and accepts contributions via GitHub pull requests. This document contains some information to make getting your contribution easier.

## Getting started

- Fork the repository on GitHub
- Read the [README.md](https://github.com/giantswarm/kong-app/blob/main/README.md) for instructions on chart development and testing

The helm chart included in this repository is meant to be used within the [Giant Swarm App Plattform](https://docs.giantswarm.io/getting-started/app-platform/) but can be installed with plain helm.

## Support

Whether you are a user or contributor, you can reach us by:

- [GitHub issues][github_issues]

Before creating an issue or submitting a new pull request, please check that the issue hasn't already been reported or is a known issue that we are aware of. Please also check the [Giant Swarm Roadmap](https://github.com/giantswarm/roadmap/).

## Reporting Bugs and Creating Issues

Reporting bugs is one of the best ways to contribute. If you find bugs or documentation mistakes in the project, please let us know by [opening an issue][github_issues]. We treat bugs and mistakes very seriously and believe no issue is too small. Before creating a bug report, please check there that one does not already exist.

You might also want to read [Elika Etemad’s article on filing good bug reports](http://fantasai.inkedblade.net/style/talks/filing-good-bugs/) before creating a bug report.

To make your bug report accurate and easy to understand, please try to create bug reports that are:

- Specific. Include as many details as possible: which version, what environment, what configuration etc. You can also attach logs and/or screenshots.

- Reproducible. Include the steps to reproduce the problem. We understand some issues might be hard to reproduce, please include the steps that might lead to the problem. If applicable, you can also attach affected data dir(s) and a stack trace to the bug report.

- Isolated. Please try to isolate and reproduce the bug with minimum dependencies. It would significantly slow down the speed to fix a bug if too many dependencies are involved in a bug report. Debugging external systems that rely on this project is out of scope, but we are happy to point you in the right direction or help you interact with our project in the correct manner.

- Unique. Do not duplicate existing bug reports.

- Scoped. One bug per report. Do not follow up with another bug inside one report.


We might ask you for further information to locate a bug. A duplicated bug report will be closed.

## Contribution flow

This is a rough outline of what a contributor's workflow looks like:

- Create a feature branch from where you want to base your work. This is usually main.
- Make commits of logical units.
- Make sure your commit messages are in the proper format (see below).
- Push your changes to a topic branch in your fork of the repository.
- Submit a pull request to our project. Follow the instructions in the [Pull Request template](https://github.com/giantswarm/kong-app/blob/main/.github/pull_request_template.md)
- Adding unit tests will greatly improve the chance for getting a quick review and your PR accepted.
- Your PR must receive a LGTM from a maintainer.
- We're squashing all commits into a single commit when merging to main.

Thanks for your contributions!

### Format of the Commit Message

We follow a rough convention for committing messages that are designed to answer two questions: what changed and why. The subject line should feature the what and the body of the commit should describe the why.

[github_issues]: https://github.com/giantswarm/kong-app/issues/new
