import subprocess
import pytest

pytestmark = pytest.mark.integration

def test_can_connect_to_floriday():
    cp = subprocess.run(["floridayvine", "floriday", "floriday-connection-info"])
    assert cp.returncode == 0

def test_can_print_direct_sales():
    cp = subprocess.run(["floridayvine", "floriday", "print-direct-sales"])
    assert cp.returncode == 0

def test_can_print_trade_items():
    cp = subprocess.run(["floridayvine", "floriday", "print-trade-items"])
    assert cp.returncode == 0

def test_can_sync_organizations():
    cp = subprocess.run(["floridayvine", "floriday", "sync-organizations-command", "--limit-result", "5"])
    assert cp.returncode == 0

def test_can_sync_trade_items():
    cp = subprocess.run(["floridayvine", "floriday", "sync-trade-items-command", "--start-seq-number", "0", "--limit-result", "5"])
    assert cp.returncode == 0
