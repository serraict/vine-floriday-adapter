# Deployment Instructions for vine-floriday-adapter

This document provides instructions for deploying the vine-floriday-adapter to a Serra Vine production system.

## Prerequisites

- Access to the Serra Vine production environment
- Necessary credentials for Floriday API and MongoDB

## Deployment Steps

1. Create a new directory named 'floridayvine' in the Serra Vine environment and copy the following files into it:

   - `floridayvine-docker-compose.yml`
   - `.env.example` (rename to `.env`)
   - `floridayvine-crontab`

2. Copy `verify_installation.sh` to the parent directory of 'floridayvine'.

3. Rename `.env.example` to `.env` and update the environment variables with the appropriate values for the production environment.

4. Include the `floridayvine-docker-compose.yml` file in the main Serra Vine docker compose file. This can typically be done by adding an `include` statement in the main docker-compose.yml file:

   ```yaml
   include:
     - floridayvine/floridayvine-docker-compose.yml
   ```

5. Ensure that the Serra Vine docker-compose file is configured to use the floridayvine services as needed.

6. Set up necessary credentials and access:
   - Obtain Floriday API credentials and update the .env file accordingly
   - Set up MongoDB access and update the connection string in the .env file

7. The crontab file is now mounted as a volume in the Docker Compose file. Ensure that the `floridayvine-crontab` file is in the correct location (./floridayvine/floridayvine-crontab) and contains the appropriate scheduled tasks.

8. Perform a test deployment to staging environment (if available):
   - Deploy the services to the staging environment using the docker-compose command
   - Run the verification script: `./verify_installation.sh`
   - Test the functionality in the staging environment

9. Execute production deployment:
   - Once staging deployment is successful, deploy to the production environment
   - Run the docker-compose command to start the services:

     ```
     docker-compose up -d
     ```

10. Verify the installation by running the verification script:

    ```
    ./verify_installation.sh
    ```

11. Verify functionality in production environment:
    - Ensure all services are running correctly
    - Test the main features of the floridayvine adapter
    - Monitor logs for any errors or issues
    - Verify that scheduled tasks are running as expected (check Docker logs for the floridayvine container)

## Verifying the Deployment

After deployment, ensure that:

- The floridayvine container is running
- The MongoDB instance is accessible
- The Floriday API connection is successful (verified by the installation script)
- Scheduled tasks are running according to the crontab configuration

## Troubleshooting

If you encounter any issues during deployment, please check the following:

- Docker logs for the floridayvine container
- MongoDB connection string in the .env file
- Floriday API credentials in the .env file
- Docker logs for scheduled task execution

For further assistance, please contact the development team.

## Updating the Application

To update the application to a new version:

1. Update the image version in the `floridayvine-docker-compose.yml` file.

2. Restart the services:
   ```
   docker-compose up -d
   ```

3. Run the verification script to ensure everything is working correctly:
   ```
   ./verify_installation.sh
   ```

4. Review and update the `floridayvine-crontab` file if necessary.
