from functools import partial
from fastapi import FastAPI

from .config import MongoDBConfig
from .event_handler import startup, shutdown

from . import endpoint


def create_app():
    fast_app = FastAPI(title='Ordering Service')
    fast_app.state.mongo_config = MongoDBConfig()
    fast_app.add_event_handler('startup', func=partial(startup, app=fast_app))
    fast_app.add_event_handler('shutdown', func=partial(shutdown, app=fast_app))
    return fast_app


app = create_app()

app.include_router(endpoint.order_router, prefix='/order', tags=['order'])
