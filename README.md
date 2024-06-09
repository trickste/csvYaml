# CSV - YAML

## Project Description
This repository contains a web application that converts between "YAML" and "CSV" file formats. It provides a user-friendly interface for uploading a file, processing it, and downloading the converted file.

## Key Components
**csvYaml Module**: A custom Python module that handles the conversion between YAML and CSV. This module is packaged in a wheel file and used within the application container.

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

#### App when file is file uploaded is of wrong extension:
![App - Wrong Extension file](./readme-asset/appWrongFile.png)

#### csvYaml module usage
```
from csvYaml import converter

output_file = converter(input_file, output_file_directory)

```

## Conversion Example
YAML to CSV : [yamlFile.csv](https://drive.google.com/file/d/1IrLk_TMGDR6hnkMUr0dJr77qOvetve1T/view?usp=sharing) => [yamlFile.csv](https://drive.google.com/file/d/1zyFa64o1pkUVE-fQGR9P_gkgTAhxrgTZ/view?usp=sharing)

CSV to YAML: [csvFile.csv](https://drive.google.com/file/d/1fET8jULu2Ow63_LCwxxgc72AlmNCzhK9/view?usp=sharing) => [csvFile.yaml](https://drive.google.com/file/d/18bLp37T-jMvvG9WGjjO8_CH-FGK7-Gr7/view?usp=sharing)

## CI/CD Flow

#### CI/CD flow of the application:
![App - Idle](./readme-asset/cicdFlowchart.png)

#### CI/CD Github Actions Screenshot
![App - Idle](./readme-asset/cicdGithub.png)

#### Note: 
- The pipeline waits for manual approval to perform CD.
- Github Runners are installed on my local machine to run the pipeline.
- Docker container for the application is deployed on my local machine.

## Roadmap
- Automatic version upgrade.
- Quality gates for PyLint, Trivy, and Dockle tests.
- CSV to YAML Conversion up to n levels.
- Updating CI/CD to make it more modular and scalable to multiple environments.
- Add Healthcheck for application
- Updadte Dockerfile to make image more secure
