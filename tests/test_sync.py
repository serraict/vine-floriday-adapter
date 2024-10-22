import pytest
from unittest.mock import Mock, patch
from floridayvine.floriday.sync import sync_entities


@pytest.fixture
def mock_get_max_sequence_number():
    with patch("floridayvine.floriday.sync.get_max_sequence_number") as mock:
        mock.return_value = 0
        yield mock


@pytest.fixture
def mock_sleep():
    with patch("floridayvine.floriday.sync.time.sleep") as mock:
        yield mock


def test_sync_entities_basic(mock_get_max_sequence_number, mock_sleep):
    mock_get_by_sequence = Mock()
    mock_persist_entity = Mock()
    mock_get_by_sequence.side_effect = [
        Mock(
            maximum_sequence_number=2,
            results=[Mock(sequence_number=1), Mock(sequence_number=2)],
        ),
        Mock(maximum_sequence_number=2, results=[]),
    ]

    sync_entities("test_entity", mock_get_by_sequence, mock_persist_entity)

    assert mock_get_by_sequence.call_count == 2
    assert mock_persist_entity.call_count == 2
    assert mock_sleep.call_count == 1


def test_sync_entities_no_results(mock_get_max_sequence_number, mock_sleep):
    mock_get_by_sequence = Mock()
    mock_persist_entity = Mock()
    mock_get_by_sequence.return_value = Mock(maximum_sequence_number=0, results=[])

    sync_entities("test_entity", mock_get_by_sequence, mock_persist_entity)

    assert mock_get_by_sequence.call_count == 1
    assert mock_persist_entity.call_count == 0
    assert mock_sleep.call_count == 0


def test_sync_entities_multiple_pages(mock_get_max_sequence_number, mock_sleep):
    mock_get_by_sequence = Mock()
    mock_persist_entity = Mock()
    mock_get_by_sequence.side_effect = [
        Mock(
            maximum_sequence_number=2,
            results=[Mock(sequence_number=1), Mock(sequence_number=2)],
        ),
        Mock(
            maximum_sequence_number=4,
            results=[Mock(sequence_number=3), Mock(sequence_number=4)],
        ),
        Mock(maximum_sequence_number=4, results=[]),
    ]

    sync_entities("test_entity", mock_get_by_sequence, mock_persist_entity)

    assert mock_get_by_sequence.call_count == 3
    assert mock_persist_entity.call_count == 4
    assert mock_sleep.call_count == 2


def test_sync_entities_with_start_sequence_number(
    mock_get_max_sequence_number, mock_sleep
):
    mock_get_by_sequence = Mock()
    mock_persist_entity = Mock()
    mock_get_by_sequence.side_effect = [
        Mock(maximum_sequence_number=2, results=[Mock(sequence_number=2)]),
        Mock(maximum_sequence_number=2, results=[]),
    ]

    sync_entities(
        "test_entity", mock_get_by_sequence, mock_persist_entity, start_seq_number=1
    )

    assert mock_get_by_sequence.call_count == 2
    mock_get_by_sequence.assert_any_call(sequence_number=1, limit_result=50)
    mock_get_by_sequence.assert_any_call(sequence_number=2, limit_result=50)
    assert mock_persist_entity.call_count == 1
    assert mock_sleep.call_count == 1


@pytest.mark.parametrize("limit_result", [10, 100])
def test_sync_entities_with_custom_limit(
    mock_get_max_sequence_number, mock_sleep, limit_result
):
    mock_get_by_sequence = Mock()
    mock_persist_entity = Mock()
    mock_get_by_sequence.side_effect = [
        Mock(
            maximum_sequence_number=2,
            results=[Mock(sequence_number=1), Mock(sequence_number=2)],
        ),
        Mock(maximum_sequence_number=2, results=[]),
    ]

    sync_entities(
        "test_entity",
        mock_get_by_sequence,
        mock_persist_entity,
        limit_result=limit_result,
    )

    assert mock_get_by_sequence.call_count == 2
    mock_get_by_sequence.assert_any_call(sequence_number=0, limit_result=limit_result)
    mock_get_by_sequence.assert_any_call(sequence_number=2, limit_result=limit_result)
    assert mock_persist_entity.call_count == 2
    assert mock_sleep.call_count == 1


def test_sync_entities_error_handling(mock_get_max_sequence_number, mock_sleep):
    mock_get_by_sequence = Mock()
    mock_persist_entity = Mock(side_effect=Exception("Persistence error"))
    mock_get_by_sequence.return_value = Mock(
        maximum_sequence_number=2,
        results=[Mock(sequence_number=1), Mock(sequence_number=2)],
    )

    with pytest.raises(Exception, match="Persistence error"):
        sync_entities("test_entity", mock_get_by_sequence, mock_persist_entity)

    assert mock_get_by_sequence.call_count == 1
    assert mock_persist_entity.call_count == 1
    assert mock_sleep.call_count == 0
