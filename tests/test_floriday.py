import subprocess
import pytest

pytestmark = pytest.mark.integration


def test_can_connect_to_floriday():
    cp = subprocess.run(["floridayvine", "about", "show-info"])
    assert cp.returncode == 0


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
