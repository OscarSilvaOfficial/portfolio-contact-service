from app.infra.configs import enviroment
from app.infra.db.dynamo import Dynamo

def dynamodb_factory():
  return Dynamo(
    table_name=enviroment.TABLE_NAME,
    host=enviroment.HOST,
    port=enviroment.PORT
  )