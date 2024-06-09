# CSV - YAML

## Project Description
This repository contains a web application that converts between "YAML" and "CSV" file formats. It provides a user-friendly interface for uploading a file, processing it, and downloading the converted file.

## Key Components
**csvYaml Module**: A custom Python module that handles the conversion between YAML and CSV. This module is packaged and used within the application container.

## Features
- **YAML to CSV Conversion**: Upload a YAML file and receive a CSV file.
    - The algorithm is able to convert ".yaml" or ".yml" file to ".csv" format.
- **CSV to YAML Conversion**: Upload a CSV file and receive a YAML file.
    - The algorithm is successfully able to convert ".csv" file to ".yaml" format **up to 2 levels**.

## Technology Stack
- **Backend**: Python with Flask
- **Frontend**: HTML, CSS
- **Containerization**: Docker
- **CICD**: Github Actions

## Application Flow
![App - Idle](./readme-asset/appFlow.png)

#### Directory Structure:
```
csvYaml
├── csvYaml
│   ├── csvYaml
│   │   ├── converterFile.py
│   │   └── __init__.py
│   ├── fetchVersion.py
│   ├── main.py
│   ├── setup.py
│   ├── static
│   │   └── css
│   │       └── style.css
│   ├── templates
│   │   └── index.html
│   └── version.txt
├── docker-compose.yaml
├── Dockerfile
└── requirements.txt
```

#### How It Works
- **Upload**: Users can upload a YAML or CSV file through the web interface.
- **Process**: The application processes the uploaded file using the csvYaml module.
- **Download**: Users can download the converted file from the web interface.
- **File Format Supported**: .yaml, .yml and .csv

#### App in idle state:
![App - Idle](./readme-asset/appIdle.png)

#### App when file is processed and ready to be downloaded:
![App - Processed](./readme-asset/appProcessed.png)

#### csvYaml module usage
```
from csvYaml import converter

output_file = converter(input_file, output_file_directory)

```

## Conversion Example
YAML to CSV : [yamlFile.csv](https://drive.google.com/file/d/1IrLk_TMGDR6hnkMUr0dJr77qOvetve1T/view?usp=sharing) => [yamlFile.csv](https://drive.google.com/file/d/1zyFa64o1pkUVE-fQGR9P_gkgTAhxrgTZ/view?usp=sharing)

CSV  to YAML: [csvFile.csv]() => [csvFile.yaml]()

## CI/CD Flow

#### CI/CD flow of the application:
![App - Idle](./readme-asset/cicdFlowchart.png)

#### CI/CD Github Actions Screenshot
![App - Idle](./readme-asset/cicdGithub.png)
#Note: The pipeline waits for manual approval to perform CD

## Roadmap
- Automatic version upgrade.
- Quality gates for PyLint, Trivy, and Dockle tests.
- CSV to YAML Conversion up to n levels.
- Handle unsupported files.
- Updating CI/CD to make it more modular and scalable to multiple environments.
