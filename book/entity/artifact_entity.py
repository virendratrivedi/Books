from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    books_file_path:str
    users_file_path:str
    ratings_file_path:str

@dataclass
class DataTransformationArtifact:
    ratings_with_names_path:str
    popular_model_path:str

@dataclass
class ModelTrainingArtifact:
    similarity_score_path:str
    pivot_table_path:str

class ModelEvaluationArtifact:...

class ModelPusherArtifact:...