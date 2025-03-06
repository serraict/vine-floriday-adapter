from floriday_supplier_client import api_factory

_api_factory = None
_clt = None


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
