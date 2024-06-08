import os
def getversion():
    '''Function to fetch version'''
    os.system("ls")
    with open('csvYaml/version.txt', 'r', encoding='UTF-8') as file:
        version = file.readlines()
    return version[-1]

if __name__ == '__main__':
    print(getversion())