import typer
from importlib.metadata import version

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
    print(f"v{get_version()}")


def main():
    app()


if __name__ == "__main__":
    main()
