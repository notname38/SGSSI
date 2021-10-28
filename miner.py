import hashlib
import os 
import time
import secrets
import datetime
import math
#from timeit import default_timer as timer
#from tqdm import tqdm

def random_hex(filler_len, extr):
    rand_hex_str = "1"
    while len(rand_hex_str) < filler_len:
        rand_hex_str = secrets.token_hex(15)
    return rand_hex_str[:filler_len] + extr
    
def encoder_function(text):
    byteString = str.encode(text)
    mLib = hashlib.sha256()
    mLib.update(byteString)
    return mLib.hexdigest()

def contarZeros(input_text):
    cont = 0
    for elem in input_text:
        if elem != "0":
            break
        cont = cont + 1
    return cont

def read_file(name):
    cwd = os.getcwd()
    name = cwd + "/" + name
    with open(name) as f:
        content = f.read()
    f.close
    return content

def write_file(content,nzeros):
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    filename = str(nzeros) + "_zeros_output_" + timestamp
    with open(filename, "w") as file:
        file.write(content)
    file.close

def cycle_to_most_zero_hash(minutes, filler_len, extr, name):
    try:
        itTimes = 0
        itMax = 0
        itMin = math.inf
        it = 0
        content = read_file(name)
        if content[-1:] != "\n":
           content = content + "\n"

        current_hex = random_hex(filler_len, extr)
        best_hex = current_hex

        current_hash = encoder_function(content+current_hex)
        best_hash = current_hash
        
        nanoTimeout = 60*minutes*1000000000
        timeout = time.time_ns() + nanoTimeout


        print("\n")
        #print("Expected miner timeout time: ", timeout/1000000000)
        #print("Current miner time: ", time.time_ns()/1000000000)
        now = datetime.datetime.now()
        print("Program start time: ", now.hour,":",now.minute,":",now.second)
        print("Expected program duration: ", (timeout - time.time_ns())/1000000000) 
        print("\n")
        
    
        while (time.time_ns() <= timeout):
            it = it + 1
            it_start = time.time_ns()
            current_hex = random_hex(filler_len, extr)
            current_hash = encoder_function(content+current_hex)
            new_zeros = contarZeros(current_hash)
            best_zeros = contarZeros(best_hash)

            if new_zeros > best_zeros:
                best_hash = current_hash
                best_hex = current_hex
                now = datetime.datetime.now()
                itBestHash = it
                print("Found hash with ", contarZeros(best_hash), " zeros at ", now.hour,":",now.minute,":",now.second, " in iteration ", it)


            it_end = time.time_ns()
            itTimes = itTimes + ((it_end-it_start)/1000000000)
            itMax = max(itMax, (it_end-it_start))
            itMin = min(itMin, (it_end-it_start))
 


        print("\n")
        print("End report:")
        now = datetime.datetime.now()
        print("Program end time: ", now.hour,":",now.minute,":",now.second)
        print("Real run time: ", itTimes, " Number of iterations: ", it)
        print("Best Hash: ", best_hash, " with ", contarZeros(best_hash), " zeros.")
        print("Final filler:  ", best_hex, ". Iterations without improvement: ", it-itBestHash)
        print("Max iteration time: ", itMax/1000000000, " Fastest iteration time: ", itMin/1000000000)
        print("Average iteration time: ",  (itTimes/it)/1000000000)

        write_file(content + best_hex, contarZeros(best_hash))

    except KeyboardInterrupt:
        print("Miner interrupted.")
        print("Best Found Hash: ", best_hash, " with ", contarZeros(best_hash), " zeros for filler ", best_hex)

def main():
    lenFiller = int(input("How long should the filler be? \n"))
    extr = input("Should any extra string be added to the filler? \n")
    mins = int(input("How many minutes shall the program run? \n"))
    name = input("Please type the file to be mined (must be in the same folder). \n")
    cycle_to_most_zero_hash(mins, lenFiller, extr, name)
    
main()
