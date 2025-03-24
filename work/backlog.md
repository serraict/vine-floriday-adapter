# Backlog

## Next

* Update CLI interface for sync commands to use new parameters from floriday-supplier-client v0.1.6
  * Add new options for batch_size and rate_limit_delay
  * Improve error reporting
  * Add progress feedback using new EntitySyncResult
* New clis options
  * sync last 100 items
  * sync first 100 items
  * use a different page number
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
