## Version LAB 3


import hashlib
import os 

def encoder_function(name):
    cwd = os.getcwd()
    name = cwd + "/" + name
    with open(name) as file:
        archivo = file.read()
        byteString = str.encode(archivo)
    file.close
    mLib = hashlib.sha256()
    mLib.update(byteString)
    return mLib.hexdigest()

def same_hash (ogFile, newFile):
    cwd = os.getcwd()
    result = True
    name1 = cwd + "/" + ogFile
    name2 = cwd + "/" + newFile
    with open(name1) as file1:
        ogFileLines = file1.readlines()
    with open(name2) as file2:
        newFileLines = file2.readlines()
    for i in range(len(ogFileLines)):
        result = result and (ogFileLines[i] == newFileLines[i])
        if not result:
            return False
    result = result and (newFileLines[-1] == encoder_function(ogFile))

    return(result)

def main():
    ogFile = input("Whats the original file? \n")
    newFile = input("Whats the file to be checked? \n")
    result = same_hash(ogFile, newFile)
    text = "File is not correct."
    if result:
        text = "File is correct."
    print(text)
    
main()
