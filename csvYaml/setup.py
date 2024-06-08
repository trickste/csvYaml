'''
The configuration file for packaging 
'''
from setuptools import setup, find_packages

with open('version.txt', 'r', encoding='UTF-8') as file:
    version = file.readlines()

setup(
    name="csvYaml",
    author="Nishant Prakash",
    author_email="nishantprakashsaini285@gmail.com",
    version=version[-1],
    packages=find_packages(),
)
