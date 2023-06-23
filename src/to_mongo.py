from base import Base
from dotenv import load_dotenv
import pymongo
import os

# class definition 
class ToMongo(Base):
    def __init__(self):
        Base.__init__(self)
        load_dotenv()
        self.mongo_url = os.getenv('MONGO_URL')
        #connect to pymongo
        self.client = pymongo.MongoClient(self.mongo_url)
        # create the database 
        self.db = self.client.drop_database
        self.df.set_index('ph', inplace=True)

if __name__ == '__main__':
    c = ToMongo()
    print('Successful connection to client object')


# this is to test as I go 