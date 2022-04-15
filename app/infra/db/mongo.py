from app.contracts.db_contract import DBContract
from fast_nosql_manager import MongoRepository


class Mongo(DBContract):
  
  def __init__(self, connection_str: str, db_name: str, collection: str):
    self.__collection = collection
    self.__driver = MongoRepository(connection_str, db_name)
    
  def create(self, item: dict):
    return self.__driver.create_document(self.__collection, item)