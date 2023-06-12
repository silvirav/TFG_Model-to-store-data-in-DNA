#!/usr/bin/env python
# coding: utf-8


# Libraries used:

import random
import string
from cryptography.hazmat.primitives import padding
import hashlib
import base64


# This function generates a random string for the given length, only with lowercase letters
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str



# This function returns a binary string of length 8 corresponding to the integer 'count'
def get_key_value(count):
    key=format(count, 'b') 
    if len(key)<8:
        n_key= key.zfill(8)
        return n_key
    else:
        return key
    


# This function returns a binary string of length 4 corresponding to the number of ones in the binary string 'key'
def num_ones(key):
    count=0
    for i in key:
        count+= int(i)
    n_count=format(count, 'b')
    n_count= str(n_count).zfill(4)
    return n_count
    


# This function returns a list of binary strings of length 8 representing the ASCII values of each character in the input string 's'
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]



# This function converts a list of binary strings of length 2 into a corresponding DNA sequence
def bin_to_nucl(binar):
    i=0
    nucl=''
    while i < len(binar):
        if (binar[i]=='0')  & (binar[i+1]=='0'):  #00 = A
            nucl+='A'
        elif (binar[i]=='0')  & (binar[i+1]=='1') : #01 = T
            nucl+='T'
        elif (binar[i]=='1')  & (binar[i+1]=='0') : #10 = C
            nucl+='C'  
        elif (binar[i]=='1')  & (binar[i+1]=='1'): #11 = G
            nucl+='G'  
        i+=2
    return nucl
    


# This function encrypts the data using the given cipher and returns the encrypted data
def encrypt_data(cipher, data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return encrypted_data



# Function to compute the SHA-256 hash of data
def compute_hash(data):
    hash_object = hashlib.sha256(data)
    return hash_object.digest()



# This function returns a DNA sequence, a hash value, and a random string, generated using the given cipher and an integer 'count'
def random_seq(cipher,count):
    key= get_key_value(count) 
    data=get_random_string(30)

    # Convert the string to bytes using UTF-8 encoding
    byte_data = data.encode('utf-8')
    enc_data = encrypt_data(cipher, byte_data)
    encr_data_str = base64.b64encode(enc_data).decode('utf-8')
    
    dataB= string2bits(encr_data_str )  
    ones= num_ones(key) 

    
    hash_val = compute_hash(enc_data)
    seq= key+ones+ ones 
    for i in dataB:
        seq+=i

    seq+=key
    return seq, bin_to_nucl(seq), hash_val, data  
        



# To convert it from binary to nucleotide, every two digits are replaced by a letter, so the length of the sequence is divided in two.


"""
def num_CG(seq):
    count=0
    for i in range(len(seq)):
        try:
            if ('C'==seq_n[i]) & ('G'==seq_n[i+1] ):
                       count+=1
        except:
            pass
    return count

#cg= num_CG(seq)
#print(cg)
"""


# Function to encrypt data using AES
# Because the data to be encrypted must be a multiple of the block size for AES. To handle data of varying lengths, I use padding to ensure it meets the required length.




