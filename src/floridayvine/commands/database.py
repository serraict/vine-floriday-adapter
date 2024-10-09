import typer
from ..persistence import (
    initialize_database,
    print_sync_status as persistence_print_sync_status,
)

app = typer.Typer()

@app.command()
def print_sync_status():
    persistence_print_sync_status()

@app.command()
def init_db():
    initialize_database()
