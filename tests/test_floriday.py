import subprocess
import pytest

pytestmark = pytest.mark.integration


@pytest.fixture(scope="session", autouse=True)
def check_floriday_connection():
    result = subprocess.run(["floridayvine", "about"], capture_output=True, text=True)
    assert result.returncode == 0, "Failed to run 'floridayvine about' command"

    output = result.stdout
    assert (
        "Floriday Connection Status:" in output
    ), "Floriday connection status not found in output"
    assert (
        "Successfully connected to Floriday." in output
    ), "Failed to connect to Floriday"

    print("Connection to Floriday verified.")


@pytest.fixture(scope="session", autouse=True)
def check_database_connection():
    result = subprocess.run(["floridayvine", "about"], capture_output=True, text=True)
    assert result.returncode == 0, "Failed to run 'floridayvine about' command"

    output = result.stdout
    assert (
        "Database Connection Status:" in output
    ), "Database connection status not found in output"
    assert (
        "Successfully connected to the database at" in output
    ), "Failed to connect to the database"
    assert (
        "Database and indices are properly set up" in output
    ), "Database or indices are not properly set up"

    print("Connection to database verified and properly set up.")


def test_can_list_direct_sales():
    cp = subprocess.run(["floridayvine", "inventory", "list-direct-sales"])
    assert cp.returncode == 0


def test_can_list_trade_items():
    cp = subprocess.run(["floridayvine", "inventory", "list-trade-items"])
    assert cp.returncode == 0


def test_can_sync_organizations():
    cp = subprocess.run(
        ["floridayvine", "sync", "organizations", "--limit-result", "5"]
    )
    assert cp.returncode == 0


def test_can_sync_trade_items():
    cp = subprocess.run(
        [
            "floridayvine",
            "sync",
            "trade-items",
            "--start-seq-number",
            "0",
            "--limit-result",
            "5",
        ]
    )
    assert cp.returncode == 0


def test_db_initialize_command():
    cp = subprocess.run(["floridayvine", "db", "init"])
    assert cp.returncode == 0, "Failed to initialize database"

    # Check if the database is properly set up after initialization
    result = subprocess.run(["floridayvine", "about"], capture_output=True, text=True)
    assert (
        "Database and indices are properly set up" in result.stdout
    ), "Database not properly set up after initialization"
