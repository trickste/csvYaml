from setuptools import setup, find_packages

with open('csvYaml/csvYaml/version.txt', 'r', encoding='UTF-8') as file:
    version = file.read() 

setup(
    name="csvYaml",
    author="Nishant Prakash",
    author_email="nishantprakashsaini285@gmail.com",
    version=version,
    packages=find_packages(),
)