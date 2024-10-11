from . import config  # noqa: F401
from dataclasses import dataclass
import typer
from .commands import about, inventory, database, sync

app = typer.Typer()


@dataclass
class Common:
    pass


def register_commands():
    app.add_typer(about.app, name="about")
    app.add_typer(inventory.app, name="inventory")
    app.add_typer(database.app, name="db")
    app.add_typer(sync.app, name="sync")


@app.callback()
def common(
    ctx: typer.Context,
):
    ctx.obj = Common()


def main():
    config.check_environment_variables()  # Explicitly call the function
    register_commands()
    app()


if __name__ == "__main__":
    main()
