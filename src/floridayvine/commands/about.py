import typer
from importlib.metadata import version as get_package_version
from pprint import pprint
from ..floriday.misc import get_organizations

app = typer.Typer(invoke_without_command=True)


def get_version():
    return get_package_version("floridayvine")


@app.callback()
def callback(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        show_info()


@app.command()
def version():
    """
    Display the current version of Floriday Vine.
    """
    print(f"{get_version()}")


@app.command()
def show_info():
    """
    Display information about Floriday Vine and its connection to Floriday.
    """
    print(
        "Floriday Vine is a Python package to ingest Floriday trade information into Serra Vine."
    )
    print(f"Version: {get_version()}")
    print("\nFloriday Connection Status:")
    try:
        orgs = get_organizations()
        print("Successfully connected to Floriday.")
        print("Organizations:")
        pprint(orgs)
    except Exception as e:
        print(f"Failed to connect to Floriday. Error: {str(e)}")
        print("For troubleshooting, please refer to the project documentation:")
        print("https://github.com/serraict/vine-floriday-adapter#readme")


if __name__ == "__main__":
    app()
