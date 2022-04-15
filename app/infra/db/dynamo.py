from app.contracts.db_contract import DBContract
import boto3


class Dynamo(DBContract):
  
  def __init__(self, host: str, port: int, table_name: str):
    connection_str = f"http://{host}:{port}"
    self.__table_name = table_name
    self.__driver = boto3.resource('dynamodb', endpoint_url=connection_str)
    
  def create(self, item: dict):
    table = self.__driver.Table(self.__table_name)
    response = table.put_item(Item=item)
    return response