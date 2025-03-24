# Vine-Floriday Adapter: Software Architecture

## 1. Introduction

The Vine-Floriday Adapter is a software solution designed to
retrieve trade information from the Floriday platform,
allowing suppliers to analyze their quotations, orders, and catalogs locally.
This document outlines the high-level architecture of the system,
its main components, and the technologies used.

## 2. System Overview

The system is primarily built using Python.
It is a command line script that queries the [Floriday Suppliers API],
using the [Floriday Python client],
a Python client generated from the [Floriday Suppliers API Swagger definition].

The CLI can run as a standalone script, or in a Docker container suitable for Serra Vine.
When running in Serra Vine, you can schedule the synchronization task using `cron`.
See the `floridayvine-crontab` for an example crontab file.

## 3. Main Components

### 3.1. CLI

The command line application is written in [Typer](https://typer.tiangolo.com/).
Its entrypoint is located in `src/floridayvine/__main__.py`,
and all sub commands are placed in `src/floridayvine/commands`.

### 3.2. Floriday

All components related to consuming the API are located in `src/floridayvine/floriday`.
Entities in Floriday can be synchronized with the local datastore.
The synchronization code uses the `sync_entities` function from the `floriday-supplier-client` package.
A thin wrapper in `src/floridayvine/floriday/sync.py` maintains backward compatibility with the original API.

### 3.3. Persistence

Data structures are persisted locally in a MongoDB.
We do not perform any local processing and persist the entities as received from Floriday.

## 4. Program Flow

- Check synchronization state of a local collection.
- From the local state, initiate a synchronization with the Floriday API.
- Repeat for any collection.

## 5. Technologies and Frameworks

The application is developed in Python 3.12, with [Typer](https://typer.tiangolo.com/) and [PyMongo](https://pymongo.readthedocs.io/) as the most important dependencies.
A MongoDB instance is needed for local storage.

## 6. Deployment and Execution

We deploy the app as Docker container image `vine-floriday-adapter` to <https://ghcr.io>.

```bash
docker pull ghcr.io/serraict/vine-floriday-adapter:latest
```

## 7. Testing

Tests are written using [PyTest](https://docs.pytest.org/).
There are unit tests that can be run standalone,
and integration tests that require access to a Floriday staging environment and a MongoDB instance.

```bash
make test
make test-integration
```

## 8. Configuration and Environment

- Environment variables are used for configuration (`.env.example`).
- Python version is managed using `.python-version`.

## 9. Error Handling and Resilience

Request and database exceptions are caught and handled with context-specific error messages.

## 10. Logging and Monitoring

Log message are written to stdout.
The file `/var/cron.log` is `tail`ed by the docker container,
see `/floridayvine-crontab` for an example on how to forward your cron jobs's output to this log file.

## 11. Security Considerations

Credentials are not persisted on disk.
Credentials are managed through environment variables

## 12. Database Management

Synchronized collections are created automatically during database initialization.
No explicit schema validation is enforced, maintaining flexibility with API response.

## 13. Future Considerations

As the synchronization workflow is central to the interaction with the Floriday API,
we should consider moving it into the client package.

Describe how to securely handle secrets without writing them to disk unencrypted.

## 14. Adding a New Entity for Synchronization

To add synchronization for a new entity type, follow these steps:

1. In `src/floridayvine/floriday/entities.py`:
   a. Create a new function for synchronizing the new entity (e.g., `sync_new_entity_type`).
   b. Define the necessary API calls using the Floriday API client.
   c. Create a persistence function for the new entity type.
   d. Call the `sync_entities` function with the appropriate parameters.

2. Example structure for adding a new entity:

   ```python
   def sync_new_entity_type(start_seq_number=None, limit_result=50):
       api = NewEntityTypeApi(get_api_client())
       
       def persist_new_entity(entity):
           persist("new_entity_type", entity.id, entity.to_dict())
           return entity.name

       return sync_entities(
           "new_entity_type",
           api.get_new_entity_type_by_sequence_number,
           persist_new_entity,
           start_seq_number,
           limit_result,
       )
   ```

   Note: 
   - The `start_seq_number` parameter defaults to `None`. The `sync_entities` function will use the maximum sequence number from the database if `start_seq_number` is not provided.
   - The function returns the result of the sync operation, which includes statistics about the synchronization process.
   - Additional parameters like `rate_limit_delay` can be added to control the synchronization behavior.

3. In `src/floridayvine/commands/floriday.py`:
   a. Add a new command to trigger the synchronization of the new entity type.

4. Update the main application entry point (`src/floridayvine/__main__.py`) to include the new command if necessary.

5. Add appropriate unit tests in the `tests/` directory to cover the new functionality.

6. Update documentation, including this architecture document, to reflect the addition of the new entity type.

7. If the new entity requires changes to the database schema, update the `persistence.py` file and any related database migration scripts.

8. Ensure that the new entity type is added to the `SYNC_COLLECTIONS` list in `src/floridayvine/persistence.py` to enable proper initialization and synchronization status reporting.

By following these steps, you can easily extend the system to synchronize new entity types while maintaining the existing architecture and leveraging the common synchronization routine.

[Floriday Suppliers API]: https://developer.floriday.io/docs/release-notes-suppliers-api
[Floriday Python client]: https://github.com/serraict/vine-floriday-python-supplier-api-client
[Floriday Suppliers API Swagger definition]: https://api.staging.floriday.io/suppliers-api-2024v2/swagger/index.html
