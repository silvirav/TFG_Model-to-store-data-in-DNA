#!/usr/bin/env python
# coding: utf-8

# Libraries used
from cryptography.hazmat.primitives import padding
import base64



# Function to separate data from a sequence
def sep_data(seq):
    # Select indices 16 to 367 from the given sequence
    data=seq[16:368] # I you change the leght of its part in the encode, this has to be modify
    return data
        


# Function to convert nucleotides to binary
def nuc_to_bin(nuc):
    i=0
    bina=''
    while i < len(nuc):
        if (nuc[i]=='A'):  #00 = A
            bina+='00'
        elif (nuc[i]=='T') : #01 = T
            bina+='01'
        elif (nuc[i]=='C'): #10 = C
            bina+='10'  
        elif (nuc[i]=='G') : #11 = G
            bina+='11'  
        i+=1
    
    return bina



# Function to convert bits to string
def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])



# Function to convert string to bits
def string2bits(data):
    return bytes(int(data[i:i+8], 2) for i in range(0, len(data), 8))



# ERROR CORRECTION
# Function to calculate hamming error
def errorh( val1, val2):  # here it is assumed that both have the same size
    if val1==val2:
        return 0
    count=0
    for i in range(len(val1)):
        if not val1[i] == val2[i]:
            count+=1
    return count



# Function to decrypt data using AES
def decrypt_data(cipher,encrypted_data):
    encrypted_data_bytes = base64.b64decode(encrypted_data) # decode the encrypted data from base64
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data_bytes) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data.decode('utf-8') # return the decrypted data in utf-8 format




