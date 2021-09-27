from fastapi import Request

from domain.model.registry import DomainRegistry


async def get_mongo_db(request: Request):
    mongo_db = request.app.state.mongo_db
    return mongo_db


async def get_domain_registry(request: Request) -> DomainRegistry:
    registry: DomainRegistry = request.app.state.registry
    return registry
