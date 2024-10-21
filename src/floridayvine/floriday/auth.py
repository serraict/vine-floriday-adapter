import os
import requests

# Constants
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


def _handle_request_exception(e, context):
    print(f"Error {context}: {str(e)}")
    if e.response is not None:
        print(f"Response content: {e.response.content}")
    raise


def get_access_token():
    try:
        response = requests.request("POST", AUTH_URL, headers=headers, data=payload)
        response.raise_for_status()
        return response.json().get("access_token")
    except requests.exceptions.RequestException as e:
        _handle_request_exception(e, "getting access token")


def get_auth_info():
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
        _handle_request_exception(e, "getting organizations")
