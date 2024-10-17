# Backlog

## Doing

Improve test coverage:

* Target: Achieve and maintain 80% overall coverage for src/floridayvine (currently 65%)
* see if the new test are robust.
* Focus areas (in order of priority):
  1. `floriday/misc.py` (currently 51%)
  2. `persistence.py` (currently 90%)
     - Add tests for remaining uncovered lines (38-43, 72-73)
* Add unit tests for uncovered functions and methods
* Add integration tests for key workflows

## Next

* Goal: show open quotations for a supplier on Floriday.
  * Create a Serra Vine dashboard for open quotations
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
