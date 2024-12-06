# Manual Testing Plan for Supply Lines Sync Command

## Prerequisites

- Ensure you have access to the staging environment
- Verify that your local environment is properly configured with the necessary credentials

## Test Cases

1. Basic Functionality
   - Run the command: `floridayvine sync supply-lines`
   - Verify that the command executes without errors
   - Check the output for indications of successful synchronization

   Actual results:

   ```text
   No sequence number found for collection supply_lines.
   Syncing supply_lines from 0 ...
   Seq nr 41059699: Persisting 6584eda4-95ec-4d77-9511-d43348eefade ...
   Seq nr 41067630: Persisting c5ce4ec8-35c9-46c1-923f-eac3571599bb ...
   Seq nr 41067810: Persisting 24c77740-9103-40a1-9964-49b1be3e00b3 ...
   Seq nr 41067811: Persisting 5a5da8b8-e576-498c-8dbd-4914e268486e ...
   Done syncing supply_lines
   ```

2. Incremental Sync
   - Run the sync command twice in succession
   - Verify that the second run only syncs new or updated supply lines

   Actual results:
   Second run output:

   ```text
   Syncing supply_lines from 41067811 ...
   Done syncing supply_lines
   ```

3. Error Handling
   - Intentionally provide invalid credentials
   - Run the sync command and verify that it handles the error gracefully

   Command used:

   ```text
   unset FLORIDAY_API_KEY && floridayvine sync supply-lines && export $(grep -v '^#' .env | xargs)
   ```

   Actual results:

   ```text
   Error: Missing required environment variables: FLORIDAY_API_KEY
   Please set these variables before running the application.
   For more information refer to the project documentation:
   https://github.com/serraict/vine-floriday-adapter#readme
   ```

4. Performance
   - Time the execution of the sync command
   - Verify that it completes within an acceptable timeframe

   Command used:

   ```text
   time floridayvine sync supply-lines
   ```

   Actual results:

   ```text
   Syncing supply_lines from 41067811 ...
   Done syncing supply_lines
   floridayvine sync supply-lines  0.27s user 0.06s system 25% cpu 1.286 total
   ```

5. Data Integrity
   - After syncing, use the `floridayvine inventory list-direct-sales` command to view the synced data
   - Verify that the data matches what's expected from the Floriday API

   Command used:

   ```text
   floridayvine inventory list-direct-sales
   ```

   Actual results:
   The command returned a list of 4 supply line entries, each containing detailed information including supply_line_id, sequence_number, trade_item_id, price information, delivery and order periods, packing configurations, and status. The data structure was consistent across all entries and matched the expected format from the Floriday API.

## Reporting

- All test cases passed successfully
- The sync command handled errors gracefully, providing clear error messages
- Performance was satisfactory, with incremental syncs completing in about 1.3 seconds
- Data integrity was maintained throughout the sync process

Suggestions for improvements:

- Consider adding more detailed logging for troubleshooting purposes
- Implement a dry-run option for the sync command to preview changes without persisting them
