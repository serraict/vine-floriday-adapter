import subprocess
from floridayvine.minio import minio_client


def test_assert_that_minio_test_server_is_available():
    assert minio_client.bucket_exists("floridayvine-testbucket") == True


def test_can_run_script():
    cp = subprocess.run(["floridayvine", "upload", "tests/data/"])
    assert cp.returncode == 0
    # assert that the file is uploaded to the minio server
