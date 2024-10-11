import typer
from importlib.metadata import version as get_package_version

app = typer.Typer(invoke_without_command=True)


def get_version():
    return get_package_version("floridayvine")


@app.callback()
def callback(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        show_info()


@app.command()
def version():
    print(f"{get_version()}")


@app.command(name="show-info")
def show_info():
    print(
        "Floriday Vine is a Python package to ingest Floriday trade information into Serra Vine."
    )
    print(f" v{get_version()}")
