# Definition of Done

This document outlines the specific criteria that must be met for a new increment of our application to be considered releasable.
It serves as a checklist for developers and AI agents to ensure quality and consistency in our releases.

## Code Quality and Testing

- [ ] `make quality` command passes, which includes:
  - Linting with `flake8` (as configured in .flake8)
  - Formatting with `black`
  - Running pre-commit hooks
  - Running non-integration tests with `pytest`
- [ ] All new functionality has corresponding unit tests in the `tests/` directory
- [ ] GitHub Actions CI workflow passes on the main branch

## Documentation

- [ ] README.md is updated with any new features, dependencies, or usage instructions
- [ ] Any new environment variables are added to both `.env.example` and `mongo/.env.default`
- [ ] `docs/software_architecture.md` is up-to-date with the current architecture and design forces.

## Functionality

- [ ] All new CLI commands are implemented in `src/floridayvine/commands/` and properly integrated in `src/floridayvine/__main__.py`

## Performance and Security

- [ ] No sensitive information (API keys, passwords) is hardcoded or logged
- [ ] All database queries are optimized and indexed appropriately
- [ ] Environment variables are used for all configuration options

## DevOps and Deployment

- [ ] `Dockerfile` and `docker-compose.yml` are updated if there are new dependencies or services
- [ ] `requirements-dev.txt` is updated with any new development dependencies
- [ ] Version number is incremented appropriately
- [ ] Configuration files (.flake8, .pre-commit-config.yaml, .vscode/settings.json) are up-to-date and committed to the repository

## Cross-compatibility

- [ ] Application runs successfully on both development and production environments
- [ ] Any new dependencies are added to `pyproject.toml` and are compatible with both Linux and macOS

## Release and Deployment

- [ ] Code and documentation are pushed to the central code repository
- [ ] Release is identified using Semantic Versioning
- [ ] Release is tagged in the repository
- [ ] GitHub Actions package workflow successfully builds and publishes the Docker container to ghcr.io

## Final Checks

- [ ] GitHub Actions CI workflow passes on the main branch, running all quality checks
- [ ] Application can be built and run using `docker-compose up` without errors

## Undone for now

The following items are considered important for future releases but are not currently part of our Definition of Done:

- [ ] Implement test coverage measurement and maintain or improve coverage (verify with coverage tool)
- [ ] Create a script to automatically check if all environment variables in `.env.example` and `mongo/.env.default` are up to date
- [ ] Implement a zipped version of the code for download as part of the release process
- [ ] Test the application in both development and production environments.
- [ ] Cross platform compatibility
  - [ ] Linux
  - [ ] Mac OSX

This Definition of Done should be reviewed and updated periodically to reflect the evolving needs of the project. Items from the "Undone for now" section should be considered for inclusion in the main DoD as they become implemented and integrated into our development process.
