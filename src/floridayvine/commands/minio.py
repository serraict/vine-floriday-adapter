from typing_extensions import Annotated
import typer

app = typer.Typer()

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
