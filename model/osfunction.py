import os

def path_change():
    path = 'C:/Users/amer/OneDrive/Backup'
    os.chdir(path)
    print("Current Working Directory " , os.getcwd())

