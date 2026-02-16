from abc import ABC, abstractmethod
import pandas as pd 
import os 
import psycopg2
import requests
class DataSource(ABC):

    def load_data(self):
        self.connect()
        data = self.fetch()
        self.close()
        return data

    @abstractmethod
    def connect(self): pass

    @abstractmethod
    def fetch(self): pass

    @abstractmethod
    def close(self): pass

    

class MLModel(ABC):
    @abstractmethod
    def train(self,X,y):
        pass
    
    @abstractmethod
    def predict(self,X):
        pass
    
    @abstractmethod
    def save_model(self,path):
        pass

class CSVLoader(DataSource):
    def __init__(self,file_path):
        self.file_path = file_path
    
    def connect(self):
        print("cheking csv file path")
        if not os.path.exists(self.file_path):
            raise FileNotFoundError('file path not found')
        print("CSV file path varified")
    
    def fetch(self):
        df = pd.read_csv(self.file_path)
        return df
    
    def close(self):
        print("CSV load completed")

class SQLLoader(DataSource):

    def __init__(self, host, database, user, password, query):
        self.conn_params = {
            "host": host,
            "database": database,
            "user": user,
            "password": password
        }
        self.query = query
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(**self.conn_params)
        print("Connected to SQL database")

    def fetch(self):
        df = pd.read_sql(self.query, self.conn)
        return df

    def close(self):
        if self.conn:
            self.conn.close()
            print("SQL connection closed")