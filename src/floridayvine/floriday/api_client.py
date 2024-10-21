from floriday_supplier_client import api_factory

_api_factory = None
_clt = None


def get_api_client():
    global _api_factory, _clt
    if _api_factory is None:
        _api_factory = api_factory.ApiFactory()
    if _clt is None:
        _clt = _api_factory.get_api_client()
    return _clt
