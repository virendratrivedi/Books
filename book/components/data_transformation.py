from book.logger import logging
from book.exception import BookException
from typing import Optional
import os,sys
from book import utils
import pandas as pd
import dill
import numpy as np
from book.entity import config_entity,artifact_entity


class DataTransformation:
    def __init__(self,data_transformation_config:config_entity.DataTransformationConfig,
                    data_ingestion_artifact:artifact_entity.DataIngestionArtifact):
        try:
            #logging.info(f"{'>>'*20} Data Transformation {'<<'*20}")
            self.data_transformation_config=data_transformation_config
            self.data_ingestion_artifact=data_ingestion_artifact

        except Exception as e:
            raise BookException(e, sys)\

    def initiate_data_transformation(self,)->artifact_entity.DataTransformationArtifact:
        try:
            logging.info(f"{'>>'*20} Data Transformation {'<<'*20}")
            #print(self.data_ingestion_artifact.books_file_path)
           
            book_df=pd.read_csv(self.data_ingestion_artifact.books_file_path,low_memory=False)
            ratings_df=pd.read_csv(self.data_ingestion_artifact.ratings_file_path,low_memory=False)
              
            # Merging Book and Rating DataFrame 
            logging.info(f"Merging Book and Rating DataFrame") 
            ratings_with_names=ratings_df.merge(book_df,on='ISBN')

            # I have to fetch average rating of books.Takes those book who have Votes greater than 250
            logging.info(f"Number of rating In each Books")
            num_rating_df = ratings_with_names.groupby('Book-Title').count()['Book-Rating'].reset_index()
            num_rating_df.rename(columns={'Book-Rating':'num-ratings'},inplace=True)

            # Average rating DataFrame
            logging.info(f"Average rating In each Books")
            avg_rating_df = ratings_with_names.groupby('Book-Title').mean()['Book-Rating'].reset_index()
            avg_rating_df.rename(columns={'Book-Rating':'avg-ratings'},inplace=True)

            # Mearging num of Rating Dataframe and Average rating DataFrame
            logging.info(f"Mearging num of Rating Dataframe and Average rating DataFrame") 
            popularity_df = num_rating_df.merge(avg_rating_df,on='Book-Title')
            logging.info(f"Total popular DF Rows and Column:{popularity_df.shape}")

            popularity_df = popularity_df[popularity_df['num-ratings']>=250].sort_values('avg-ratings',ascending=False).head(50)
            logging.info(f"New Popular Df Rows and Column:{popularity_df.shape}")

            # We need Author name,Image detail of this popular Df
            popularity_df = popularity_df.merge(book_df,on='Book-Title').drop_duplicates('Book-Title')[['Book-Title','Book-Author','Image-URL-M','num-ratings','avg-ratings']]
             
            rating_with_name_dir = os.path.dirname(self.data_transformation_config.ratings_with_names_file_path)
            os.makedirs(rating_with_name_dir,exist_ok=True)

            ratings_with_names.to_csv(path_or_buf=self.data_transformation_config.ratings_with_names_file_path,index=False,header=True)

            
            popular_pkl_dir = os.path.dirname(self.data_transformation_config.popular_pkl_file_path)
            os.makedirs(popular_pkl_dir,exist_ok=True)
            
            utils.save_object(file_path=self.data_transformation_config.popular_pkl_file_path, obj=popularity_df)
            # Save popular df pickle file
            #utils.save_obj(file_path=self.data_transformation_config.popular_pkl_file_path, obj=popularity_df)

            data_transformation_artifact=artifact_entity.DataTransformationArtifact(ratings_with_names_path=self.data_transformation_config.ratings_with_names_file_path, 
            popular_model_path=self.data_transformation_config.popular_pkl_file_path) 

            return data_transformation_artifact
            
        except Exception as e:
            raise BookException(e, sys)
