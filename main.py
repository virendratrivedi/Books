from book.exception import BookException
from book.logger import logging
import os,sys
from book.entity import config_entity
from book.utils import get_collection_as_dataframe,load_object
from book.components.data_ingestion import DataIngestion
from book.components.data_transformation import DataTransformation
from book.components.model_training import ModelTraining
from book.components.webapp import WebApp



if __name__=='__main__':
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        #print("my object::",data_ingestion_config.to_dict())

        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        
        # Data Transformation (Top-50 Books)
        data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
        data_transformation = DataTransformation(data_transformation_config=data_transformation_config,
                           data_ingestion_artifact=data_ingestion_artifact)
        data_transformation_artifact=data_transformation.initiate_data_transformation()

        # Model Training
        model_training_config = config_entity.ModelTrainingConfig(training_pipeline_config=training_pipeline_config)
        model_training = ModelTraining(model_training_config=model_training_config,
                      data_ingestion_artifact=data_ingestion_artifact,
                      data_transformation_artifact=data_transformation_artifact)
        model_training_artifact=model_training.initiate_model_training()
       
        # Creating Web App using Streamlit
        web_app=WebApp(data_ingestion_artifact=data_ingestion_artifact,
               data_transformation_artifact=data_transformation_artifact,
               model_training_artifact=model_training_artifact)
        
        web_app.initiate_webapp()




        

                    

            
           
        
        

                      

    except Exception as e:
        raise BookException(e,sys)
