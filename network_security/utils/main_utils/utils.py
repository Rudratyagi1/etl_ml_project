import yaml
import os
import sys
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
import numpy as np
import dill
import pickle


def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its content as a Python dictionary.

    Args:
        file_path (str): Path to the YAML file to read.

    Returns:
        dict: Parsed content of the YAML file.

    Raises:
        NetworkSecurityException: If reading or parsing the file fails.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Writes Python object content into a YAML file.

    Args:
        file_path (str): Path where the YAML file should be written.
        content (object): Python object to serialize into YAML.
        replace (bool): If True and file exists, removes it before writing.

    Raises:
        NetworkSecurityException: If writing the YAML file fails.
    """
    try:
        # Remove existing file if replace is True
        if replace and os.path.exists(file_path):
            os.remove(file_path)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write content to YAML
        with open(file_path, "w") as file:
            yaml.dump(content, file)
            
    except Exception as e:
        raise NetworkSecurityException(e, sys)
