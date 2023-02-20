import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://arpit_t:12345@cluster0.ekedees.mongodb.net/?retryWrites=true&w=majority")

@dataclass
class EnvirontVariable:
    mongo_db_url:str=os.getenv("MONGO_DB_URL")

env_var = EnvirontVariable()    

print(env_var.mongo_db_url)
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)