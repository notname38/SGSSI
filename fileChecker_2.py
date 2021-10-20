## Version lab 5

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
    
    # both files have the same information.
    for i in range(len(ogFileLines)):
        result = result and (ogFileLines[i] == newFileLines[i])
        if not result:
            return False

    # How does this work?
    # We need to check if the newFile or the file to be tested has, in its last line,
    # a filler with at least 8 characters, plus a small sequence showing thr group it belongs to.
    # This small sequence will always be at least of size 3 (G01, G02...), plus a blank character in the 
    # middle. Thus the total length of the sequence will always be 8+3+1=12 or more. 
    # Then the only thing we need to check is if the length is correct and that space followed by G
    # is in the line.
    result = result and (len(newFileLines[-1]) >= 12) and (" G" in newFileLines[-1])

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
