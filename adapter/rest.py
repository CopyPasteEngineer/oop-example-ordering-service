from domain.model.registry import DomainRegistry

from .model.maps.service import GoogleMapsService
from .model.order.repository import MongoDBOrderRepository
from .model.payment.service import PayPalPaymentService
from .model.product.service import ProductService


def create_domain_registry(mongo_db):
    registry = DomainRegistry()
    registry.assign_defaults()

    registry.maps_service = GoogleMapsService()
    registry.order_repository = MongoDBOrderRepository(mongo_db)
    registry.payment_service = PayPalPaymentService()
    registry.product_service = ProductService()

    return registry
