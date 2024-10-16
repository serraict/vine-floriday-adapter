# Backlog

## Doing

Set up Codecov:

- [x] Create a Codecov account and link it to the GitHub repository
- [x] Add CODECOV_TOKEN to GitHub repository secrets
- [ ] Verify Codecov integration by pushing a change and checking the coverage report

## Next

Improve test coverage:

- Target: Achieve 70-80% overall coverage
- Focus areas:
  1. `__main__.py` (currently 0%)
  2. `config.py` (currently 0%)
  3. `persistence.py` (currently 19%)
  4. `floriday/misc.py` (currently 51%)
- Add unit tests for uncovered functions and methods
- Add integration tests for key workflows

## Later

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
