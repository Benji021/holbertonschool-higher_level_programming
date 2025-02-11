#!/usr/bin/python3
"""Docstring Serialization ans Deserialization with XML"""


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')
    
    def add_elements(parent, dictionary):
        for key, value in dictionary.items():
            element = ET.SubElement(parent, key)
            if isinstance(value, dict):
                add_elements(element, value)
            else:
                element.text = str(value)
    
    add_elements(root, dictionary)
    
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    def elements_to_dict(element):
        dictionary = {}
        for child in element:
            if len(child) > 0:
                dictionary[child.tag] = elements_to_dict(child)
            else:
                dictionary[child.tag] = convert_type(child.text)
        return dictionary
    
    def convert_type(value):
        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            return value
    
    return elements_to_dict(root)
