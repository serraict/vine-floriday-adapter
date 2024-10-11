import typer
from ..persistence import initialize_database

app = typer.Typer()


@app.command()
def init():
    initialize_database()
