from minio import Minio
import os

minio_endpoint = os.getenv("MINIO_ENDPOINT")
minio_access_key = os.getenv("MINIO_ACCESS_KEY")
minio_secret_key = os.getenv("MINIO_SECRET_KEY")

minio_client = Minio(minio_endpoint, minio_access_key, minio_secret_key, secure=False)


def upload_directory(bucket: str, target_path: str, source_path: str):
    if not os.path.isdir(source_path):
        raise NotADirectoryError(f"{source_path} is not a directory.")
    for root, dirs, files in os.walk(source_path):
        for file in files:
            full_path = os.path.join(root, file)
            upload_file(bucket, os.path.join(target_path, file), full_path)


def upload_file(target_bucket: str, target_file: str, source_file: str):
    minio_client.fput_object(target_bucket, target_file, source_file)
