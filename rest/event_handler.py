from fastapi import FastAPI
import motor.motor_asyncio

from adapter.rest import create_domain_registry

from .config import MongoDBConfig


def create_mongo_db(config: MongoDBConfig):
    uri = f'mongodb://{config.MONGO_USERNAME}:{config.MONGO_PASSWORD}@{config.MONGO_SERVER}:{config.MONGO_PORT}'
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client.OrderingService
    return db


async def startup(app: FastAPI):
    app.state.mongo_db = create_mongo_db(app.state.mongo_config)
    app.state.registry = create_domain_registry(app.state.mongo_db)


async def shutdown(app: FastAPI):
    app.state.mongo_db.close()
