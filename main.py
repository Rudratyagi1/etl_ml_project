# ============================ #
#     Main Execution Script    #
# ============================ #

# Internal imports
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.components.data_ingestion import DataIngestion
from network_security.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
import sys

# ---------------- Main Script ----------------
if __name__ == "__main__":
    try:
        # 1️⃣ Load the global training pipeline configuration
        training_pipeline_config = TrainingPipelineConfig()

        # 2️⃣ Initialize the Data Ingestion configuration using the training pipeline config
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)

        # 3️⃣ Instantiate the DataIngestion component
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Starting data ingestion process...")

        # 4️⃣ Execute data ingestion: fetch from MongoDB, export feature store, split train/test
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        # 5️⃣ Print the paths to the generated train/test CSV files
        print(data_ingestion_artifact)

    except Exception as e:
        # Raise custom exception with system traceback info
        raise NetworkSecurityException(e, sys)
