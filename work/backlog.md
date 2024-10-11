# Backlog

## Done

Repository is setup at <https://github.com/serraict/vine-floriday-adapter>.
Containers are pushed to <https://ghcr.io/serraict/vine-floriday-adapter>.

## Doing

* Clean up the command line interface, so that it is consistent, explorable and user friendly
  - Review current CLI structure and document areas for improvement (Done)
  - Propose a consistent naming convention for all commands
  - Suggest a reorganized command structure to improve clarity and reduce duplication
  - Draft improved help messages for all commands
  - Propose a standardized output format for all commands
  - Implement basic error handling for all commands

## Next

* Goal: Cleanup codebase and do the first deploy to a Serra Vine environment
  * (Should, L) Deploy to a Serra Vine production system.
    Serra vine runs docker containers configured in multiple docker compose files.
    The env files are saved as .env.example fils. On deploy, they are modified on the host system manually.
    - Prepare deployment documentation, preferrable just the files or a directory to copy-paste.
    - Add script to verify successful installation
    - Set up necessary credentials and access for production environment
    - Add example compose files that use the floridayvine container image,
      a mongodb instance and the appropriate crontab and .env files.
      These file should be copied to a Serra Vine environment and configured on the host system.
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
* Create a local catalog
  * Copy trade items
  * Translate vbn codes
  * Download images 

## Out of Scope
