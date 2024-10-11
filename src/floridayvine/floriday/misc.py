import os
import time
import requests
from ..persistence import persist, get_max_sequence_number
from floriday_supplier_client import (
    TradeItemsApi,
    api_factory,
    DirectSalesApi,
    OrganizationsApi,
)

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
    try:
        response = requests.request("POST", AUTH_URL, headers=headers, data=payload)
        response.raise_for_status()
        return response.json().get("access_token")
    except requests.exceptions.RequestException as e:
        print(f"Error getting access token: {str(e)}")
        if e.response is not None:
            print(f"Response content: {e.response.content}")
        raise


_api_factory = None
_clt = None


def get_api_client():
    global _api_factory, _clt
    if _api_factory is None:
        _api_factory = api_factory.ApiFactory()
    if _clt is None:
        _clt = _api_factory.get_api_client()
    return _clt


def get_organizations():
    try:
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
    except requests.exceptions.RequestException as e:
        print(f"Error getting organizations: {str(e)}")
        if e.response is not None:
            print(f"Response content: {e.response.content}")
        raise


def sync_entities(
    api,
    entity_type,
    get_max_sequence,
    get_by_sequence,
    persist_entity,
    start_seq_number=None,
    limit_result=5,
):
    if start_seq_number is None:
        start_seq_number = get_max_sequence_number(entity_type)

    my_sequence = start_seq_number
    max_seq_nr = get_max_sequence()

    print(f"Syncing {entity_type} from {my_sequence} to {max_seq_nr} ...")

    while my_sequence < max_seq_nr:
        sync_result = get_by_sequence(
            sequence_number=my_sequence, limit_result=limit_result
        )
        max_seq_nr = sync_result.maximum_sequence_number
        for entity in sync_result.results:
            print(
                f"Seq nr {entity.sequence_number}: Persisting {persist_entity(entity)} ..."
            )
        my_sequence = sync_result.maximum_sequence_number
        time.sleep(0.5)

    print(f"Done syncing {entity_type}")


def sync_organizations(start_seq_number=None, limit_result=5):
    api = OrganizationsApi(get_api_client())

    def persist_org(org):
        persist("organizations", org.organization_id, org.to_dict())
        return org.name

    sync_entities(
        api,
        "organizations",
        api.get_organizations_max_sequence,
        api.get_organizations_by_sequence_number,
        persist_org,
        start_seq_number,
        limit_result,
    )


def get_trade_items():
    api = TradeItemsApi(get_api_client())
    items = api.get_trade_items()
    return items


def get_direct_sales():
    api = DirectSalesApi(get_api_client())
    items = api.get_supply_lines()
    return items


def sync_trade_items(start_seq_number=None, limit_result=5):
    api = TradeItemsApi(get_api_client())

    def persist_item(item):
        persist("trade_items", item.trade_item_id, item.to_dict())
        return item.trade_item_name

    sync_entities(
        api,
        "trade items",
        api.get_trade_items_max_sequence,
        api.get_trade_items_by_sequence_number,
        persist_item,
        start_seq_number,
        limit_result,
    )
