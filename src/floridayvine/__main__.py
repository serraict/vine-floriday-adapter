from dataclasses import dataclass
import typer
import os
import sys
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


def check_environment_variables():
    required_vars = [
        "FLORIDAY_CLIENT_ID",
        "FLORIDAY_CLIENT_SECRET",
        "FLORIDAY_AUTH_URL",
        "FLORIDAY_BASE_URL",
        "FLORIDAY_API_KEY",
        "MONGODB_CONNECTION_STRING",
    ]
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if not value:
            missing_vars.append(var)
        print(f"Environment variable {var}: {'[SET]' if value else '[NOT SET]'}")

    if missing_vars:
        print(
            f"Error: Missing required environment variables: {', '.join(missing_vars)}"
        )
        print("Please set these variables before running the application.")
        print("For more information, refer to the project documentation:")
        print("https://github.com/serraict/vine-floriday-adapter#readme")
        sys.exit(1)


def main():
    check_environment_variables()
    register_commands()
    app()


if __name__ == "__main__":
    main()
