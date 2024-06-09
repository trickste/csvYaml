"""
Converter file to initialize module
"""
# pylint: disable=C0103, E0401, C0301
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


def yamlToCsv(input_file, output_path):
    '''Function to read yaml file and forward for data conversion'''
    output = {}
    try:
        with open(input_file, "r", encoding='UTF-8') as file:
            fileData = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)
        sys.exit(1)
    output = conversionToCsv(fileData, output)
    pandas_output = pd.DataFrame(output)
    output_file = outputFileNameConversion(input_file, "csv")
    pandas_output.to_csv(output_path + "/" + output_file, index=False)
    return output_file


def manageDictCSV(elementList, data, output, row):
    '''This function populates Dictionary content and checks dataype of upcoming data'''
    print("dict: "+str(elementList))
    if len(elementList) == 1:
        output[elementList[0]] = data[row]
    else:
        if elementList[1].isdigit():
            output[elementList[0]] = manageListCSV(elementList[1:], data, [], row)
        else:
            output[elementList[0]] = manageDictCSV(elementList[1:], data, output, row)
    return output


def manageListCSV(elementList, data, output, row):
    '''This function populates List content and checks dataype of upcoming data'''
    print("list: "+str(elementList))
    if len(elementList) == 1:
        output.append(data[row])
        # return data[row]
    else:
        if elementList[1].isdigit():
            output.append(manageListCSV(elementList[1:], data, output, row))
        else:
            output.append(manageDictCSV(elementList[1:], data, {}, row))
    return output


def conversionToYaml(data, rows, output):
    '''Function initiates conversion of content fetched from CSV file for YAML file'''
    for row in range(rows):
        val = {}
        localList = []
        for elements in data:
            elementList = elements.split("/")
            if len(elementList) == 1:
                val[elements] = data[elements][row]
            else:
                if elementList[1].isdigit():
                    val[elementList[0]] = manageListCSV(elementList[1:], data[elements], localList, row)
                else:
                    val[elementList[0]] = {}
        output.append(val)
    return output

def csvToYaml(input_file, output_path):
    '''Function to read csv file and forward for data conversion'''
    output = []
    try:
        fileData = pd.read_csv(input_file)
    except yaml.YAMLError as exc:
        print(exc)
        sys.exit(1)
    output = conversionToYaml(fileData.to_dict(), len(fileData.index), output)
    output_file = outputFileNameConversion(input_file, "yaml")
    with open( output_path + "/" + output_file, 'w', encoding='UTF-8' ) as outfile:
        yaml.dump( output , outfile , default_flow_style=False )
    return output_file


def outputFileNameConversion(input_file, ext):
    '''This Function is changing output file extension'''
    filename = input_file.split("/")[-1]
    filename = filename.split(".")
    filename[-1] = ext
    return ".".join(filename)
