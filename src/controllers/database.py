from pymongo import collection, database, MongoClient
from typing import TypeVar, Type, Generic
from dataclasses import asdict
from functools import wraps
import logging

T = TypeVar("T")

def with_connection(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            # Conectar ao banco de dados
            self.connect_client()
            # Executar a função
            result = func(self, *args, **kwargs)
            logging.warning(f'{func.__name__} response: {result}')
            return result
        finally:
            # Fechar a conexão
            self.close()
    return wrapper


class MongoDB(Generic[T]):
    
    def __init__(self, connection, database) -> None:
        self.connection_string = connection
        self.db_name = database
        pass

    def set_container(self, collection_name):
        self.col_name = collection_name

    def connect_client(self):
        self.client: MongoClient = MongoClient(self.connection_string)
        self.database = self.client.get_database(self.db_name)
        self.container = self.database.get_collection(self.col_name)
        pass

    def close(self):
        self.client.close()
        pass

    @with_connection
    def create_item(self, instance: T):
        data_dict = asdict(instance)
        return self.container.insert_one(data_dict)
    
    @with_connection
    def query(self, filter: dict):
        res = self.container.find(filter)
        return list(res)
    
    @with_connection
    def update_item(self, data: dict):
        res = self.container.replace_one({'_id': data['_id']}, data)
        return res
    
    @with_connection
    def list_all_items(self):
        res = self.container.find()
        return list(res)
    
    @with_connection
    def create_item(self, data):
        return self.container.insert_one(data)
    pass