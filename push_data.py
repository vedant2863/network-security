import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv('MONGO_DB_URL')

print(MONGO_DB_URL)

import certifi

ca = certifi.where()
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger


class NetworkSecurityExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)

            json_data = data.T.to_json()  # Convert DataFrame to JSON

            if json_data is None:  # Check if conversion failed
                raise ValueError("Conversion to JSON returned None")

            records = list(json.loads(json_data).values())  # Ensure json_data is valid
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def insert_data_mongodb(self,records,database,collection):
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)  # Connect to MongoDB
            self.database = self.mongo_client[database]  # Get the database
            self.collection = self.database[collection]  # Get the collection
            self.collection.insert_many(records)  # Insert records
            return len(records)  # Return the number of inserted records
        except Exception as e:
                raise NetworkSecurityException(e, sys.exc_info())


if __name__ == '__main__':
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "deku"
    COLLECTION = "network_data"
    networkObj = NetworkSecurityExtract()
    records = networkObj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records = networkObj.insert_data_mongodb(records=records,database=DATABASE,collection=COLLECTION)
    print(no_of_records)
