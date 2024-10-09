import typer
from pprint import pprint
from ..floriday.misc import (
    get_organizations,
    get_trade_items,
    get_direct_sales,
)
from . import sync

app = typer.Typer()

@app.command()
def floriday_connection_info():
    orgs = get_organizations()
    print("Connected to Floriday:")
    pprint(orgs)

@app.command()
def print_direct_sales():
    items = get_direct_sales()
    pprint(items)

@app.command()
def print_trade_items():
    trade_items = get_trade_items()
    pprint(trade_items)

app.add_typer(sync.app, name="sync")
