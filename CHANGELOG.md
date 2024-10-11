# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Refactored CLI structure: renamed 'floriday' command to 'inventory'
- Updated 'about' command with new subcommands: 'show-info' and 'version'
- Added new subcommands to 'inventory': 'list-direct-sales', 'list-trade-items', and 'sync'
- Updated CLI documentation to reflect these changes

## [0.11] - 2024-10-10

### Added

- New script `scripts/verify_env_vars.py` to verify environment variables
- Deployment directory with documentation and configuration files for Serra Vine deployment
- Automatic CHANGELOG.md update process in Makefile for releases

### Removed

- Minio functionality has been completely removed from the project

### Changed

- Updated Makefile to automatically update CHANGELOG.md during the release process