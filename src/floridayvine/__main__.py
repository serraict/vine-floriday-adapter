import typer
from importlib.metadata import version
from .minio import upload_directory
import os

app = typer.Typer()


def get_version():
    return version("floridayvine")


@app.command()
def print_version():
    print(f"{get_version()}")


@app.command()
def about():
    print(
        "Floriday Vine is a Python package to ingest Floriday trade information into Serra Vine."
    )
    print(f" v{get_version()}")
    print(f" Minio endpoint: {os.getenv('MINIO_ENDPOINT', 'play.min.io')}")


@app.command()
def upload(path: str):
    bucket = "floridayvine-testbucket"
    target_dir = "quotations"
    upload_directory(bucket, target_dir, path)
    print(f" {path} --> {bucket} ... upload complete")


def main():
    app()


if __name__ == "__main__":
    main()
