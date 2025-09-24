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
