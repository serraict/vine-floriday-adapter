"""
Synchronization module for Floriday entities.

This module provides a wrapper around the floriday-supplier-client sync module
to maintain backward compatibility with the original API.
"""

from typing import Callable, Any, Optional, Dict

from floriday_supplier_client.sync import sync_entities as client_sync_entities
from ..persistence import get_max_sequence_number


def sync_entities(
    entity_type: str,
    get_by_sequence: Callable,
    persist_entity: Callable,
    start_seq_number: Optional[int] = None,
    limit_result: int = 50,
    rate_limit_delay: float = 0.5,
) -> Dict[str, Any]:
    """
    Synchronize entities from Floriday to local storage.

    This is a wrapper around the floriday_supplier_client.sync.sync_entities function
    that maintains backward compatibility with the original API.

    Args:
        entity_type: Type of entity being synchronized (e.g., 'trade_items')
        get_by_sequence: Function to fetch entities by sequence number
        persist_entity: Function to persist an entity
        start_seq_number: Optional starting sequence number
        limit_result: Number of entities to fetch per batch
        rate_limit_delay: Delay between API calls in seconds

    Returns:
        Dictionary with sync statistics
    """
    print(
        f"Syncing {entity_type} from {start_seq_number or get_max_sequence_number(entity_type)} ..."
    )

    # If start_seq_number is not provided, get it from the database
    if start_seq_number is None:
        start_seq_number = get_max_sequence_number(entity_type)

    result = client_sync_entities(
        entity_type=entity_type,
        fetch_entities_callback=get_by_sequence,
        persist_entity_callback=persist_entity,
        start_seq_number=start_seq_number,
        batch_size=limit_result,
        rate_limit_delay=rate_limit_delay,
    )

    print(f"Done syncing {entity_type}")

    # Convert EntitySyncResult to the original dictionary format for backward compatibility
    return {
        "entity_type": entity_type,
        "start_sequence_number": result.start_sequence_number,
        "end_sequence_number": result.end_sequence_number,
        "entities_processed": result.entities_processed,
        "success": result.success,
    }
