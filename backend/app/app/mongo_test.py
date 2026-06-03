from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(uri)

try:
    print(client.admin.command("ping"))
    print("MongoDB Connected Successfully")
except Exception as e:
    print("ERROR:", e)