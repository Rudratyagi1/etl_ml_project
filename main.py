# ============================ #
#     Main Execution Script    #
# ============================ #

# Internal imports
from network_security.components import data_transformation
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation
from network_security.components.data_transformation import DataTransformation
from network_security.components.model_trainer import ModelTrainer
from network_security.entity.config_entity import DataIngestionConfig, ModelTrainerConfig, TrainingPipelineConfig , DataValidationConfig , DataTransformationConfig

import sys

# ---------------- Main Script ----------------
if __name__ == "__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()

        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)

        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)

        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact , data_transformation_config )
        logging.info("data Transformation started")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("data  Transformation  Completed")
        print(data_transformation_artifact)


        logging.info("model_training started")
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config = model_trainer_config , data_transform_artifact=data_transformation_artifact )
        model_trainer_artifact = model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")

    



        


    except Exception as e:
        # Raise custom exception with system traceback info
        raise NetworkSecurityException(e, sys)
