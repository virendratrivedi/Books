from book.logger import logging
from book.exception import BookException
from typing import Optional
import os,sys
import streamlit as st
from book import utils
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import dill
import numpy as np
from book.entity import config_entity,artifact_entity

class WebApp:
    def __init__(self,data_ingestion_artifact:artifact_entity.DataIngestionArtifact,
                     data_transformation_artifact:artifact_entity.DataTransformationArtifact,
                     model_training_artifact:artifact_entity.ModelTrainingArtifact):
        try:
            logging.info(f"{'>>'*20} Web App {'<<'*20}")
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_transformation_artifact=data_transformation_artifact
            self.model_training_artifact=model_training_artifact
            
        except Exception as e:
            raise BookException(e,sys)
        
    def initiate_webapp(self,):
        try:
            popular_df=utils.load_object(self.data_transformation_artifact.popular_model_path)
            titles=list(popular_df['Book-Title'].values[0:51])
            texts=list(popular_df['Book-Author'].values[0:51])
            img_srcs=list(popular_df['Image-URL-M'].values[0:51])

            pt=utils.load_object(self.model_training_artifact.pivot_table_path)
            allbooks=pt.index 

            st.sidebar.title("Navigation")
            nav=st.sidebar.radio("pages",["Home","Recommendation"])

            if nav=="Home":
                st.header("Home")
                st.header("TOP 50 BOOKS")
                col1, col2, col3 = st.columns(3)
                for i in range(len(img_srcs)):
                    if i % 3 == 0:
                        card_col = col1
                    elif i % 3 == 1:  
                        card_col = col2   
                    else:
                        card_col = col3 
                    with card_col:
                        st.image(img_srcs[i], use_column_width=True,)
                        st.markdown(f"<h3 style='font-size: 10px;'>{titles[i]}</h3>", unsafe_allow_html=True)
                        st.write(texts[i])   
                    
            if nav=="Recommendation":
                st.header("reco") 
                
            
        except Exception as e:
            raise BookException(e,sys)
