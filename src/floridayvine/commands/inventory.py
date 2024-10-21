import typer
from pprint import pprint
from ..floriday.entities import (
    get_trade_items,
    get_direct_sales,
)

app = typer.Typer(help="Inventory management commands.")


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
