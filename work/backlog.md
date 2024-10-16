# Backlog

## Doing

## Next

* Implement consistent logging throughout the application
  * Define logging standards and best practices
  * Add appropriate log levels (INFO, WARNING, ERROR, etc.)
  * Ensure all modules use the logging system consistently
  * Add contextual information to log messages
  * Configure log output format and destination

## Later

* Goal: show open quotations for a supplier on Floriday.
  * Create a Serra Vine dashboard for open quotations

* Consider implementing improvements suggested during manual testing:
  * Add more detailed logging for troubleshooting purposes
  * Implement a dry-run option for the sync command to preview changes without persisting them

## Out of Scope

## Done

* Implemented sync command for supply lines
  * Added a new command in the sync.py file for syncing supply lines
  * Implemented the following steps in the sync command:
    1. Get the highest generated sequence number
    2. Sync supply lines and batch sequence number using the Floriday API
    3. Process and store the returned supply lines in the local database
  * Ensured prerequisites are met:
    - Checked if organizations are present in the system
    - Verified tradeitem and batch information is available
  * Added error handling and logging
  * Updated CLI documentation to include the new command
  * Tested the new command with the staging environment
  * Updated persistence.py to handle storage and retrieval of supply lines
* Performed manual testing of the supply lines sync command
* Improved unit tests for the sync_supply_lines function, covering various scenarios and edge cases
