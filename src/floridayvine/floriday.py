import os
from pprint import pprint
import requests

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


def get_trade_items():
    access_token = get_access_token()
    url = f"{BASE_URL}/trade-items"

    headers = {
        "X-Api-Key": API_KEY,
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    base_sync_number = 0
    sync_items = sync_trade_items(base_sync_number)
    max_sync_number = sync_items.get("maximumSequenceNumber")
    results = sync_items.get("results")
    print(f"{len(results)} trade items synced ({base_sync_number}..{max_sync_number})")
    # pprint(items)

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def sync_trade_items(base_sync_number=0):
    access_token = get_access_token()
    url = f"{BASE_URL}/trade-items/sync/{base_sync_number}"

    headers = {
        "X-Api-Key": API_KEY,
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
