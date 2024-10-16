import pytest
from unittest.mock import patch, MagicMock, call
from floridayvine.floriday.misc import sync_supply_lines


@pytest.fixture
def mock_dependencies():
    with (
        patch("floridayvine.floriday.misc.DirectSalesApi") as mock_direct_sales_api,
        patch("floridayvine.floriday.misc.get_api_client") as mock_get_api_client,
        patch("floridayvine.floriday.misc.persist") as mock_persist,
        patch(
            "floridayvine.floriday.misc.get_max_sequence_number"
        ) as mock_get_max_sequence_number,
    ):

        mock_get_max_sequence_number.return_value = 0
        mock_api_client = MagicMock()
        mock_get_api_client.return_value = mock_api_client
        mock_direct_sales_api.return_value = mock_api_client

        yield {
            "get_max_sequence_number": mock_get_max_sequence_number,
            "persist": mock_persist,
            "api_client": mock_api_client,
        }


def test_sync_supply_lines_basic(mock_dependencies):
    mock_supply_line = MagicMock(supply_line_id="test_id", sequence_number=1)
    mock_supply_line.to_dict.return_value = {"id": "test_id"}
    mock_dependencies["api_client"].get_supply_lines_by_sequence_number.side_effect = [
        MagicMock(results=[mock_supply_line], maximum_sequence_number=1),
        MagicMock(results=[], maximum_sequence_number=1),
    ]

    sync_supply_lines()

    mock_dependencies["get_max_sequence_number"].assert_called_once_with("supply_lines")
    mock_dependencies[
        "api_client"
    ].get_supply_lines_by_sequence_number.assert_has_calls(
        [
            call(sequence_number=0, limit_result=50),
            call(sequence_number=1, limit_result=50),
        ]
    )
    mock_dependencies["persist"].assert_called_once_with(
        "supply_lines", "test_id", {"id": "test_id"}
    )


def test_sync_supply_lines_multiple_pages_limit_one(mock_dependencies):
    mock_supply_line1 = MagicMock(supply_line_id="test_id1", sequence_number=1)
    mock_supply_line1.to_dict.return_value = {"id": "test_id1"}
    mock_supply_line2 = MagicMock(supply_line_id="test_id2", sequence_number=2)
    mock_supply_line2.to_dict.return_value = {"id": "test_id2"}

    mock_dependencies["api_client"].get_supply_lines_by_sequence_number.side_effect = [
        MagicMock(results=[mock_supply_line1], maximum_sequence_number=1),
        MagicMock(results=[mock_supply_line2], maximum_sequence_number=2),
        MagicMock(results=[], maximum_sequence_number=2),
    ]

    sync_supply_lines(limit_result=1)

    assert (
        mock_dependencies["api_client"].get_supply_lines_by_sequence_number.call_count
        == 3
    )
    mock_dependencies[
        "api_client"
    ].get_supply_lines_by_sequence_number.assert_has_calls(
        [
            call(sequence_number=0, limit_result=1),
            call(sequence_number=1, limit_result=1),
            call(sequence_number=2, limit_result=1),
        ]
    )
    mock_dependencies["persist"].assert_has_calls(
        [
            call("supply_lines", "test_id1", {"id": "test_id1"}),
            call("supply_lines", "test_id2", {"id": "test_id2"}),
        ]
    )


def test_sync_supply_lines_multiple_pages_limit_three(mock_dependencies):
    mock_supply_lines = [
        MagicMock(supply_line_id=f"test_id{i}", sequence_number=i) for i in range(1, 6)
    ]
    for mock_supply_line in mock_supply_lines:
        mock_supply_line.to_dict.return_value = {"id": mock_supply_line.supply_line_id}

    mock_dependencies["api_client"].get_supply_lines_by_sequence_number.side_effect = [
        MagicMock(results=mock_supply_lines[:3], maximum_sequence_number=3),
        MagicMock(results=mock_supply_lines[3:], maximum_sequence_number=5),
        MagicMock(results=[], maximum_sequence_number=5),
    ]

    sync_supply_lines(limit_result=3)

    assert (
        mock_dependencies["api_client"].get_supply_lines_by_sequence_number.call_count
        == 3
    )
    mock_dependencies[
        "api_client"
    ].get_supply_lines_by_sequence_number.assert_has_calls(
        [
            call(sequence_number=0, limit_result=3),
            call(sequence_number=3, limit_result=3),
            call(sequence_number=5, limit_result=3),
        ]
    )
    mock_dependencies["persist"].assert_has_calls(
        [
            call("supply_lines", f"test_id{i}", {"id": f"test_id{i}"})
            for i in range(1, 6)
        ]
    )


def test_sync_supply_lines_no_new_data(mock_dependencies):
    mock_dependencies["get_max_sequence_number"].return_value = 10
    mock_dependencies["api_client"].get_supply_lines_by_sequence_number.return_value = (
        MagicMock(results=[], maximum_sequence_number=10)
    )

    sync_supply_lines()

    mock_dependencies[
        "api_client"
    ].get_supply_lines_by_sequence_number.assert_called_once_with(
        sequence_number=10, limit_result=50
    )
    mock_dependencies["persist"].assert_not_called()


def test_sync_supply_lines_api_error(mock_dependencies):
    mock_dependencies["api_client"].get_supply_lines_by_sequence_number.side_effect = (
        Exception("API Error")
    )

    with pytest.raises(Exception, match="API Error"):
        sync_supply_lines()

    mock_dependencies["persist"].assert_not_called()
