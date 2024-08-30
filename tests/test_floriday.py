import subprocess
import pytest


pytestmark = pytest.mark.integration


def test_can_connect_to_floriday():
    cp = subprocess.run(["floridayvine", "floriday-connection-info"])
    assert cp.returncode == 0
