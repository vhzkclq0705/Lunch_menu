import os
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv('DB_NAME')

db_config = {
    "dbname": db_name,
    "user": os.getenv('DB_USERNAME'),
    "password": os.getenv('DB_PASSWORD'),
    "host": os.getenv('DB_HOST'),
    "port": os.getenv('DB_PORT')
}
