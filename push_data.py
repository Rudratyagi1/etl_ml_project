#basic imports
import os , sys , json
import pandas as pd
import numpy as np
import pymongo   


#internal imports
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging


#advance imports
import certifi
ca = certifi.where()


#load secrets
from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


#read data
class NetworkDataExtract():
    #create constructor
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    #create cv_to_json converter
    def cv_to_json_converter(self,file_path):

        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records

        except Exception as e:
            raise NetworkSecurityException(e,sys)

    #insert data to mongodb 
    def insert_data_mongodb(self,records,database,collection):

        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)
            return (len(self.records))


        except Exception as e:
            raise NetworkSecurityException(e,sys)



if __name__=="__main__":
    FILE_PATH = "network_data/phisingData.csv"
    DATABASE = "RUDRA1"
    COLLECTION = "Network_data"

    network_obj = NetworkDataExtract()

    records = network_obj.cv_to_json_converter(file_path=FILE_PATH)
    no_of_records = network_obj.insert_data_mongodb(records=records , database=DATABASE , collection=COLLECTION)
    print(no_of_records)



