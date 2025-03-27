from floriday_supplier_client import (
    TradeItemsApi,
    DirectSalesApi,
    OrganizationsApi,
    CustomerOffersApi,
)
from .api_client import get_api_client
from .sync import sync_entities
from ..persistence import persist


def sync_organizations(start_seq_number=None, limit_result=50):
    api = OrganizationsApi(get_api_client())

    def persist_org(org):
        persist("organizations", org.organization_id, org.to_dict())
        return org.name

    return sync_entities(
        "organizations",
        api.get_organizations_by_sequence_number,
        persist_org,
        start_seq_number,
        limit_result,
    )


def get_trade_items():
    api = TradeItemsApi(get_api_client())
    items = api.get_trade_items()
    return items


def sync_trade_items(start_seq_number=None, limit_result=50):
    api = TradeItemsApi(get_api_client())

    def persist_item(item):
        persist("trade_items", item.trade_item_id, item.to_dict())
        return item.trade_item_name

    return sync_entities(
        "trade_items",
        api.get_trade_items_by_sequence_number,
        persist_item,
        start_seq_number,
        limit_result,
    )


def get_direct_sales():
    api = DirectSalesApi(get_api_client())
    items = api.get_supply_lines()
    return items


def sync_supply_lines(start_seq_number=None, limit_result=50):
    api = DirectSalesApi(get_api_client())

    def persist_supply_line(supply_line):
        persist("supply_lines", supply_line.supply_line_id, supply_line.to_dict())
        return supply_line.supply_line_id

    return sync_entities(
        "supply_lines",
        api.get_supply_lines_by_sequence_number,
        persist_supply_line,
        start_seq_number,
        limit_result,
    )


def sync_customer_offers(start_seq_number=None, limit_result=50):
    """
    Synchronize customer offers data from Floriday.

    Args:
        start_seq_number: Optional starting sequence number
        limit_result: Number of entities to fetch per batch

    Returns:
        Dictionary with sync statistics
    """
    api = CustomerOffersApi(get_api_client())

    def persist_offer(offer):
        persist("customer_offers", offer.offer_id, offer.to_dict())
        return offer.offer_number

    return sync_entities(
        "customer_offers",
        api.get_customer_offers_by_sequence_number,
        persist_offer,
        start_seq_number,
        limit_result,
    )
