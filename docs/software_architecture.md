# Vine-Floriday Adapter: Software Architecture

[... Previous sections remain unchanged ...]

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

[... Conclusion remains unchanged ...]
