'''
all the code that is related to reading the data
 (contain all the data reading code here)

 => after reading the data we do data validation , data transformation 
 so we creatte new file which is data transorm   
 '''


'''
 read the data from specific data source  thet data source can be created by BIG Data team or maybe created by cloud rteam maybe some live stream data 
 our aim is to read that data will split that data into train,test then after data transformation happen (its happen in the next file data_transformation.py file)
'''
'''
below input require for data ingestion 
The input can be where i have to save the traning data , where i have to save test data , raw data 
'''

import sys
sys.path.append("./src")
from src.logger import logging
import os
from src.exception import CustomException
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass # this is besically used to create class veriable

@dataclass # without __init__ you can define your class variables with #dataclass
class DataIngestionconfig: # this take all the input
    train_data_path: str=os.path.join('artifacts','train.csv') # all the output will be stored in artifacts folder train.csv is file
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')
     
    
class DataIngestion: 
    def __init__(self): # if you want to define veriable then you can use dataclass 
        self.ingestion_config=DataIngestionconfig()

    def initiate_date_ingestion(self): # to read the data from database
        logging.info("Enter the dataingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("read the dataset as dataframe")
            print("location is ---------->222",self.ingestion_config)
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.train_data_path)),exist_ok=True) # Exist = True means if the directory alredy exoist then keep it dont delete and recreate it
            print("location is ---------->",self.ingestion_config)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("intial to train and test data")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("ingiestion is completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            print("e",e)
            raise CustomException(e,sys)

    
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_date_ingestion()

