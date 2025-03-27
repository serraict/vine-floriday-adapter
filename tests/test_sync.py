from unittest.mock import patch
from typer.testing import CliRunner
from floridayvine.commands.sync import app


runner = CliRunner()


@patch("floridayvine.commands.sync.sync_organizations")
def test_organizations_command(mock_sync_organizations):
    result = runner.invoke(
        app, ["organizations", "--start-seq-number", "100", "--limit-result", "10"]
    )
    assert result.exit_code == 0
    mock_sync_organizations.assert_called_once_with(100, 10)


@patch("floridayvine.commands.sync.sync_trade_items")
def test_trade_items_command(mock_sync_trade_items):
    result = runner.invoke(
        app, ["trade-items", "--start-seq-number", "200", "--limit-result", "20"]
    )
    assert result.exit_code == 0
    mock_sync_trade_items.assert_called_once_with(200, 20)


@patch("floridayvine.commands.sync.sync_supply_lines")
def test_supply_lines_command(mock_sync_supply_lines):
    result = runner.invoke(
        app, ["supply-lines", "--start-seq-number", "300", "--limit-result", "30"]
    )
    assert result.exit_code == 0
    mock_sync_supply_lines.assert_called_once_with(300, 30)


@patch("floridayvine.commands.sync.sync_customer_offers")
def test_customer_offers_command(mock_sync_customer_offers):
    result = runner.invoke(
        app, ["customer-offers", "--start-seq-number", "400", "--limit-result", "40"]
    )
    assert result.exit_code == 0
    mock_sync_customer_offers.assert_called_once_with(400, 40)


@patch("floridayvine.commands.sync.persistence_print_sync_status")
def test_status_command(mock_print_sync_status):
    result = runner.invoke(app, ["status"])
    assert result.exit_code == 0
    mock_print_sync_status.assert_called_once()
