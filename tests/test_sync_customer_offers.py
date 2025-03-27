import subprocess
import pytest
from pymongo import MongoClient
import os
from floridayvine.persistence import mongodb_connection_string, DATABASE

pytestmark = pytest.mark.integration


@pytest.fixture(scope="module")
def mongodb_client():
    """Create a MongoDB client for testing."""
    client = MongoClient(mongodb_connection_string)
    yield client
    client.close()


@pytest.fixture(scope="module")
def db(mongodb_client):
    """Get the database for testing."""
    return mongodb_client[DATABASE]


def test_sync_customer_offers_command():
    """Test that the customer-offers sync command works correctly."""
    # Run the sync command with a small limit
    result = subprocess.run(
        ["floridayvine", "sync", "customer-offers", "--limit-result", "3"],
        capture_output=True,
        text=True,
    )

    # Check that the command executed successfully
    assert result.returncode == 0, f"Command failed with output: {result.stderr}"

    # Check that the output contains expected text
    assert "Syncing customer_offers" in result.stdout
    assert "Done syncing customer_offers" in result.stdout


def test_incremental_sync(db):
    """Test that incremental sync works correctly."""
    # Get the current max sequence number
    collection = db["customer_offers"]
    max_seq = max([doc.get("sequence_number", 0) for doc in collection.find()] or [0])

    # Run the sync command starting from the max sequence number
    result = subprocess.run(
        [
            "floridayvine",
            "sync",
            "customer-offers",
            "--start-seq-number",
            str(max_seq),
            "--limit-result",
            "2",
        ],
        capture_output=True,
        text=True,
    )

    # Check that the command executed successfully
    assert result.returncode == 0, f"Command failed with output: {result.stderr}"

    # Check that the output contains expected text
    assert f"Syncing customer_offers from {max_seq}" in result.stdout
    assert "Done syncing customer_offers" in result.stdout


def test_error_handling():
    """Test that the command handles errors gracefully."""
    # Save the current API key
    api_key = os.environ.get("FLORIDAY_API_KEY", "")

    try:
        # Unset the API key
        os.environ["FLORIDAY_API_KEY"] = ""

        # Run the sync command
        result = subprocess.run(
            ["floridayvine", "sync", "customer-offers"],
            capture_output=True,
            text=True,
        )

        # Check that the command failed with an appropriate error message
        assert result.returncode != 0
        assert "Error" in result.stderr or "Error" in result.stdout
    finally:
        # Restore the API key
        if api_key:
            os.environ["FLORIDAY_API_KEY"] = api_key
