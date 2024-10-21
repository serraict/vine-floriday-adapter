import time
from ..persistence import get_max_sequence_number


def sync_entities(
    entity_type, get_by_sequence, persist_entity, start_seq_number=None, limit_result=50
):
    if start_seq_number is None:
        start_seq_number = get_max_sequence_number(entity_type)

    next_sequence_start_number = start_seq_number

    print(f"Syncing {entity_type} from {next_sequence_start_number} ...")

    while True:
        sync_result = get_by_sequence(
            sequence_number=next_sequence_start_number, limit_result=limit_result
        )

        if next_sequence_start_number >= sync_result.maximum_sequence_number:
            break

        for entity in sync_result.results:
            print(
                f"Seq nr {entity.sequence_number}: Persisting {persist_entity(entity)} ..."
            )

        next_sequence_start_number = sync_result.maximum_sequence_number

        time.sleep(0.5)

    print(f"Done syncing {entity_type}")
