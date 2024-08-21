# Backlog

## Done

Repository is setup at <https://github.com/serraict/vine-floriday-adapter>.

## Doing

* Create a Docker image
  * As part of build script
  * Publish (to docker hub or similar)

## Next

* Goal: make it deployable
  * Add the Docker image to Serra Vine
  * Have a cronjob of some kind that periodically runs the upload
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
