import typer
from ..persistence import initialize_database

app = typer.Typer(help="Database management commands.")


@app.command()
def init():
    initialize_database()
