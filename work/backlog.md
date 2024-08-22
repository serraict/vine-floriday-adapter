# Backlog

## Done

Repository is setup at <https://github.com/serraict/vine-floriday-adapter>.
Containers are pushed to <ghcr.io/serraict/vine-floriday-adapter>.

## Doing

Add the Docker image to Serra Vine.

* [ ] The image works out-of-the-box so that we can test integration with our Serra Vine instance.
  * [ ] url of minio server is configurable
  * [ ] credentials are configurable form the Serra Vine Host
  * [ ] location of source (test) data is configurable
* [ ] Write a manual on how to include it in Serra Vine

## Next

* Goal: make it deployable

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
