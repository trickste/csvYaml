"""
INIT file to initialize module
"""
# pylint: disable=C0103, E0401
import sys
from .converterFile import csvToYaml, yamlToCsv

def converter(input_file, output_path):
    '''Init method for the module'''
    output_file = ""
    if input_file.split(".")[-1].lower() in ["yaml","yml"]:
        output_file = yamlToCsv(input_file, output_path)
    elif input_file.split(".")[-1].lower() == "csv":
        output_file = csvToYaml(input_file, output_path)
    else:
        print("File not of acceptable format")
        sys.exit(1)
    return output_file
