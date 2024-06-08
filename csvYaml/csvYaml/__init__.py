"""
INIT file to initialize module
"""
# pylint: disable=C0103, E0401
import sys
from .converterFile import *

def converter(filename):
    '''Init method for the module'''
    if filename.split(".")[-1].lower() == "yaml":
        yamlToCsv(filename)
    elif filename.split(".")[-1].lower() == "csv":
        csvToYaml(filename)
    else:
        print("File not of acceptable format")
        sys.exit(1)

def getversion():
    with open('./version.txt', 'r', encoding='UTF-8') as file:
        version = file.read() 
    return version