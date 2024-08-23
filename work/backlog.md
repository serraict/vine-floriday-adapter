# Backlog

## Done

Repository is setup at <https://github.com/serraict/vine-floriday-adapter>.
Containers are pushed to <ghcr.io/serraict/vine-floriday-adapter>.

## Doing

Add the Docker image to Serra Vine.

* [x] The image works out-of-the-box so that we can test integration with our Serra Vine instance.
  * [x] url of minio server is configurable
  * [x] credentials are configurable form the Serra Vine Host
  * [x] location of source (test) data is configurable
  * [x] target location is configurable
* [x] Write a manual on how to include it in Serra Vine
* [x] Have a cronjob of some kind that periodically runs the upload

## Next

* Goal: make it deployable
  * Refactor configuration variables and command line parameters

## Later

* Goal: connect to Floriday.
  * Setup Floriday account
  * Setup automatic tests against a staging environment (consider generating a mock server from the api)
  * Understand and implement a client for Floriday synchronization mechanism
* Goal: show open quotations for a supplier on Floriday.
  * retrieve "Supply Line" information
  * create a Serra Vine dashboard for open quotations

## Out of Scope
