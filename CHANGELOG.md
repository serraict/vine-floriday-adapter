# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- New `sync supply-lines` command to synchronize supply lines data from Floriday

## [0.12.4] - 2024-10-15

### Changed

- Fixed synchronization bugs.

## [0.12.3] - 2024-10-14

### Changed

- Updated Makefile to only add and commit CHANGELOG.md during release process if it has been changed

## [0.12.2] - 2024-10-11

### Changed

- Updated crontab configuration to run `floridayvine about` every minute
- Existing cron job for `floridayvine sync status` is maintained

## [0.12] - 2024-10-11

### Changed
- Refactored CLI structure: renamed 'floriday' command to 'inventory'
- Updated 'about' command with new subcommands: 'show-info' and 'version'
- Added new subcommands to 'inventory': 'list-direct-sales', 'list-trade-items', and 'sync'

## [0.11] - 2024-10-10

### Added
- New script `scripts/verify_env_vars.py` to verify environment variables
- Deployment directory with documentation and configuration files for Serra Vine deployment
- Automatic CHANGELOG.md update process in Makefile for releases

### Removed
- Minio functionality has been completely removed from the project

### Changed
- Updated Makefile to automatically update CHANGELOG.md during the release process
