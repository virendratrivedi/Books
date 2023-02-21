from book.logger import logging
from book.exception import BookException
import os,sys
from book import utils
from book.entity import config_entity
from book.entity import artifact_entity


class DataIngestion:
    def __init__(self,data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config

        except Exception as e:
            raise BookException(e, sys)

    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info(f"Exporting collection data as pandas dataframe")
            df_books:df.DataFrame=utils.get_collection_as_dataframe(database_name=self.data_ingestion_config.database_name, 
            collection_name=self.data_ingestion_config.collection_books)
            df_users:df.DataFrame=utils.get_collection_as_dataframe(database_name=self.data_ingestion_config.database_name,
             collection_name=self.data_ingestion_config.collection_users)
            df_ratings:df.DataFrame=utils.get_collection_as_dataframe(database_name=self.data_ingestion_config.database_name, 
            collection_name=self.data_ingestion_config.collection_ratings)

            logging.info("Save data in feature store")
            #Save data in feature store
            logging.info("Create feature store folder if not available")
            #Create feature store folder if not available
            
            feature_store_book_dir = os.path.dirname(self.data_ingestion_config.feature_store_book_file_path)
            os.makedirs(feature_store_book_dir,exist_ok=True)
            logging.info("Save df to feature store folder")
            #Save df to feature store folder
            #print("shape",df_books.shape)
            df_books.to_csv(path_or_buf=self.data_ingestion_config.feature_store_book_file_path,index=False,header=True)
            #df_users.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_dir,index=False,header=True)
            #df_reviews.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_dir,index=False,header=True)

            feture_store_users_dir = os.path.dirname(self.data_ingestion_config.feature_store_users_file_path)
            os.makedirs(feture_store_users_dir,exist_ok=True)
            df_users.to_csv(path_or_buf=self.data_ingestion_config.feature_store_users_file_path,index=False,header=True)

            feture_store_ratings_dir = os.path.dirname(self.data_ingestion_config.feature_store_ratings_file_path)
            os.makedirs(feture_store_ratings_dir,exist_ok=True)
            df_ratings.to_csv(path_or_buf=self.data_ingestion_config.feature_store_ratings_file_path,index=False,header=True)


            # Prepare artifact

            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(books_file_path=self.data_ingestion_config.feature_store_book_file_path,
            users_file_path=self.data_ingestion_config.feature_store_users_file_path,
            ratings_file_path=self.data_ingestion_config.feature_store_ratings_file_path)
               
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")  
            return data_ingestion_artifact 

        except Exception as e:
            raise BookException(e, sys)

        
