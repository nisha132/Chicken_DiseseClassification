import os
from box.exceptions import BoxValueError
import yaml
from src.CNNClassifier import logger
import json
import joblib
from ensure import ensure_annotations

from box import ConfigBox
from box.exceptions import BoxValueError

print("Box is working ✅")

from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns the content as a ConfigBox object.
    Args:
        path_to_yaml (Path): Path to the yaml file.
    raises:
        ValueError: If the file is empty.
        e: Empty file
    returns:
        ConfigBox: ConfigBox object containing the yaml file content.   """

    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)     
    except BoxValueError:
        raise ValueError("The yaml file is empty")  
    except Exception as e:
        raise e   
    

@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """
    Create list of directories
    Args:
        path_to_directories (list[Path]): List of directory paths to be created
        verbose (bool, optional): Whether to log the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")   

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary to a JSON file.
    Args:
        path (Path): The file path where the JSON data will be saved.
        data (dict): The dictionary to be saved as JSON.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)             

    logger.info(f"JSON file saved at: {path}")    

@ensure_annotations
def load_json(path: Path) -> dict:
    """Loads a JSON file and returns its content as a dictionary.
    Args:
        path (Path): The file path of the JSON file to be loaded. """

    with open(path) as json_file:
        content = json.load(json_file)

    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)    

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """Saves data to a binary file using joblib.
    Args:
        data (Any): The data to be saved.
        path (Path): The file path where the binary data will be saved.
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")


def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib.
    Args:
        path (Path): The file path of the binary file to be loaded. """

    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data    


@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in kilobytes (KB).
    Args:
        path (Path): The file path of the file whose size is to be determined.
    Returns:
        str: The size of the file in KB, formatted as a string with 'KB' suffix.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"

def decodeImage(imgstring, fileName):
    """
    Decode a base64 encoded image string and save it to a file. 
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()
    logger.info(f"Image saved to {fileName}")

def encodeImageIntoBase64(imagePath):
    """
    Encode an image file to a base64 string.
    """
    with open(imagePath, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
        logger.info(f"Image at {imagePath} encoded into base64 string")
        return b64_string    
    

