import pytest
from unittest.mock import patch, MagicMock, ANY
from floridayvine.floriday.entities import sync_supply_lines


@pytest.fixture
def mock_dependencies():
    with (
        patch("floridayvine.floriday.entities.DirectSalesApi") as mock_direct_sales_api,
        patch("floridayvine.floriday.entities.get_api_client") as mock_get_api_client,
        patch("floridayvine.floriday.entities.persist") as mock_persist,
        patch("floridayvine.floriday.entities.sync_entities") as mock_sync_entities,
    ):
        mock_api_client = MagicMock()
        mock_get_api_client.return_value = mock_api_client
        mock_direct_sales_api.return_value = mock_api_client

        yield {
            "sync_entities": mock_sync_entities,
            "persist": mock_persist,
            "api_client": mock_api_client,
        }


def test_sync_supply_lines_basic(mock_dependencies):
    sync_supply_lines()

    mock_dependencies["sync_entities"].assert_called_once_with(
        "supply_lines",
        mock_dependencies["api_client"].get_supply_lines_by_sequence_number,
        ANY,
        None,
        50,
    )


def test_sync_supply_lines_with_params(mock_dependencies):
    sync_supply_lines(start_seq_number=10, limit_result=100)

    mock_dependencies["sync_entities"].assert_called_once_with(
        "supply_lines",
        mock_dependencies["api_client"].get_supply_lines_by_sequence_number,
        ANY,
        10,
        100,
    )


def test_sync_supply_lines_persist_function(mock_dependencies):
    mock_supply_line = MagicMock(supply_line_id="test_id")
    mock_supply_line.to_dict.return_value = {"id": "test_id"}

    sync_supply_lines()

    persist_function = mock_dependencies["sync_entities"].call_args[0][2]
    result = persist_function(mock_supply_line)

    assert result == "test_id"
    mock_dependencies["persist"].assert_called_once_with(
        "supply_lines", "test_id", {"id": "test_id"}
    )


def test_sync_supply_lines_api_error(mock_dependencies):
    mock_dependencies["sync_entities"].side_effect = Exception("API Error")

    with pytest.raises(Exception, match="API Error"):
        sync_supply_lines()

    mock_dependencies["persist"].assert_not_called()
