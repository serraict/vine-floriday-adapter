import os
from pprint import pprint
import time
import requests
from ..persistence import persist
from floriday_supplier_client import (
    TradeItemsApi,
    api_factory,
    DirectSalesApi,
    OrganizationsApi,
)
from floriday_supplier_client.models.organization import Organization

CLIENT_ID = os.getenv("FLORIDAY_CLIENT_ID")
CLIENT_SECRET = os.getenv("FLORIDAY_CLIENT_SECRET")
API_KEY = os.getenv("FLORIDAY_API_KEY")
AUTH_URL = os.getenv("FLORIDAY_AUTH_URL")
BASE_URL = os.getenv("FLORIDAY_BASE_URL")

payload = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "scope": "role:app catalog:read sales-order:write organization:read supply:read supply:write sales-order:read delivery-conditions:read fulfillment:write fulfillment:read",
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
}


def get_access_token():
    response = requests.request("POST", AUTH_URL, headers=headers, data=payload)
    response.raise_for_status()
    return response.json().get("access_token")


_api_factory = api_factory.ApiFactory()
_clt = _api_factory.get_api_client()


def get_organizations():
    access_token = get_access_token()
    url = f"{BASE_URL}/auth/key"

    headers = {
        "X-Api-Key": API_KEY,
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def sync_organizations(start_seq_number=0, limit_result=5):
    api = OrganizationsApi(_clt)
    my_sequence = start_seq_number
    max_seq_nr = api.get_organizations_max_sequence()

    print(f"Syncing organizations from {my_sequence} to {max_seq_nr} ...")

    while my_sequence < max_seq_nr:
        orgs_sync_result = api.get_organizations_by_sequence_number(
            sequence_number=my_sequence, limit_result=limit_result
        )
        max_seq_nr = orgs_sync_result.maximum_sequence_number
        for org in orgs_sync_result.results:
            print(f"Seq nr {org.sequence_number}: Persisting {org.name} ...")
            persist("organizations", org.organization_id, org.to_dict())
        my_sequence = orgs_sync_result.maximum_sequence_number
        time.sleep(0.5)
    print("Done syncing organizations")


def get_trade_items():
    api = TradeItemsApi(_clt)
    items = api.get_trade_items()
    return items


def get_direct_sales():
    api = DirectSalesApi(_clt)
    items = api.get_supply_lines()
    return items


def sync_trade_items(start_seq_number=0, limit_result=5):
    api = TradeItemsApi(_clt)
    my_sequence = start_seq_number
    max_seq_nr = api.get_trade_items_max_sequence()

    print(f"Syncing trade items from {my_sequence} to {max_seq_nr} ...")

    while my_sequence < max_seq_nr:
        trade_items_sync_result = api.get_trade_items_by_sequence_number(
            sequence_number=my_sequence, limit_result=limit_result
        )
        max_seq_nr = trade_items_sync_result.maximum_sequence_number
        for item in trade_items_sync_result.results:
            print(
                f"Seq nr {item.sequence_number}: Persisting {item.trade_item_name} ..."
            )
            persist("trade_items", item.trade_item_id, item.to_dict())
        my_sequence = trade_items_sync_result.maximum_sequence_number
        print(f"Next sequence number: {my_sequence}")
        time.sleep(0.5)
    print("Done syncing trade items")
