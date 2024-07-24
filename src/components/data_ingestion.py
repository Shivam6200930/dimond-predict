import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


## intialize the data ingestion configuration

@dataclass
class DataIngestionconfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')


## create a data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')

        try:
            df=pd.read_csv(os.path.join('notebook/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Train test split")
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of data is completed')
            train_data_path =  self.ingestion_config.train_data_path
            test_data_path =  self.ingestion_config.test_data_path
            print(f"Train Data Path: {train_data_path}, Test Data Path: {test_data_path}")

            if not os.path.isfile(train_data_path):
                raise FileNotFoundError(f"Train data file does not exist at {train_data_path}")
            if not os.path.isfile(test_data_path):
                raise FileNotFoundError(f"Test data file does not exist at {test_data_path}")

            # Print or log the paths for debugging
            logging.info(f"Train Data Path: {train_data_path}")
            logging.info(f"Test Data Path: {test_data_path}")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

            
        except FileNotFoundError as e:
            logging.error(f"FileNotFoundError: {str(e)}")
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred: {str(e)}")
            return None








