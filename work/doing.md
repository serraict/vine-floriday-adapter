# Doing

## Fixed: Authentication Error in Production

We were running into an authentication error when running in production. The issue was that the API client was using a hardcoded staging URL instead of the production URL from the environment variables.

### The Fix

We modified the `get_api_client()` function in `src/floridayvine/floriday/api_client.py` to ensure the API client uses the correct base URL from the environment variable:

```python
def get_api_client():
    """
    Get an API client with the correct base URL.

    This function ensures the API client uses the base URL from the environment variable,
    not the hardcoded staging URL in the Configuration class.
    """
    global _api_factory, _clt
    if _api_factory is None:
        _api_factory = api_factory.ApiFactory()
    if _clt is None:
        _clt = _api_factory.get_api_client()
        # Set the host to the base URL from the environment variable
        _clt.configuration.host = _api_factory.base_url
    return _clt
```

We also created a verification script (`scripts/verify_floriday_auth.sh`) that can be used to test the authentication in production.
This runs fine:

```bash
marijn@serraserver:/opt/serra-vine/scripts$ floridayvine about
Floriday Vine is a Python package to ingest Floriday trade information into Serra Vine.
Version: 0.12.5

Database Connection Status:
Successfully connected to the database at mongodb://root:'*****'@mongo:27017. Server version: 4.4.29. Database and indices are properly set up

Floriday Connection Status:
Successfully connected to Floriday.
Organizations:
{'apiVersion': '2024v1',
 'clientId': '7rgObHz4k4pfdEnE8qmF',
 'organizationId': '64a03e85-7792-3ce9-b5be-70b5ee7fa96c'}
```

But this does not:

