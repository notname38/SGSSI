import hashlib
import os 
import time
import secrets

def random_hex(filler_len, extr):
    rand_hex_str = "1"
    while len(rand_hex_str) < filler_len:
        # Garantizamos un HEX random de longitud grande.
        rand_hex_str = secrets.token_hex(15)
    # Identificador ACT 1.3
    return rand_hex_str[:filler_len] + extr
    
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

def copy_write_to_file(input_text, name, list_input = False):
    cwd = os.getcwd()
    name = cwd + "/" + name
    with open(name) as f:
        contenido = f.readlines()
    f.close
    with open("output.txt", "w") as file:
        for line in contenido:
            file.write(line)
        if list_input:
            for elem in input_text:
                file.write(elem)
                file.write("\n")
        else:
            file.write(input_text)
    file.close

def contarZeros(input_text):
    cont = 0
    for elem in input_text:
        if elem != "0":
            break
        cont = cont + 1
    return cont

def cycle_to_most_zero_hash(minutes, filler_len, extr, name = "ask_for_name"):
    if name == "ask_for_name":
        name = input("Please type the file to be mined (must be in the same folder). \n")

    timeout = time.time() + 60*minutes

    current_hex = random_hex(filler_len, extr)
    best_hex = current_hex

    copy_write_to_file(current_hex, name)
    current_hash = encoder_function("output.txt")
    best_hash = current_hash

    while True:
        print("Tried hex ", current_hex, " for sha256 ", current_hash)
        current_hex = random_hex(filler_len, extr)
        copy_write_to_file(current_hex, name)
        current_hash = encoder_function("output.txt")
        new_zeros = contarZeros(current_hash)
        best_zeros = contarZeros(best_hash)

        if new_zeros > best_zeros:
            best_hash = current_hash
            best_hex = current_hex
        if (time.time() > timeout):
            break

    print("Found SHA 256 ", best_hash, "for HEX ", best_hex)
    end_result = [best_hex, best_hash]
    copy_write_to_file(end_result, name, list_input=True)

def main():
    #endName = "mining_result.txt"
    lenFiller = int(input("How long should the filler be? \n"))
    extr = input("Should any extra string be added to the filler? \n")
    mins = int(input("How many minutes shall the program run? \n"))
    cycle_to_most_zero_hash(mins, lenFiller, extr)
    
main()
