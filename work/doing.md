# Doing

## Goal

Update to the new sync module in floriday-supplier-client v0.1.6.

## Analysis

The current sync implementation in `src/floridayvine/floriday/sync.py` is basic and needs to be updated to use the new sync module from floriday-supplier-client v0.1.6. Key differences:

1. Current implementation:
   - Basic function-based approach
   - Limited error handling
   - Fixed rate limiting (0.5s)
   - Print statements for logging
   - No type hints

2. New sync module features:
   - More Pythonic with type hints
   - Proper error handling
   - Configurable rate limiting
   - Optional in-memory tracking
   - Logging instead of print statements
   - Class-based approach with EntitySynchronizer
   - Context manager support

3. Impact areas:
   - src/floridayvine/floriday/sync.py
   - src/floridayvine/floriday/entities.py (uses sync.py)
   - src/floridayvine/commands/sync.py (CLI interface)
   - tests that use sync functionality

## Design

1. Remove local sync.py implementation
   - The functionality is now provided by floriday-supplier-client
   - Create a thin wrapper around the new sync module to maintain backward compatibility

2. Update tests
   - Remove test_sync.py as it tests implementation details of the client library
   - Existing tests for entities.py already mock sync_entities, so they don't need to be updated

3. Update CLI interface
   - Add new options for batch_size and rate_limit_delay
   - Improve error reporting
   - Add progress feedback using new EntitySyncResult

## Steps

1. Dependencies
   - [x] Update floriday-supplier-client to v0.1.6
   - [x] Update requirements-dev.txt if needed

2. Code Changes
   - [ ] Remove src/floridayvine/floriday/sync.py
   - [ ] Update imports in entities.py
   - [ ] Refactor sync functions in entities.py
   - [ ] Update CLI interface in commands/sync.py
   - [ ] Update tests to work with new sync module

3. Documentation
   - [ ] Update CHANGELOG.md
   - [ ] Update software_architecture.md if needed
   - [ ] Update cli_documentation.md with new options

4. Testing
   - [ ] Run unit tests (make test)
   - [ ] Run integration tests (make test-integration)
   - [ ] Run quality checks (make quality)

5. Final Checks
   - [ ] Verify no sensitive information is exposed
   - [ ] Check cross-platform compatibility
   - [ ] Test Docker build
   - [ ] Update version number

## Progress

Ready to start implementation. Will need to:
1. First update dependencies
2. Then make code changes incrementally, testing each change
3. Finally update documentation and perform final checks
