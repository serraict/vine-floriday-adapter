# Backlog

## Doing

Improve test coverage:

* Target: Achieve and maintain 80% overall coverage for src/floridayvine (currently 65%)
* Focus areas (in order of priority):
  1. `floriday/misc.py` (previously 51%)
     * ✅ Create new test file: test_misc.py in the tests directory
     * ✅ Write tests for the following functions:
       - handle_request_exception
       - get_access_token
       - get_api_client
     * Write tests for the remaining functions:
       - get_organizations
       - sync_entities (generic function)
       - sync_organizations
       - get_trade_items
       - get_direct_sales
       - sync_trade_items
       - sync_supply_lines
     * Implement naming and modularization improvements:
       - Rename misc.py to floriday_api.py or floriday_sync.py
       - Group related functions together
       - Consider creating separate modules for authentication, API interactions, and sync operations
     * Code improvements:
       - Add type hints
       - Use environment variables more consistently
       - Implement better error handling and logging
  2. `persistence.py` (currently 90%)
     * Add tests for remaining uncovered lines (38-43, 72-73)
* Add integration tests for key workflows

## Next

* Goal: show open quotations for a supplier on Floriday.
  * Create a Serra Vine dashboard for open quotations
  * Monitor rate limits for the application
* Implement consistent logging throughout the application
  * Define logging standards and best practices
  * Add appropriate log levels (INFO, WARNING, ERROR, etc.)
  * Ensure all modules use the logging system consistently
  * Add contextual information to log messages
  * Configure log output format and destination
* Consider implementing improvements suggested during manual testing:
  * Add more detailed logging for troubleshooting purposes
  * Implement a dry-run option for the sync command to preview changes without persisting them

## Out of Scope
