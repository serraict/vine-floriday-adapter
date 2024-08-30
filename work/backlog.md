# Backlog

## Done

Repository is setup at <https://github.com/serraict/vine-floriday-adapter>.
Containers are pushed to <ghcr.io/serraict/vine-floriday-adapter>.

## Doing

* Retrieve trade-item information.

## Next

* Goal: connect to Floriday.
  * Understand and implement a client for Floriday synchronization mechanism
    * implement it for trade items
  * Experiment: generate mock server from api definition for local development

## Later

* Goal: have a decent developer experience
  * generate an api
  * use the api to implement a generic sync implementation
  * learn about typer wrt exceptions and exit codes
  * document versioning strategy: what will we do when the api updates
  * organize typer commands into submodules
* Goal: show open quotations for a supplier on Floriday.
  * retrieve "Supply Line" information
  * create a Serra Vine dashboard for open quotations

## Out of Scope
