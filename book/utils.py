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