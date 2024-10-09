import typer
from pprint import pprint
from ..floriday.misc import (
    get_organizations,
    get_trade_items,
    get_direct_sales,
    sync_organizations,
    sync_trade_items,
)

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

@app.command()
def sync_organizations_command(start_seq_number: int = 0, limit_result: int = 5):
    sync_organizations(start_seq_number, limit_result)

@app.command()
def sync_trade_items_command(start_seq_number: int = 0, limit_result: int = 5):
    sync_trade_items(start_seq_number, limit_result)
