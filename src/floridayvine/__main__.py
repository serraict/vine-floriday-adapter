from typing_extensions import Annotated
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
def upload(
    path: Annotated[str, typer.Argument()],
    bucket: Annotated[str, typer.Argument(envvar="DEFAULT_BUCKET")] = "floriday",
    target_dir: Annotated[str, typer.Argument(envvar="DEFAULT_DIR")] = "inbox",
):
    upload_directory(bucket, target_dir, path)
    print(f" {path} --> {bucket}/{target_dir} ... upload complete")


def main():
    app()


if __name__ == "__main__":
    main()
