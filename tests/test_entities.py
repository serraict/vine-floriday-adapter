from unittest.mock import patch, MagicMock
from floridayvine.floriday.entities import (
    sync_organizations,
    get_trade_items,
    sync_trade_items,
    get_direct_sales,
    sync_supply_lines,
)


@patch("floridayvine.floriday.entities.OrganizationsApi")
@patch("floridayvine.floriday.entities.get_api_client")
@patch("floridayvine.floriday.entities.sync_entities")
def test_sync_organizations(
    mock_sync_entities, mock_get_api_client, mock_organizations_api
):
    mock_api = MagicMock()
    mock_organizations_api.return_value = mock_api

    sync_organizations(start_seq_number=100, limit_result=25)

    mock_sync_entities.assert_called_once_with(
        "organizations",
        mock_api.get_organizations_by_sequence_number,
        mock_sync_entities.call_args[0][2],  # This is the persist_org function
        100,
        25,
    )

    # Test the persist_org function
    mock_org = MagicMock()
    mock_org.organization_id = "123"
    mock_org.name = "Test Org"
    mock_org.to_dict.return_value = {"id": "123", "name": "Test Org"}

    persist_org = mock_sync_entities.call_args[0][2]
    with patch("floridayvine.floriday.entities.persist") as mock_persist:
        result = persist_org(mock_org)
        mock_persist.assert_called_once_with(
            "organizations", "123", {"id": "123", "name": "Test Org"}
        )
        assert result == "Test Org"


@patch("floridayvine.floriday.entities.TradeItemsApi")
@patch("floridayvine.floriday.entities.get_api_client")
def test_get_trade_items(mock_get_api_client, mock_trade_items_api):
    mock_api = MagicMock()
    mock_trade_items_api.return_value = mock_api
    mock_items = [MagicMock(), MagicMock()]
    mock_api.get_trade_items.return_value = mock_items

    result = get_trade_items()

    assert result == mock_items
    mock_api.get_trade_items.assert_called_once()


@patch("floridayvine.floriday.entities.TradeItemsApi")
@patch("floridayvine.floriday.entities.get_api_client")
@patch("floridayvine.floriday.entities.sync_entities")
def test_sync_trade_items(
    mock_sync_entities, mock_get_api_client, mock_trade_items_api
):
    mock_api = MagicMock()
    mock_trade_items_api.return_value = mock_api

    sync_trade_items(start_seq_number=200, limit_result=30)

    mock_sync_entities.assert_called_once_with(
        "trade_items",
        mock_api.get_trade_items_by_sequence_number,
        mock_sync_entities.call_args[0][2],  # This is the persist_item function
        200,
        30,
    )

    # Test the persist_item function
    mock_item = MagicMock()
    mock_item.trade_item_id = "456"
    mock_item.trade_item_name = "Test Item"
    mock_item.to_dict.return_value = {"id": "456", "name": "Test Item"}

    persist_item = mock_sync_entities.call_args[0][2]
    with patch("floridayvine.floriday.entities.persist") as mock_persist:
        result = persist_item(mock_item)
        mock_persist.assert_called_once_with(
            "trade_items", "456", {"id": "456", "name": "Test Item"}
        )
        assert result == "Test Item"


@patch("floridayvine.floriday.entities.DirectSalesApi")
@patch("floridayvine.floriday.entities.get_api_client")
def test_get_direct_sales(mock_get_api_client, mock_direct_sales_api):
    mock_api = MagicMock()
    mock_direct_sales_api.return_value = mock_api
    mock_items = [MagicMock(), MagicMock()]
    mock_api.get_supply_lines.return_value = mock_items

    result = get_direct_sales()

    assert result == mock_items
    mock_api.get_supply_lines.assert_called_once()


@patch("floridayvine.floriday.entities.DirectSalesApi")
@patch("floridayvine.floriday.entities.get_api_client")
@patch("floridayvine.floriday.entities.sync_entities")
def test_sync_supply_lines(
    mock_sync_entities, mock_get_api_client, mock_direct_sales_api
):
    mock_api = MagicMock()
    mock_direct_sales_api.return_value = mock_api

    sync_supply_lines(start_seq_number=300, limit_result=35)

    mock_sync_entities.assert_called_once_with(
        "supply_lines",
        mock_api.get_supply_lines_by_sequence_number,
        mock_sync_entities.call_args[0][2],  # This is the persist_supply_line function
        300,
        35,
    )

    # Test the persist_supply_line function
    mock_supply_line = MagicMock()
    mock_supply_line.supply_line_id = "789"
    mock_supply_line.to_dict.return_value = {"id": "789", "name": "Test Supply Line"}

    persist_supply_line = mock_sync_entities.call_args[0][2]
    with patch("floridayvine.floriday.entities.persist") as mock_persist:
        result = persist_supply_line(mock_supply_line)
        mock_persist.assert_called_once_with(
            "supply_lines", "789", {"id": "789", "name": "Test Supply Line"}
        )
        assert result == "789"
