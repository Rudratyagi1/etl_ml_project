# ============================ #
#   Data Ingestion Artifact    #
# ============================ #

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """
    Holds metadata about data ingestion outputs.
    Attributes:
        trained_file_path (str): Path to the training dataset CSV file.
        test_file_path (str): Path to the testing dataset CSV file.
    """
    trained_file_path: str
    test_file_path: str



@dataclass
class DataValidationArtifact:
    """
    Data class to hold the metadata and results from the data validation step 
    of the ML pipeline.

    Attributes:
        validation_status (bool): Indicates whether the dataset passed validation.
        valid_train_file_path (str): File path to the validated training dataset CSV.
        valid_test_file_path (str): File path to the validated testing dataset CSV.
        invalid_train_file_path (str): File path to the invalid training dataset CSV.
        invalid_test_file_path (str): File path to the invalid testing dataset CSV.
        drift_report_file_path (str): File path to the data drift report (YAML/JSON).
    """
    
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str


