# Backlog

## Doing

Improve test coverage:

* Target: Achieve and maintain 80% overall coverage for src/floridayvine (currently 65%)
* Focus areas (in order of priority):
  1. `floriday` module (previously `misc.py`)
     * ✅ Implement naming and modularization improvements:
       - ✅ Rename misc.py to separate modules (auth.py, api_client.py, sync.py, entities.py)
       - ✅ Group related functions together
     * Write tests for the following functions in their respective modules:
       - get_organizations
       - sync_entities (generic function)
       - sync_organizations
       - get_trade_items
       - get_direct_sales
       - sync_trade_items
     * ✅ Write tests for sync_supply_lines (test_sync_supply_lines.py)
     * Code improvements:
       - Add type hints
       - Use environment variables more consistently
       - Implement better error handling and logging
  2. `persistence.py` (currently 90%)
     * Add tests for remaining uncovered lines (38-43, 72-73)
* Add integration tests for key workflows

## Next

* Implement consistent logging throughout the application
  * Define logging standards and best practices
  * Add appropriate log levels (INFO, WARNING, ERROR, etc.)
  * Ensure all modules use the logging system consistently
  * Add contextual information to log messages
  * Configure log output format and destination
* Goal: show open quotations for a supplier on Floriday.
  * Create a Serra Vine dashboard for open quotations
  * Monitor rate limits for the application
* Enhance command-line interface
  * Review and improve the `inventory`, `sync`, and `about` commands
  * Ensure consistent behavior and error handling across all commands
* Consider implementing improvements suggested during manual testing:
  * Add more detailed logging for troubleshooting purposes
  * Implement a dry-run option for the sync command to preview changes without persisting them
* Update documentation
  * Review and update README.md
  * Update CLI documentation to reflect new commands and structure
  * Document the new module structure in software_architecture.md

## Out of Scope

* Implement user interface beyond command-line
* Support for multiple Floriday accounts simultaneously
