# Doing

## Goal

Add API version validation to the about command to warn users when their FLORIDAY_BASE_URL environment variable points to an incorrect API version.

## Analysis

The Floriday API client already has version validation built in through the `_validate_api_version()` method in the ApiFactory class. When the base URL points to a different version than what the client expects, it raises a ValueError with a helpful message.

Currently, this validation only happens when commands try to use the API client, leading to errors in various commands. We should surface this validation in the about command to help users identify and fix configuration issues early.

## Design

Add a new function `check_api_version()` to about.py that:
1. Attempts to initialize the API client (which triggers version validation)
2. Returns None if version is correct
3. Returns the error message if there's a version mismatch

Update the show_info function to:
1. Call check_api_version() before attempting to connect to Floriday
2. Display the base URL being used
3. Show a warning if API version doesn't match
4. Continue with regular connection status checks

## Steps

After each step, make sure there is a test for any changed functionality and commit our work.

1. Add check_api_version function to about.py
2. Update show_info to use check_api_version
3. Test with both correct and incorrect base URL values
4. Update tests if needed
5. Review the about command's output

## Progress

- [x] Add check_api_version function
- [x] Update show_info function
- [x] Test with incorrect base URL
- [x] Test with correct base URL
- [x] Update tests if needed
