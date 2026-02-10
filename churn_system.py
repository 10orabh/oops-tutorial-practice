from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def get_data(self):
        pass

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