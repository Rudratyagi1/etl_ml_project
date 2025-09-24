# ============================ #
#   Data Validation Component  #
# ============================ #

# -------- Standard Imports --------
import os
import sys
from scipy.stats import ks_2samp  # For detecting dataset drift using Kolmogorov-Smirnov test
import pandas as pd                 # Data handling

# -------- Internal Imports --------
from network_security.exception.exception import NetworkSecurityException  # Custom exception handling
from network_security.logging.logger import logging                        # Project-level logging
from network_security.constant.training_pipeline import SCHEMA_FILE_PATH   # Path to schema YAML
from network_security.utils.main_utils.utils import read_yaml_file, write_yaml_file  # YAML utils

# -------- Environment Variables Loader --------
from dotenv import load_dotenv
load_dotenv()  # Load secrets like MongoDB credentials from .env

# Load MongoDB URL from environment (never hardcode in codebase)
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)  # Debugging only; remove in production

# -------- Config / Entity Imports --------
from network_security.entity.config_entity import DataValidationConfig
from network_security.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact


class DataValidation:
    """
    Component for validating ingested datasets:
        - Checks column count
        - Detects dataset drift
        - Stores drift report
        - Returns DataValidationArtifact for pipeline
    """

    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            # Load schema YAML for reference
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        """
        Reads a CSV file into a pandas DataFrame.
        """
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def validate_no_of_columns(self, dataframe: pd.DataFrame) -> bool:
        """
        Validates if the DataFrame has the required number of columns
        based on the schema configuration.
        """
        try:
            number_of_columns = len(self._schema_config)
            logging.info(f"Required number of columns: {number_of_columns}")
            logging.info(f"DataFrame columns: {len(dataframe.columns)}")

            return len(dataframe.columns) == number_of_columns
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def detect_dataset_drift(self, base_df: pd.DataFrame, current_df: pd.DataFrame, threshold=0.05) -> bool:
        """
        Detects drift between base and current dataset using KS test.
        Saves a YAML report containing p-values and drift status per column.
        """
        try:
            status = True
            report = {}

            # Compare distributions for each column
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                ks_result = ks_2samp(d1, d2)

                # Determine if drift occurred
                is_found = ks_result.pvalue < threshold
                if is_found:
                    status = False

                # Update report
                report[column] = {
                    "p_value": float(ks_result.pvalue),
                    "drift_status": is_found
                }

            # Save drift report
            drift_report_file_path = self.data_validation_config.drift_report_file_path
            os.makedirs(os.path.dirname(drift_report_file_path), exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path, content=report)

            return status
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        """
        Main method to execute data validation:
            1. Reads ingested train/test datasets
            2. Validates number of columns
            3. Detects dataset drift
            4. Stores validated data and returns DataValidationArtifact
        """
        try:
            # Get train/test paths
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            # Read datasets
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            # Validate number of columns
            if not self.validate_no_of_columns(train_dataframe):
                logging.error("Train dataframe column validation failed")
            if not self.validate_no_of_columns(test_dataframe):
                logging.error("Test dataframe column validation failed")

            # Detect dataset drift
            drift_status = self.detect_dataset_drift(base_df=train_dataframe, current_df=test_dataframe)

            # Save validated train/test files
            os.makedirs(os.path.dirname(self.data_validation_config.valid_train_file_path), exist_ok=True)
            train_dataframe.to_csv(self.data_validation_config.valid_train_file_path, index=False, header=True)
            test_dataframe.to_csv(self.data_validation_config.valid_test_file_path, index=False, header=True)

            # Return DataValidationArtifact
            return DataValidationArtifact(
                validation_status=drift_status,
                valid_train_file_path=self.data_validation_config.valid_train_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
            )
        except Exception as e:
            raise NetworkSecurityException(e, sys)
