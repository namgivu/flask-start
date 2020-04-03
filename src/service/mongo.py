import os
from pymongo import MongoClient
from dotenv import load_dotenv
from .misc import torr

load_dotenv() # https://preslav.me/2019/01/09/dotenv-files-python/

MONGO_DB_HOST = os.environ.get('MONGO_DB_HOST'); torr(MONGO_DB_HOST, 'Require :MONGO_DB_HOST in system variable')
MONGO_DB_PORT = os.environ.get('MONGO_DB_PORT', 27017)
MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME'); torr(MONGO_DB_NAME, 'Require :MONGO_DB_NAME in system variable')


def connect(collection_name):
    """
    connect to db then collection in mongodb
    """
    client  = MongoClient(host=f'mongodb://{MONGO_DB_HOST}:{MONGO_DB_PORT}/', connect=False)  # connect=False means prepare client instance only; the real connection opened on 1st query
    db      = client[MONGO_DB_NAME]; torr(db, f'Failed to connect to mongo database {MONGO_DB_NAME}')
    c       = db[collection_name];   torr(db, f'Mongo collection not found {collection_name} in db {MONGO_DB_NAME}')  # c aka collection
    return c


def insert(document:dict, collection_name:str):
    c = connect(collection_name)
    c.insert_one(document)
