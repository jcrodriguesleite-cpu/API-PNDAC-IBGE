import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

MONGO_URI = os.getenv("uri")

class Load:
    def __init__(self):
        self.MONGO_URI = os.getenv("uri")

        """
        Método de extração de dados do PNADC

        Atributos:
            nome_arquivo: string
            data: list (resultado do request na api do IBGE)
        """

    def load_json(self, nome_arquivo, data:list):
        with open(f'{nome_arquivo}.json','w',encoding='utf-8') as f:
            json.dump(data, f)

    def insert_in_mongo(self,uni_dict,db_name,collection_name):
        uri = self.MONGO_URI

        client = MongoClient(uri, server_api=ServerApi('1'))

        db = client[db_name]

        collection = db[collection_name]

        if uni_dict:

            collection.insert_many(uni_dict)
            print("Dados inseridos com sucesso!")
