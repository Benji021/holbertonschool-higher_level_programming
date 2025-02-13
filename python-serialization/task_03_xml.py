#!/usr/bin/python3
"""Docstring Serialization ans Deserialization with XML"""


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into an XML file."""
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert all values to strings for XML storage
    
    tree = ET.ElementTree(root)
    with open(filename, "wb") as file:
        tree.write(file)

def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text  # Values will be strings by default
    
    return dictionary
