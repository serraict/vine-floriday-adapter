# Contributing

This document describes how we work and collaborate on this project.
It describes our workflow
and outlines the specific criteria that must be met
for a new increment of our application to be considered releasable.
It serves as a checklist for developers and AI agents to ensure quality and consistency in our releases.

## Workflow

In our [backlog] we list what we think we need to build to achieve our [product vision].
In [doing] we describe what we are currently working on.
Maintaining this information in plain text in out repository allows us to easily collaborate with AI agents.

## Code Quality

Our code is well-readable and understandable for humans and AI agents.
For this application, we prefer readability, simplicity, and understandability over performance.

We lint with `flake8`, format with `black` and `pytest` before we commit.
Enforced on merges to `main` by [`ci.yml` Github action](.github/workflows/ci.yml).

Measure: `make quality`

## Testing

We validate our code by testing it.
Do not add code without tests.
Fast, local unit tests can be run without any prerequisites.
These tests are part of our CI job.

Measure: `make test`

Our integration tests require access to a local database and a Floriday staging environment.
These tests ensure our application works end-to-end.
These tests as of now are not part of our CI job and need to be executed manually before creating a release.

To run integration tests:

1. Load the required credentials: `source scripts/load_credentials.sh`
2. Verify connectivity: `floridayvine about` (this checks database and API connectivity)
3. Run the tests: `make test-integration`

Measure: `make test-integration`

## Documentation

Our documentation should help our players to make their next move in the game.
The documentation is accessible to the end users on the command line.

For other players, we rely on manual inspection of the following:

- [ ] <../CHANGELOG.md> is updated with any new features, dependencies, or usage instructions
- [ ] Any new environment variables are added to both `.env.example` and `mongo/.env.default`
- [ ] <../docs/software_architecture.md> is up-to-date with the current architecture and design forces.
- [ ] <../docs/cli_documentation.md> is helpful to get an overview of the capabilities of the application.

## Performance and Security

For now, these require manual verification:

- [ ] No sensitive information (API keys, passwords) is hardcoded or logged
- [ ] All database queries are optimized and indexed appropriately
- [ ] Environment variables are used for all configuration options

## DevOps

- [ ] `Dockerfile` and `docker-compose.yml` are updated if there are new dependencies or services
- [ ] `requirements-dev.txt` is updated with any new development dependencies
- [ ] Version number is incremented appropriately
- [ ] Configuration files (.flake8, .pre-commit-config.yaml, .vscode/settings.json) are up-to-date and committed to the repository

## Cross platform compatibility

- [ ] Application runs successfully on both development and production environments
- [ ] Any new dependencies are added to `pyproject.toml` and are compatible with both Linux and macOS

## Release and Deployment

Running `make release` will take care of:

- [x] Code and documentation are pushed to the central code repository
- [x] Release is identified using Semantic Versioning
- [x] Release is tagged in the repository
- [x] GitHub Actions package workflow successfully builds and publishes the Docker container to <https://ghcr.io/serraict/vine-floriday-adapter>.

Additionally, for each release:

- [ ] CHANGELOG.md is updated following the guidelines from https://keepachangelog.com/, documenting all changes since the last release

## Final Checks

- [ ] GitHub Actions CI workflow passes on the main branch, running all quality checks
- [ ] Application can be built and run using `docker-compose up` without errors

## Undone for now

The following items are considered important for future releases but are not currently part of our Definition of Done:

- [ ] Implement test coverage measurement and maintain or improve coverage (verify with coverage tool)
- [ ] Create a script to automatically check if all environment variables in `.env.example` and `mongo/.env.default` are up to date
- [ ] Implement a zipped version of the code for download as part of the release process
- [ ] Test the application in both development and production environments.
- [ ] Document our application using specification by example. For now, we use simple `pytest`s.
- [ ] Cross platform compatibility
  - [ ] Linux
  - [ ] Mac OSX

This contributing guideline should be reviewed and updated periodically to reflect the evolving needs of the project.
Items from the "Undone for now" section should be considered for inclusion in the main DoD as they become implemented and integrated into our development process.

[backlog]: ./work/backlog.md
[doing]: ./work/doing.md
[product vision]: ./readme.md
