# Backlog

## Done

Repository is setup at <https://github.com/serraict/vine-floriday-adapter>.
Containers are pushed to <https://ghcr.io/serraict/vine-floriday-adapter>.

## Doing

## Next

* Goal: Cleanup codebase and do the first deploy to a Serra Vine environment
  * (Must, M) Create script to verify environment variables
    - Develop a Python script to check .env.default and .env.example files
    - Script should compare variables used in the application against those defined in .env files
    - Implement error reporting for missing or mismatched variables
    - Add script to CI/CD pipeline
    - Acceptance: Script successfully identifies all used variables and reports discrepancies
  * (Should, L) Deploy to a Serra Vine production system
    - Prepare deployment documentation
    - Set up necessary credentials and access for production environment
    - Configure CI/CD pipeline for automated deployment
    - Perform a test deployment to staging environment
    - Execute production deployment
    - Verify functionality in production environment
    - Acceptance: Application successfully deployed and running in Serra Vine production system

## Later

* Goal: show open quotations for a supplier on Floriday.
  * Sync organizations to local database
  * Sync trade items to local database
  * Sync direct sales
  * create a Serra Vine dashboard for open quotations
* Goal: learn/ understand the FLoriday api
  * Watch Floriday instruction videos and read som tutorials
  * Understand and implement a client for Floriday synchronization mechanism
    * implement it for trade items

## Out of Scope
