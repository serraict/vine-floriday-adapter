# Vine-Floriday Adapter: Software Architecture

## 1. Introduction

The Vine-Floriday Adapter is a software solution designed to retrieve trade information from the Floriday platform, allowing suppliers to analyze their quotations, orders, and catalogs locally. This document outlines the high-level architecture of the system, its main components, and the technologies used.

## 2. System Overview

The system is primarily built using Python and consists of several key components that work together to fetch, process, and store data from the Floriday platform.

## 3. Main Components

### 3.1 Data Retrieval Module

- Located in: `src/floridayvine/floriday/`
- Purpose: Interfaces with the Floriday API to fetch trade information.
- Key files:
  - `misc.py`: Contains miscellaneous functions for interacting with Floriday.

### 3.2 Data Processing Module

- Located in: `src/floridayvine/`
- Purpose: Processes and transforms the data retrieved from Floriday.
- Key files:
  - `__main__.py`: Entry point for the application, orchestrates the overall process.

### 3.3 Persistence Module

- Located in: `src/floridayvine/`
- Purpose: Handles data storage and retrieval from the local database.
- Key files:
  - `persistence.py`: Manages database operations.

## 4. Data Flow

1. The Data Retrieval Module fetches trade information from the Floriday API.
2. The Data Processing Module transforms and prepares the data for storage.
3. The Persistence Module stores the processed data in the MongoDB database.

## 5. Technologies and Frameworks

- **Programming Language**: Python
- **Database**: MongoDB
  - Chosen for its flexibility and potential integration with Dremio data lake solution.
- **API Integration**: Custom implementation for Floriday API
- **Containerization**: Docker (as evidenced by Dockerfile and docker-compose.yml)
- **Version Control**: Git

## 6. Deployment and Execution

- The application is containerized using Docker, allowing for easy deployment and scaling.
- A cron job (`floridayvine-crontab` and `floridayvine-cronjob/`) is set up for scheduled execution of the data retrieval and processing tasks.

## 7. Testing

- Located in: `tests/`
- Includes unit tests for various components of the system.
- Key test files:
  - `test_can_run_script.py`
  - `test_floriday.py`

## 8. Configuration and Environment

- Environment variables are used for configuration (`.env.example`).
- Python version is managed using `.python-version`.

## 9. Future Considerations

- The architecture is designed to be flexible, allowing for potential integration with other data lake solutions compatible with MongoDB.
- The modular structure allows for easy expansion to include additional data sources or processing capabilities.

## 10. Adding a New Entity for Synchronization

To add synchronization for a new entity type, follow these steps:

1. In `src/floridayvine/floriday/misc.py`:
   a. Create a new function for synchronizing the new entity (e.g., `sync_new_entity_type`).
   b. Define the necessary API calls using the Floriday API client.
   c. Create a persistence function for the new entity type.
   d. Call the `sync_entities` function with the appropriate parameters.

2. Example structure for adding a new entity:

   ```python
   def sync_new_entity_type(start_seq_number=None, limit_result=5):
       api = NewEntityTypeApi(_clt)
       
       def persist_new_entity(entity):
           persist("new_entity_type", entity.id, entity.to_dict())
           return entity.name

       sync_entities(
           api,
           "new_entity_type",
           api.get_new_entity_type_max_sequence,
           api.get_new_entity_type_by_sequence_number,
           persist_new_entity,
           start_seq_number,
           limit_result,
       )
   ```

   Note: The `start_seq_number` parameter now defaults to `None`. The `sync_entities` function will use the maximum sequence number from the database if `start_seq_number` is not provided.

3. In `src/floridayvine/commands/floriday.py`:
   a. Add a new command to trigger the synchronization of the new entity type.

4. Update the main application entry point (`src/floridayvine/__main__.py`) to include the new command if necessary.

5. Add appropriate unit tests in the `tests/` directory to cover the new functionality.

6. Update documentation, including this architecture document, to reflect the addition of the new entity type.

7. If the new entity requires changes to the database schema, update the `persistence.py` file and any related database migration scripts.

8. Ensure that the new entity type is added to the `SYNC_COLLECTIONS` list in `src/floridayvine/persistence.py` to enable proper initialization and synchronization status reporting.

By following these steps, you can easily extend the system to synchronize new entity types while maintaining the existing architecture and leveraging the common synchronization routine.

## 11. Conclusion

The Vine-Floriday Adapter provides a robust solution for retrieving and locally storing trade information from the Floriday platform. Its modular architecture and use of modern technologies ensure scalability and maintainability for future enhancements.
