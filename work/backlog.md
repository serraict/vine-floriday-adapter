# Backlog

## Next

* Goal: handle api secrets according to <https://serra.fibery.io/Public/Learnings-by-State-80#Learning/passing-secrets-to-containerized-apps-101>
* Goal: show open quotations for a supplier on Floriday.
  * Create a Serra Vine dashboard for open quotations
  * Monitor rate limits for the application
* Implement consistent logging throughout the application
  * Define logging standards and best practices
  * Add appropriate log levels (INFO, WARNING, ERROR, etc.)
  * Ensure all modules use the logging system consistently
  * Add contextual information to log messages
  * Configure log output format and destination
* Enhance command-line interface
  * Review and improve the `inventory`, `sync`, and `about` commands
  * Ensure consistent behavior and error handling across all commands
* Consider implementing improvements suggested during manual testing:
  * Add more detailed logging for troubleshooting purposes
  * Implement a dry-run option for the sync command to preview changes without persisting them

## Out of Scope

* Implement user interface beyond command-line
* Support for multiple Floriday accounts simultaneously
