import os
import requests

FLORIDAY_CLIENT_ID = os.getenv("FLORIDAY_CLIENT_ID")
FLORIDAY_CLIENT_SECRET = os.getenv("FLORIDAY_CLIENT_SECRET")
url = os.getenv("FLORIDAY_URL")

payload = {
    "grant_type": "client_credentials",
    "client_id": FLORIDAY_CLIENT_ID,
    "client_secret": FLORIDAY_CLIENT_SECRET,
    "scope": "role:app catalog:read sales-order:write organization:read supply:read supply:write sales-order:read delivery-conditions:read fulfillment:write fulfillment:read",
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
}


def get_access_token():
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")
