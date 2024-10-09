from dataclasses import dataclass
import typer
from .minio import MinioClient
from .commands import version, minio, floriday, database

app = typer.Typer()


@dataclass
class Common:
    minio: MinioClient


def register_commands():
    app.add_typer(version.app, name="version")
    app.add_typer(minio.app, name="minio")
    app.add_typer(floriday.app, name="floriday")
    app.add_typer(database.app, name="db")


@app.callback()
def common(
    ctx: typer.Context,
    minio_endpoint: str = typer.Option(..., envvar="MINIO_ENDPOINT"),
    minio_access_key: str = typer.Option(..., envvar="MINIO_ACCESS_KEY"),
    minio_secret_key: str = typer.Option(..., envvar="MINIO_SECRET_KEY"),
):
    ctx.obj = Common(MinioClient(minio_endpoint, minio_access_key, minio_secret_key))


def main():
    register_commands()
    app()


if __name__ == "__main__":
    main()
