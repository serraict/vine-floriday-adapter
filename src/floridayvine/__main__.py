from dataclasses import dataclass
from typing_extensions import Annotated
import typer
from importlib.metadata import version
from .minio import MinioClient
from .floriday import get_organizations
from pprint import pprint


app = typer.Typer()


@dataclass
class Common:
    minio: MinioClient


def get_version():
    return version("floridayvine")


@app.command()
def print_version():
    print(f"{get_version()}")


@app.command()
def about(ctx: typer.Context):
    print(
        "Floriday Vine is a Python package to ingest Floriday trade information into Serra Vine."
    )
    print(f" v{get_version()}")
    print(f" Minio endpoint: {ctx.obj.minio.endpoint}")


@app.command()
def upload(
    ctx: typer.Context,
    path: Annotated[str, typer.Argument()],
    bucket: Annotated[str, typer.Argument(envvar="DEFAULT_BUCKET")] = "floriday",
    target_dir: Annotated[str, typer.Argument(envvar="DEFAULT_DIR")] = "inbox",
):
    """Upload a directory to Minio"""
    clt = ctx.obj.minio
    clt.upload_directory(bucket, target_dir, path)
    print(f" {path} --> {bucket}/{target_dir} ... upload complete")


@app.command()
def floriday_connection_info():
    orgs = get_organizations()
    print("Connected to Floriday:")
    pprint(orgs)


@app.callback()
def common(
    ctx: typer.Context,
    minio_endpoint: Annotated[str, typer.Option(envvar="MINIO_ENDPOINT")],
    minio_access_key: Annotated[str, typer.Option(envvar="MINIO_ACCESS_KEY")],
    minio_secret_key: str = typer.Option(envvar="MINIO_SECRET_KEY"),
):
    ctx.obj = Common(MinioClient(minio_endpoint, minio_access_key, minio_secret_key))


def main():
    app()


if __name__ == "__main__":
    main()
