#!/usr/bin/python3
"""Docstring Basic serialization"""


import json
import os

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    
    Parameters:
        data (dict): The dictionary data to serialize.
        filename (str): The name of the JSON file to save the data to. 
        
    If the file already exists, it will be replaced.
    """

    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
    print(f"Data has been serialized and saved to {filename}.")

def load_and_deserialize(filename):
    """
    Loads and deserializes a JSON file into a Python dictionary.
    
    Parameters:
        filename (str): The name of the JSON file to load data from.
    
    Returns:
        dict: The deserialized data as a Python dictionary.
    """

    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")

    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    print(f"Data has been loaded and deserialized from {filename}.")
    return data
