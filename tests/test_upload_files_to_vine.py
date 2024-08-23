import subprocess
import pytest
import glob
import os

from minio import Minio

# Since we do not specify a minio cli options in our tests,
# floridayvine will fallback to the environment variables,
# so we can use those for our assertions too.
minio_endpoint = os.getenv("MINIO_ENDPOINT")
minio_access_key = os.getenv("MINIO_ACCESS_KEY")
minio_secret_key = os.getenv("MINIO_SECRET_KEY")
minio_client = Minio(minio_endpoint, minio_access_key, minio_secret_key, secure=False)

# this module only runs in an integration test environment:
pytestmark = pytest.mark.integration

bucket = "floridayvine-testbucket"


@pytest.fixture(scope="module", autouse=True)
def setup():
    assert minio_client.bucket_exists(bucket) == True


@pytest.fixture(autouse=True)
def teardown_integration():
    yield  # This is where the testing happens

    for obj in minio_client.list_objects(bucket, recursive=True):
        print(f"Removing {obj.object_name} from {bucket}")
        minio_client.remove_object(bucket, obj.object_name)

    assert (
        count_blobs() == 0
    ), f"Bucket '{bucket}' should be empty after each test, but it is not."


def test_can_run_script():
    source_dir = "tests/data/"
    cp = subprocess.run(["floridayvine", "upload", source_dir])
    assert cp.returncode == 0

    file_count = count_files(source_dir)
    blob_count = count_blobs(bucket)

    assert blob_count == file_count


def count_blobs(in_bucket=bucket):
    blob_count = len(list(minio_client.list_objects(in_bucket, recursive=True)))
    return blob_count


def count_files(source_dir):
    file_paths = glob.glob(f"{source_dir}/**", recursive=True)
    files_only = [f for f in file_paths if os.path.isfile(f)]
    file_count = len(files_only)
    return file_count
