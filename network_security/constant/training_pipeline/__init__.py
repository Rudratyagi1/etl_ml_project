# ================================
# 📦 Basic Imports
# ================================
import os     # for path operations
import sys    # for system-level operations (like traceback info in exceptions)
import numpy as np   # for numerical operations (useful in preprocessing/ML)
import pandas as pd  # for data manipulation (CSV reading, DataFrame operations)


# ================================
# 🎯 Common Constants for Training Pipeline
# ================================
# Column in dataset that the model should predict
TARGET_COLUMN = "Result"  # Why? Model training requires a label column to predict

# Name of your ML pipeline/project
PIPELINE_NAME: str = "NetworkSecurity"  # Used in logs, artifacts, and reports

# Root folder where all artifacts of the pipeline (processed data, models, logs) are stored
ARTIFACT_DIR: str = "Artifacts"  # Keeps outputs organized and separate from source code

# Raw data filename (CSV) that your pipeline will ingest
FILE_NAME: str = "phisingData.csv"  # Ensures consistent file reference across modules

# Names for the train/test split files
TRAIN_FILE_NAME: str = "train.csv"  # Saved after splitting raw dataset
TEST_FILE_NAME: str = "test.csv"    # Saved after splitting raw dataset




# ================================
# 💾 Data Ingestion Related Constants
# ================================
# MongoDB collection name where raw data will be inserted
DATA_INGESTION_COLLECTION_NAME: str = "Network_data"  # Used in NetworkDataExtract class

# MongoDB database name
DATA_INGESTION_DATABASE_NAME: str = "RUDRA1"  # Centralized database name for ingestion

# Folder names for organizing ingestion artifacts
DATA_INGESTION_DIR_NAME: str  = "data_ingestion"            # Parent folder for ingestion stage
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"     # Folder to store raw feature snapshots
DATA_INGESTION_INGESTED_DIR: str = "ingested"              # Folder to store train/test splits

# Train/test split ratio
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2        # 20% test data, 80% train data
# Why? Ensures consistency across runs and reproducibility in experiments


