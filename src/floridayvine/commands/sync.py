import typer
from ..floriday.misc import sync_organizations, sync_trade_items
from ..persistence import print_sync_status as persistence_print_sync_status


app = typer.Typer(help="Synchronize collections in the local database with Floriday.")


@app.command()
def status():
    """
    Display the synchronization status for all synchronized collections.
    """
    persistence_print_sync_status()


@app.command()
def organizations(start_seq_number: int = 0, limit_result: int = 5):
    """
    Synchronize organizations data from Floriday.
    """
    sync_organizations(start_seq_number, limit_result)


@app.command()
def trade_items(start_seq_number: int = 0, limit_result: int = 5):
    """
    Synchronize trade items data from Floriday.
    """
    sync_trade_items(start_seq_number, limit_result)
