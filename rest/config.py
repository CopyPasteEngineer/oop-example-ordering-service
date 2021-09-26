from pydantic import BaseSettings


class MongoDBConfig(BaseSettings):
    MONGO_SERVER: str = 'mongo-db'
    MONGO_PORT: str = '27017'
    MONGO_USERNAME: str = ''
    MONGO_PASSWORD: str = ''