```bash
marijn@serraserver:/opt/serra-vine/scripts$ floridayvine inventory list-trade-items
╭───────────────────── Traceback (most recent call last) ──────────────────────╮
│ /usr/local/lib/python3.12/site-packages/floridayvine/commands/inventory.py:2 │
│ 5 in list_trade_items                                                        │
│                                                                              │
│   22 │   """                                                                 │
│   23 │   List all trade items from Floriday.                                 │
│   24 │   """                                                                 │
│ ❱ 25 │   trade_items = get_trade_items()                                     │
│   26 │   pprint(trade_items)                                                 │
│   27                                                                         │
│                                                                              │
│ /usr/local/lib/python3.12/site-packages/floridayvine/floriday/misc.py:126 in │
│ get_trade_items                                                              │
│                                                                              │
│   123                                                                        │
│   124 def get_trade_items():                                                 │
│   125 │   api = TradeItemsApi(get_api_client())                              │
│ ❱ 126 │   items = api.get_trade_items()                                      │
│   127 │   return items                                                       │
│   128                                                                        │
│   129                                                                        │
│                                                                              │
│ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
│ │ api = <floriday_supplier_client.api.trade_items_api.TradeItemsApi object │ │
│ │       at 0x74f28688b2f0>                                                 │ │
│ ╰──────────────────────────────────────────────────────────────────────────╯ │
│                                                                              │
│ /usr/local/lib/python3.12/site-packages/floriday_supplier_client/api/trade_i │
│ tems_api.py:748 in get_trade_items                                           │
│                                                                              │
│    745 │   │   if kwargs.get('async_req'):                                   │
│    746 │   │   │   return self.get_trade_items_with_http_info(**kwargs)  # n │
│    747 │   │   else:                                                         │
│ ❱  748 │   │   │   (data) = self.get_trade_items_with_http_info(**kwargs)  # │
│    749 │   │   │   return data                                               │
│    750 │                                                                     │
│    751 │   def get_trade_items_with_http_info(self, **kwargs):  # noqa: E501 │
│                                                                              │
│ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
│ │ kwargs = {'_return_http_data_only': True}                                │ │
│ │   self = <floriday_supplier_client.api.trade_items_api.TradeItemsApi     │ │
│ │          object at 0x74f28688b2f0>                                       │ │
│ ╰──────────────────────────────────────────────────────────────────────────╯ │
│                                                                              │
│ /usr/local/lib/python3.12/site-packages/floriday_supplier_client/api/trade_i │
│ tems_api.py:809 in get_trade_items_with_http_info                            │
│                                                                              │
│    806 │   │   # Authentication setting                                      │
│    807 │   │   auth_settings = ['JWT Token', 'X-Api-Key']  # noqa: E501      │
│    808 │   │                                                                 │
│ ❱  809 │   │   return self.api_client.call_api(                              │
│    810 │   │   │   '/trade-items', 'GET',                                    │
│    811 │   │   │   path_params,                                              │
│    812 │   │   │   query_params,                                             │
│                                                                              │
│ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
│ │ _return_http_data_only = True                                            │ │
│ │             all_params = [                                               │ │
│ │                          │   'page',                                     │ │
│ │                          │   'limit_result',                             │ │
│ │                          │   'include_deleted',                          │ │
│ │                          │   'async_req',                                │ │
│ │                          │   '_return_http_data_only',                   │ │
│ │                          │   '_preload_content',                         │ │
│ │                          │   '_request_timeout'                          │ │
│ │                          ]                                               │ │
│ │          auth_settings = ['JWT Token', 'X-Api-Key']                      │ │
│ │            body_params = None                                            │ │
│ │     collection_formats = {}                                              │ │
│ │            form_params = []                                              │ │
│ │          header_params = {                                               │ │
│ │                          │   'Accept': 'application/json',               │ │
│ │                          │   'User-Agent':                               │ │
│ │                          'Swagger-Codegen/1.0.0/python'                  │ │
│ │                          }                                               │ │
│ │                    key = '_return_http_data_only'                        │ │
│ │                 kwargs = {'_return_http_data_only': True}                │ │
│ │        local_var_files = {}                                              │ │
│ │                 params = {                                               │ │
│ │                          │   'self':                                     │ │
│ │                          <floriday_supplier_client.api.trade_items_api.… │ │
│ │                          object at 0x74f28688b2f0>,                      │ │
│ │                          │   'all_params': [                             │ │
│ │                          │   │   'page',                                 │ │
│ │                          │   │   'limit_result',                         │ │
│ │                          │   │   'include_deleted',                      │ │
│ │                          │   │   'async_req',                            │ │
│ │                          │   │   '_return_http_data_only',               │ │
│ │                          │   │   '_preload_content',                     │ │
│ │                          │   │   '_request_timeout'                      │ │
│ │                          │   ],                                          │ │
│ │                          │   '_return_http_data_only': True,             │ │
│ │                          │   'kwargs': {                                 │ │
│ │                          │   │   '_return_http_data_only': True          │ │
│ │                          │   },                                          │ │
│ │                          │   'params': ...,                              │ │
│ │                          │   'key': '_return_http_data_only',            │ │
│ │                          │   'val': True,                                │ │
│ │                          │   'collection_formats': {},                   │ │
│ │                          │   'path_params': {},                          │ │
│ │                          │   'query_params': [],                         │ │
│ │                          │   ... +5                                      │ │
│ │                          }                                               │ │
│ │            path_params = {}                                              │ │
│ │           query_params = []                                              │ │
│ │                   self = <floriday_supplier_client.api.trade_items_api.… │ │
│ │                          object at 0x74f28688b2f0>                       │ │
│ │                    val = True                                            │ │
│ ╰──────────────────────────────────────────────────────────────────────────╯ │
│                                                                              │
│ /usr/local/lib/python3.12/site-packages/floriday_supplier_client/api_client. │
│ py:316 in call_api                                                           │
│                                                                              │
│   313 │   │   │   then the method will return the response directly.         │
│   314 │   │   """                                                            │
│   315 │   │   if not async_req:                                              │
│ ❱ 316 │   │   │   return self.__call_api(resource_path, method,              │
│   317 │   │   │   │   │   │   │   │      path_params, query_params, header_p │
│   318 │   │   │   │   │   │   │   │      body, post_params, files,           │
│   319 │   │   │   │   │   │   │   │      response_type, auth_settings,       │
│                                                                              │
│ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
│ │       _preload_content = True                                            │ │
│ │       _request_timeout = None                                            │ │
│ │ _return_http_data_only = True                                            │ │
│ │              async_req = None                                            │ │
│ │          auth_settings = ['JWT Token', 'X-Api-Key']                      │ │
│ │                   body = None                                            │ │
│ │     collection_formats = {}                                              │ │
│ │                  files = {}                                              │ │
│ │          header_params = {                                               │ │
│ │                          │   'Accept': 'application/json',               │ │
│ │                          │   'User-Agent':                               │ │
│ │                          'Swagger-Codegen/1.0.0/python'                  │ │
│ │                          }                                               │ │
│ │                 method = 'GET'                                           │ │
│ │            path_params = {}                                              │ │
│ │            post_params = []                                              │ │
│ │           query_params = []                                              │ │
│ │          resource_path = '/trade-items'                                  │ │
│ │          response_type = 'list[TradeItem]'                               │ │
│ │                   self = <floriday_supplier_client.api_client.ApiClient  │ │
│ │                          object at 0x74f2870d3b30>                       │ │
│ ╰──────────────────────────────────────────────────────────────────────────╯ │
│                                                                              │
│ /usr/local/lib/python3.12/site-packages/floriday_supplier_client/api_client. │
│ py:148 in __call_api                                                         │
│                                                                              │
│   145 │   │   url = self.configuration.host + resource_path                  │
│   146 │   │                                                                  │
│   147 │   │   # perform request and return response                          │
│ ❱ 148 │   │   response_data = self.request(                                  │
│   149 │   │   │   method, url, query_params=query_params, headers=header_par │
│   150 │   │   │   post_params=post_params, body=body,                        │
│   151 │   │   │   _preload_content=_preload_content,                         │
│                                                                              │
│ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
│ │       _preload_content = True                                            │ │
│ │       _request_timeout = None                                            │ │
│ │ _return_http_data_only = True                                            │ │
│ │          auth_settings = ['JWT Token', 'X-Api-Key']                      │ │
│ │                   body = None                                            │ │
│ │     collection_formats = {}                                              │ │
│ │                 config = <floriday_supplier_client.configuration.Config… │ │
│ │                          object at 0x74f286a1eba0>                       │ │
│ │                  files = {}                                              │ │
│ │          header_params = {                                               │ │
│ │                          │   'Accept': 'application/json',               │ │
│ │                          │   'User-Agent':                               │ │
│ │                          'Swagger-Codegen/1.0.0/python',                 │ │
│ │                          │   'Authorization': 'Bearer                    │ │
│ │                          eyJraWQiOiJnR0VBRVNmRTVJSkctWDBsQWhGeTlDRnUwdk… │ │
│ │                          │   'X-Api-Key':                                │ │
│ │                          'efa5f536d268d9f20acbb48456e2c7e166297c06d7f9b… │ │
│ │                          │   'Content-Type': 'application/json'          │ │
│ │                          }                                               │ │
│ │                 method = 'GET'                                           │ │
│ │            path_params = {}                                              │ │
│ │            post_params = []                                              │ │
│ │           query_params = []                                              │ │
│ │          resource_path = '/trade-items'                                  │ │
│ │          response_type = 'list[TradeItem]'                               │ │
│ │                   self = <floriday_supplier_client.api_client.ApiClient  │ │
│ │                          object at 0x74f2870d3b30>                       │ │
│ │                    url = 'https://api.staging.floriday.io/suppliers-api… │ │
│ ╰──────────────────────────────────────────────────────────────────────────╯ │
│                                                                              │
│ /usr/local/lib/python3.12/site-packages/floriday_supplier_client/api_client. │
│ py:338 in request                                                            │
│                                                                              │
│   335 │   │   │   │   _request_timeout=None):                                │
│   336 │   │   """Makes the HTTP request using RESTClient."""                 │
│   337 │   │   if method == "GET":                                            │
│ ❱ 338 │   │   │   return self.rest_client.GET(url,                           │
│   339 │   │   │   │   │   │   │   │   │   │   query_params=query_params,     │
│   340 │   │   │   │   │   │   │   │   │   │   _preload_content=_preload_cont │
│   341 │   │   │   │   │   │   │   │   │   │   _request_timeout=_request_time │
│                                                                              │
│ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
│ │ _preload_content = True                                                  │ │
│ │ _request_timeout = None                                                  │ │
│ │             body = None                                                  │ │
│ │          headers = {                                                     │ │
│ │                    │   'Accept': 'application/json',                     │ │
│ │                    │   'User-Agent': 'Swagger-Codegen/1.0.0/python',     │ │
│ │                    │   'Authorization': 'Bearer                          │ │
│ │                    eyJraWQiOiJnR0VBRVNmRTVJSkctWDBsQWhGeTlDRnUwdkVHZlc3… │ │
│ │                    │   'X-Api-Key':                                      │ │
│ │                    'efa5f536d268d9f20acbb48456e2c7e166297c06d7f9b985',   │ │
│ │                    │   'Content-Type': 'application/json'                │ │
│ │                    }                                                     │ │
│ │           method = 'GET'                                                 │ │
│ │      post_params = []                                                    │ │
│ │     query_params = []                                                    │ │
│ │             self = <floriday_supplier_client.api_client.ApiClient object │ │
│ │                    at 0x74f2870d3b30>                                    │ │
│ │              url = 'https://api.staging.floriday.io/suppliers-api-2024v… │ │
│ ╰──────────────────────────────────────────────────────────────────────────╯ │
│                                                                              │
│ /usr/local/lib/python3.12/site-packages/floriday_supplier_client/rest.py:228 │
│ in GET                                                                       │
│                                                                              │
│   225 │                                                                      │
│   226 │   def GET(self, url, headers=None, query_params=None, _preload_conte │
│   227 │   │   │   _request_timeout=None):                                    │
│ ❱ 228 │   │   return self.request("GET", url,                                │
│   229 │   │   │   │   │   │   │   headers=headers,                           │
│   230 │   │   │   │   │   │   │   _preload_content=_preload_content,         │
│   231 │   │   │   │   │   │   │   _request_timeout=_request_timeout,         │
│                                                                              │
│ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
│ │ _preload_content = True                                                  │ │
│ │ _request_timeout = None                                                  │ │
│ │          headers = {                                                     │ │
│ │                    │   'Accept': 'application/json',                     │ │
│ │                    │   'User-Agent': 'Swagger-Codegen/1.0.0/python',     │ │
│ │                    │   'Authorization': 'Bearer                          │ │
│ │                    eyJraWQiOiJnR0VBRVNmRTVJSkctWDBsQWhGeTlDRnUwdkVHZlc3… │ │
│ │                    │   'X-Api-Key':                                      │ │
│ │                    'efa5f536d268d9f20acbb48456e2c7e166297c06d7f9b985',   │ │
│ │                    │   'Content-Type': 'application/json'                │ │
│ │                    }                                                     │ │
│ │     query_params = []                                                    │ │
│ │             self = <floriday_supplier_client.rest.RESTClientObject       │ │
│ │                    object at 0x74f28688b290>                             │ │
│ │              url = 'https://api.staging.floriday.io/suppliers-api-2024v… │ │
│ ╰──────────────────────────────────────────────────────────────────────────╯ │
│                                                                              │
│ /usr/local/lib/python3.12/site-packages/floriday_supplier_client/rest.py:222 │
│ in request                                                                   │
│                                                                              │
│   219 │   │   │   logger.debug("response body: %s", r.data)                  │
│   220 │   │                                                                  │
│   221 │   │   if not 200 <= r.status <= 299:                                 │
│ ❱ 222 │   │   │   raise ApiException(http_resp=r)                            │
│   223 │   │                                                                  │
│   224 │   │   return r                                                       │
│   225                                                                        │
│                                                                              │
│ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
│ │ _preload_content = True                                                  │ │
│ │ _request_timeout = None                                                  │ │
│ │             body = None                                                  │ │
│ │          headers = {                                                     │ │
│ │                    │   'Accept': 'application/json',                     │ │
│ │                    │   'User-Agent': 'Swagger-Codegen/1.0.0/python',     │ │
│ │                    │   'Authorization': 'Bearer                          │ │
│ │                    eyJraWQiOiJnR0VBRVNmRTVJSkctWDBsQWhGeTlDRnUwdkVHZlc3… │ │
│ │                    │   'X-Api-Key':                                      │ │
│ │                    'efa5f536d268d9f20acbb48456e2c7e166297c06d7f9b985',   │ │
│ │                    │   'Content-Type': 'application/json'                │ │
│ │                    }                                                     │ │
│ │           method = 'GET'                                                 │ │
│ │      post_params = {}                                                    │ │
│ │     query_params = []                                                    │ │
│ │                r = <floriday_supplier_client.rest.RESTResponse object at │ │
│ │                    0x74f286f63010>                                       │ │
│ │             self = <floriday_supplier_client.rest.RESTClientObject       │ │
│ │                    object at 0x74f28688b290>                             │ │
│ │          timeout = None                                                  │ │
│ │              url = 'https://api.staging.floriday.io/suppliers-api-2024v… │ │
│ ╰──────────────────────────────────────────────────────────────────────────╯ │
╰──────────────────────────────────────────────────────────────────────────────╯
ApiException: (401)
Reason: Unauthorized
HTTP response headers: HTTPHeaderDict({'Content-Type': 'application/json', 
'Content-Length': '222', 'Connection': 'keep-alive', 'Date': 'Thu, 06 Mar 2025 
13:05:19 GMT', 'X-Amzn-Trace-Id': 'Root=1-67c99d8f-30043cf26631bfa255c9cd06', 
'x-amzn-RequestId': 'ef286e0a-49e4-480c-a453-b53c1a2b5a82', 
'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 
'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,X-Selected
-Organization-Id,X-Language-Code,X-Selected-Sub-Customer-Id', 
'x-amzn-ErrorType': 'UnauthorizedException', 'WWW-Authenticate': 'Bearer 
realm="Floriday API", error="invalid_token"', 'x-amz-apigw-id': 
'HAWOhG7IjoEEXBQ=', 'Access-Control-Allow-Methods': 
'DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT', 'X-Cache': 'Error from cloudfront', 
'Via': '1.1 07ddb29e6fb6e0d7584320febca423a6.cloudfront.net (CloudFront)', 
'X-Amz-Cf-Pop': 'FRA60-P8', 'X-Amz-Cf-Id': 
'2S-rLp-_NwPFdfqcOWc1w5YQKrrk1u8qNW9IXEFnlOdofFLl-uPGpw=='})
HTTP response body: b'{"type": 
"https://developer.floriday.io/docs/error-codes#invalid-access-token","title": 
"Unauthorized","detail": "The access token is missing, invalid or 
expired.","status": "401","domainErrorCode": "invalid-access-token"}'

marijn@serraserver:/opt/serra-vine/scripts$
```
