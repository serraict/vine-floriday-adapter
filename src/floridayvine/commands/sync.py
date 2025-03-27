import typer
from ..floriday.entities import (
    sync_organizations,
    sync_trade_items,
    sync_supply_lines,
    sync_customer_offers,
)
from ..persistence import print_sync_status as persistence_print_sync_status


app = typer.Typer(help="Synchronize collections in the local database with Floriday.")


@app.command()
def status():
    """
    Display the synchronization status for all synchronized collections.
    """
    persistence_print_sync_status()


@app.command()
def organizations(start_seq_number: int = None, limit_result: int = 5):
    """
    Synchronize organizations data from Floriday.
    """
    sync_organizations(start_seq_number, limit_result)


@app.command()
def trade_items(start_seq_number: int = None, limit_result: int = 5):
    """
    Synchronize trade items data from Floriday.
    """
    sync_trade_items(start_seq_number, limit_result)


@app.command()
def supply_lines(start_seq_number: int = None, limit_result: int = 5):
    """
    Synchronize supply lines data from Floriday.
    """
    sync_supply_lines(start_seq_number, limit_result)


@app.command()
def customer_offers(start_seq_number: int = None, limit_result: int = 5):
    """
    Synchronize customer offers data from Floriday.
    """
    sync_customer_offers(start_seq_number, limit_result)
