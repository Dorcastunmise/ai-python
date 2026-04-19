import os
from dotenv import load_dotenv

#load_dotenv("../folder/.env") or
load_dotenv()

api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_NAME', 'default.db')

print(f"API Key: {api_key}" + "\n" + f"Database: {database}")