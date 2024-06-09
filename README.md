# CSVYAML

## Purpose
This repository create a creates and deploys an application that can take "YAML" and converts to "CSV" file and vice-versa.

This is done using a python mdoule called "csvYaml" that is packed and then used in the application container


## Application

| Application Name  | Default Port | Language | Description |
| ------------- | ------------- | ------------- | ------------- |
| CSVYAML | 5000 | Python | This is a flask based application that renders a frontend which asks for a file returns the processed file as an interactive link to download output file.  |

## Web App Screenshot

#### App in idle state:
![App - Idle](./readme-asset/appIdle.png)

#### App when file is processed and ready to be downloaded:
![App - Processed](./readme-asset/appProcessed.png)

## CICD Screenshot

#### CICD flow of the application:
![App - Idle](./readme-asset/cicd.png)
#Note: The deployment step waits for manual approval

## Application Flow
