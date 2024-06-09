# CSV - YAML

## Project Decscription
This repository contains a Web application that converts between "YAML" and "CSV" file formats. It provides a user-friendly interface for uploading a file, processing it, and downloading the converted file.


## Features
- YAML to CSV Conversion: Upload a YAML file and receive a CSV file.
- CSV to YAML Conversion: Upload a CSV file and receive a YAML file.
    - The algorithm is successfully able to convert ".csv" file to ".yaml" format up to 2 levels.

## Technology Stack
- Backend: Python with Flask
- Frontend: HTML, CSS
- Containerization: Docker
- CICD: Github Actions

## Key Components
**csvYaml Module**: A custom Python module that handles the conversion between YAML and CSV. This module is packaged and used within the application container.

## How It Works
- Upload: Users can upload a YAML or CSV file through the web interface.
- Process: The application processes the uploaded file using the csvYaml module.
- Download: Users can download the converted file from the web interface.
- File Format Supported: **.yaml**, **.yml**, **.csv**


### Application Flow
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

<!-- ## Application

| Application Name  | Default Port | Language | Description |
| ------------- | ------------- | ------------- | ------------- |
| CSVYAML | 5000 | Python | This is a flask based application that renders a frontend which asks for a file returns the processed file as an interactive link to download output file.  | -->

#### App in idle state:
![App - Idle](./readme-asset/appIdle.png)

#### App when file is processed and ready to be downloaded:
![App - Processed](./readme-asset/appProcessed.png)

### CI/CD Flow

#### CI/CD flow of the application:
![App - Idle](./readme-asset/cicdFlowchart.png)

#### CI/CD Github Actions Screenshot
![App - Idle](./readme-asset/cicdGithub.png)
#Note: The pipeline waits for manual approval to perform CD


