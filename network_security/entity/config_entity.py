# ================================
# 📦 Imports
# ================================
from datetime import datetime  # To generate timestamps for artifact folders
import os                     # To handle directory and path operations
from network_security.constant import training_pipeline  # Import your constants file



# ================================
# ⚙️ Training Pipeline Configuration
# ================================
class TrainingPipelineConfig:
    """
    Configuration class for the overall training pipeline.
    Purpose:
    - Stores the pipeline name and artifact folder location.
    - Ensures that each pipeline run has its own timestamped directory.
    """

    def __init__(self, timestamp=datetime.now()):
        # Convert timestamp to string format for folder naming
        timestamp = timestamp.strftime("%d_%m_%Y_%H_%M_%S")

        # Name of your ML pipeline (from constants)
        self.pipeline_name = training_pipeline.PIPELINE_NAME

        # Root artifact folder (from constants)
        self.artifact_name = training_pipeline.ARTIFACT_DIR

        # Full artifact directory for this run (e.g., Artifacts/23_09_2025_12_15_00/)
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)

        # Store timestamp as string (useful for logging, saving models, or reports)
        self.timestamp: str = timestamp



# ================================
# ⚙️ Data Ingestion Configuration
# ================================
class DataIngestionConfig:
    """
    Configuration class for the data ingestion stage.
    Purpose:
    - Defines all paths & parameters needed for data ingestion.
    - Keeps ingestion logic generic & decoupled from hardcoded paths.
    """

    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        # Base directory for data ingestion (e.g., Artifacts/<timestamp>/data_ingestion/)
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )

        # Path to save raw feature store file (snapshot of raw dataset)
        # e.g., Artifacts/<timestamp>/data_ingestion/feature_store/phisingData.csv
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
            training_pipeline.FILE_NAME
        )

        # Path to save training data after splitting
        # e.g., Artifacts/<timestamp>/data_ingestion/ingested/train.csv
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TRAIN_FILE_NAME
        )

        # Path to save testing data after splitting
        # e.g., Artifacts/<timestamp>/data_ingestion/ingested/test.csv
        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TEST_FILE_NAME
        )

        # Train/Test split ratio (from constants)
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION

        # MongoDB collection name to insert raw/network data
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME

        # MongoDB database name
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME
        
