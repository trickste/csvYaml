# CSV - YAML

## Project Decscription
This repository contains a Web application that converts between "YAML" and "CSV" file formats. It provides a user-friendly interface for uploading a file, processing it, and downloading the converted file.

## Key Components
**csvYaml Module**: A custom Python module that handles the conversion between YAML and CSV. This module is packaged and used within the application container.

## Features
- **YAML to CSV Conversion**: Upload a YAML file and receive a CSV file.
    - The algorithm is able to convert ".yaml" or ".yml" file to ".cvs" format.
- **CSV to YAML Conversion**: Upload a CSV file and receive a YAML file.
    - The algorithm is successfully able to convert ".csv" file to ".yaml" format up to 2 levels.

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

## CI/CD Flow

#### CI/CD flow of the application:
![App - Idle](./readme-asset/cicdFlowchart.png)

#### CI/CD Github Actions Screenshot
![App - Idle](./readme-asset/cicdGithub.png)
#Note: The pipeline waits for manual approval to perform CD

## Conversion Example

#### Sample yaml File: yamlFile.yaml
```
    instances:
- host: 173.20.1.1
  timeout: 1.0
  tags:
  - ip:173.20.1.1
  - env:prod
  - type:virtual
  - name:2-base
  - hardware:server
  - testval:
    - val11
    - val12
    - val13
- host: 174.28.2.2
  timeout: 1.0
  tags:
  - ip:174.28.2.2
  - env:prod
  - type:virtual
  - name:2-game
  - hardware:server
  - testval:
    - val21
    - val22
    - val23
- host: 174.28.32.8
  timeout: 1.0
  tags:
  - ip:174.28.32.8
  - env:prod
  - type:virtual
  - name:2-play
  - hardware:server
  - testval:
    - val31
    - val32
    - val33
```

#### Output File:
```
host,timeout,tags/0/ip,tags/1/env,tags/2/type,tags/3/name,tags/4/hardware,tags/5/testval/0,tags/5/testval/1,tags/5/testval/2
173.20.1.1,1.0,173.20.1.1,prod,virtual,2-base,server,val11,val12,val13
174.28.2.2,1.0,174.28.2.2,prod,virtual,2-game,server,val21,val22,val23
174.28.32.8,1.0,174.28.32.8,prod,virtual,2-play,server,val31,val32,val33
```


## Roadmap
- Automatic Version upgrade
- Threashold gateway for PyLint, trivy and dockle tests
- Better CSV to YAML Conversion
- Handle Unsupported files
- Updating CICD to make it mode modular to scale it to multiple environments.
