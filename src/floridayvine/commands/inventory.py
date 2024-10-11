import typer
from pprint import pprint
from ..floriday.misc import (
    get_trade_items,
    get_direct_sales,
)
from . import sync

app = typer.Typer()


@app.command()
def list_direct_sales():
    """
    List all direct sales from Floriday.
    """
    items = get_direct_sales()
    pprint(items)


@app.command()
def list_trade_items():
    """
    List all trade items from Floriday.
    """
    trade_items = get_trade_items()
    pprint(trade_items)


app.add_typer(sync.app, name="sync")
