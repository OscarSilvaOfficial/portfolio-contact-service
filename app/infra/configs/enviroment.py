import os
from dotenv import load_dotenv

load_dotenv()

# Credenciais de acesso ao e-mail
ROOT_EMAIL=os.environ.get('EMAIL')
ROOT_PASSWORD=os.environ.get('PASSWORD')

# Credenciais de acesso ao banco de dados DYNAMO
TABLE_NAME=os.environ.get('TABLE_NAME')
HOST=os.environ.get('HOST')
PORT=os.environ.get('PORT')

# Credenciais de acesso ao banco de dados MONGO
MONGO_CONNECTION_STR=os.environ.get('MONGO_CONNECTION_STR')
MONGO_DB_NAME=os.environ.get('MONGO_DB_NAME')
MONGO_DB_COLLECTION=os.environ.get('MONGO_DB_COLLECTION')