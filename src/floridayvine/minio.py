from minio import Minio
import os


class MinioClient:
    def __init__(self, endpoint: str, access_key: str, secret_key: str):
        self.endpoint = endpoint
        self.client = Minio(endpoint, access_key, secret_key, secure=False)

    def upload_directory(self, bucket: str, target_path: str, source_path: str):
        if not os.path.isdir(source_path):
            raise NotADirectoryError(f"{source_path} is not a directory.")
        for root, dirs, files in os.walk(source_path):
            for file in files:
                full_path = os.path.join(root, file)
                self.upload_file(bucket, os.path.join(target_path, file), full_path)

    def upload_file(self, target_bucket: str, target_file: str, source_file: str):
        self.client.fput_object(target_bucket, target_file, source_file)
