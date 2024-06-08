"""
Converter file to initialize module
"""
# pylint: disable=C0103, E0401
import sys
import yaml
import pandas as pd

def manageListYAML(data, output, header):
    '''This function populates list content and checks dataype of upcoming data'''
    for elementNo,_ in enumerate(data):
        if header == "":
            head = ""
        else:
            head = header + str(elementNo) + "/"
        if isinstance(data[elementNo],list):
            manageListYAML(data[elementNo], output, head)
        elif isinstance(data[elementNo], dict):
            manageDictYAML(data[elementNo], output, head)
        else:
            head = head[:-1]
            if head in output:
                output[head].append(data[elementNo])
            else:
                output[head] = [data[elementNo]]
    return output

def manageDictYAML(data, output, header):
    '''This function populates Dictionary content and checks dataype of upcoming data'''
    for element in data:
        head = header + element + "/"
        if isinstance(data[element], list):
            manageListYAML(data[element], output, head)
        elif isinstance(data[element],dict):
            manageDictYAML(data[element], output, head)
        else:
            head = head[:-1]
            if head in output:
                output[head].append(data[element])
            else:
                output[head] = [data[element]]
    return output

def removeTop(data, top):
    '''This function cleans the content till the first dictionary to get better looking csv files'''
    for element in data:
        if isinstance(data, dict) and top:
            data = removeTop(data[element], top)
        else:
            top = False
        return data

def conversionToCsv(data, output):
    '''Function initiates conversion of content fetched from YAML file for CSV file'''
    data = removeTop(data, True)
    if isinstance(data, list):
        manageListYAML(data, output, "")
    else:
        print(type(data))
    return output


def yamlToCsv(filename):
    '''Function to read yaml file and forward for data conversion'''
    output = {}
    try:
        with open(filename, "r", encoding='UTF-8') as file:
            fileData = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)
        sys.exit(1)
    output = conversionToCsv(fileData, output)
    pandas_output = pd.DataFrame(output)
    pandas_output.to_csv("yamlFileCsvOutput.csv", index=False)


def conversionToYaml(data, rows, output):
    '''Function initiates conversion of content fetched from CSV file for YAML file'''
    for row in range(rows):
        val = {}
        for element in data:
            val[element] = data[element][row]
        output.append(val)
    return output

def csvToYaml(filename):
    '''Function to read csv file and forward for data conversion'''
    print("this is csv: "+ filename)
    output = []
    try:
        fileData = pd.read_csv(filename)
    except yaml.YAMLError as exc:
        print(exc)
        sys.exit(1)
    output = conversionToYaml(fileData.to_dict(), len(fileData.index), output)
    with open( "csvFileYamlOutput.yaml" , 'w', encoding='UTF-8' ) as outfile:
        yaml.dump( output , outfile , default_flow_style=False )
