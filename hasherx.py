import hashlib
import os
import pyfiglet                                                                                             import time

def Banner():
    time.sleep(0.5)
    os.system("figlet Hasher-X")                                                                                print("------------------------------------------------------------------------------")
    print("                               (V1.0)")
    print("                               Github: midotech1")
    print("                               Instagram: @hackerman_zx_1")
    print("------------------------------------------------------------------------------")
    time.sleep(0.5)
    print("")
Banner()
#Input string
string = input("Input String : ")
print("------------------------------------------------------------------------------")
#Create a SHA-256 hash object
hash_object = hashlib.sha256()

#Update the hash object with the input string (encoded as bytes)
#hash_object.update(string.encode())

#Get the hexadecimal representation of the hash
hex_dig = hash_object.hexdigest()
print("------------------------------------------------------------------------------")
print(f"SHA-256 Hash: {hex_dig}")
file_name = 'output.txt'

#Open the file in write mode
with open(file_name, 'w') as file:                                                                              # Write the input string to the file
    file.write(hex_dig)
print("------------------------------------------------------------------------------")
print(f"The string has been saved to : {file_name}")
print("------------------------------------------------------------------------------")




