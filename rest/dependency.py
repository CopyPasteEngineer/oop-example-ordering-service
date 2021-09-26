from fastapi import Request, Depends

from domain.model.registry import DomainRegistry
from domain.model.order import OrderService, OrderRepositoryAbstract


async def get_mongo_db(request: Request):
    mongo_db = request.app.state.mongo_db
    return mongo_db


async def get_domain_registry(request: Request) -> DomainRegistry:
    registry: DomainRegistry = request.app.state.registry
    return registry


async def _get_order_service(request: Request) -> OrderService:
    registry: DomainRegistry = request.app.state.registry
    return registry.order_service


def get_order_service() -> OrderService:
    return Depends(_get_order_service)


async def _get_order_repository(request: Request) -> OrderRepositoryAbstract:
    registry: DomainRegistry = request.app.state.registry
    return registry.order_repository


def get_order_repository() -> OrderRepositoryAbstract:
    return Depends(_get_order_repository)
