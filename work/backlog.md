# Backlog

## Done

Repository is setup at <https://github.com/serraict/vine-floriday-adapter>.
Containers are pushed to <ghcr.io/serraict/vine-floriday-adapter>.

## Doing

## Next

* Goal: have a decent developer experience
  * use the api to implement a generic sync implementation
    * sync organizations from seq nr = 0
    * sync from a certain number N
      * sync from 0 up until N
      * sync from N
    * Data can be stored locally
    * Mongo DB as part of this compose file makes more sense. Use serra-vine network.
  * learn about typer wrt exceptions and exit codes
  * document versioning strategy: what will we do when the api updates
  * organize typer commands into submodules
  * Experiment: generate mock server from api definition for local development

## Later

* Goal: show open quotations for a supplier on Floriday.
  * Sync organizations to local database
    * For now: create a csv that we place in Mino and read with dremio
    * Sync from base
    * Sync from a specific sequence number
  * Sync trade items to local database
  * Sync batches (optional)
  * Sync direct sales
  * create a Serra Vine dashboard for open quotations
* Goal: learn/ understand the FLoriday api
  * Watch Floriday instruction videos and read som tutorials
  * Understand and implement a client for Floriday synchronization mechanism
    * implement it for trade items

## Out of Scope
