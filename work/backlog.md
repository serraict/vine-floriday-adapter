# Backlog

## Done

Repository is setup at <https://github.com/serraict/vine-floriday-adapter>.

## Doing

Goal: *get some sample Data into a Serra Vine instance*.

* Setup project structure.
  * [ ] Repository layout for source code, tests and documentation.
  * [ ] Running minimal test.
  * [x] Running cli application.
  * [x] Setup Python env

## Next

* Test data is uploaded to Serra Vine.
  * [ ] Generate test data in the form of json documents.
  * [ ] Documents are uploaded to Serra Vine's Minio server.
  * [ ] THe documents are combined into a virtual dataset in Serra Vine's data lake.

## Backlog

* Goal: connect to Floriday.
  * Setup Floriday account
  * Setup automatic tests against a staging environment (consider generating a mock server from the api)
  * Understand and implement a client for Floriday synchronization mechanism
* Goal: show open quotations for a supplier on Floriday.
  * retrieve "Supply Line" information
  * create a Serra Vine dashboard for open quotations
