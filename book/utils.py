from book.config import mongo_client
from book.exception import BookException
from book.logger import logging
import os,sys
import dill
import pandas as pd

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    try:
        
        logging.info(f"Reading data from database {database_name} and Collecion {collection_name}")
        df=pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found Column: {df.columns}")

        if '_id' in df.columns:
            df=df.drop("_id",axis=1)
            logging.info(f"Rows and column in df: {df.shape}") 

        return df  
     
    except Exception as e:
        raise BookException(e, sys)
    

def save_object(file_path:str,obj:object)-> None:
    try:
        logging.info(f"Entered the save object method of MainUtil class")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Exited the save object method of MainUtil class")    

    except Exception as e:
        raise BookException(e, sys)        


def load_object(file_path:str)->object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file:{file_path} is not exist")
        with open(file_path,"rb") as file_obj:
            print("file_obj",file_obj)
            return dill.load(file_obj)
    except Exception as e:
        raise BookException(e, sys)    