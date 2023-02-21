import os,sys
from book.logger import logging
from book.exception import BookException
from datetime import datetime

FILE_NAME_BOOKS = "books.csv"
FILE_NAME_USERS = "users.csv"
FILE_NAME_RATINGS = "ratings.csv"

class TrainingPipelineConfig:
    try:
        def __init__(self):
            self.artifact_dir=os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
    except Exception as e:
        raise BookException(e, sys)  
    
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name='mylib'
            self.collection_books='books'
            self.collection_users='users'
            self.collection_ratings='ratings'

            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_book_file_path=os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME_BOOKS)
            self.feature_store_users_file_path=os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME_USERS)
            self.feature_store_ratings_file_path=os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME_RATINGS)
            
        except Exception as e:
            raise BookException(e, sys)   

    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception  as e:
            raise BookException(e,sys)      

