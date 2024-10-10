from dataclasses import dataclass
import typer
from .commands import version, floriday, database, sync

app = typer.Typer()


@dataclass
class Common:
    pass


def register_commands():
    app.add_typer(version.app, name="version")
    app.add_typer(floriday.app, name="floriday")
    app.add_typer(database.app, name="db")
    app.add_typer(sync.app, name="sync")


@app.callback()
def common(
    ctx: typer.Context,
):
    ctx.obj = Common()


def main():
    register_commands()
    app()


if __name__ == "__main__":
    main()
