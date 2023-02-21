from book.exception import BookException
from book.logger import logging
import os,sys
import streamlit as st
from book.entity import config_entity
from book.utils import get_collection_as_dataframe
from book.components.data_ingestion import DataIngestion
#from book.components.data_transformation import DataTransformation
#from book.components.model_training import ModelTraining
from flask import Flask


if __name__=='__main__':
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print("my object::",data_ingestion_config.to_dict())

        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(data_ingestion.initiate_data_ingestion())

    except Exception as e:
        raise BookException(e,sys)
