import subprocess
import pytest

pytestmark = pytest.mark.integration


@pytest.fixture(scope="session", autouse=True)
def check_connections():
    result = subprocess.run(["floridayvine", "about"], capture_output=True, text=True)
    assert result.returncode == 0, "Failed to run 'floridayvine about' command"

    output = result.stdout
    assert (
        "Successfully connected to Floriday." in output
    ), "Failed to connect to Floriday"
    assert (
        "Successfully connected to the database" in output
    ), "Failed to connect to the database"
    assert (
        "Database and indices are properly set up" in output
    ), "Database or indices are not properly set up"

    print("Connections to Floriday and database verified.")


def test_can_list_direct_sales():
    assert (
        subprocess.run(["floridayvine", "inventory", "list-direct-sales"]).returncode
        == 0
    )


def test_can_list_trade_items():
    assert (
        subprocess.run(["floridayvine", "inventory", "list-trade-items"]).returncode
        == 0
    )


def test_can_sync_organizations():
    assert (
        subprocess.run(
            ["floridayvine", "sync", "organizations", "--limit-result", "5"]
        ).returncode
        == 0
    )


def test_can_print_sync_status():
    assert subprocess.run(["floridayvine", "sync", "status"]).returncode == 0


def test_can_sync_trade_items():
    assert (
        subprocess.run(
            [
                "floridayvine",
                "sync",
                "trade-items",
                "--start-seq-number",
                "0",
                "--limit-result",
                "5",
            ]
        ).returncode
        == 0
    )


def test_db_initialize_command():
    assert (
        subprocess.run(["floridayvine", "db", "init"]).returncode == 0
    ), "Failed to initialize database"
    result = subprocess.run(["floridayvine", "about"], capture_output=True, text=True)
    assert (
        "Database and indices are properly set up" in result.stdout
    ), "Database not properly set up after initialization"
