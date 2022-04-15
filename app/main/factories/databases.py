from app.infra.configs import enviroment
from app.infra.db.dynamo import Dynamo
from app.infra.db.mongo import Mongo

def dynamodb_factory():
  return Dynamo(
    table_name=enviroment.TABLE_NAME,
    host=enviroment.HOST,
    port=enviroment.PORT
  )
  
def mongodb_factory():
  return Mongo(
    connection_str=enviroment.MONGO_CONNECTION_STR,
    db_name=enviroment.MONGO_DB_NAME,
    collection=enviroment.MONGO_DB_COLLECTION
  )