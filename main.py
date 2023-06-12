#!/usr/bin/env python
# coding: utf-8


# Libraries used
import os
import encrypt as enc
import decrypt as dec
import mutation as mut
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend



# Generate a symmetric encryption key for AES
encryption_key = os.urandom(32)

# Generate a random initialization vector (IV)
iv = os.urandom(16)

# Create an AES cipher with CBC mode
cipher = Cipher(algorithms.AES(encryption_key), modes.CBC(iv), backend=default_backend())



# Create variables to store the data
fragments= []
fragmentsc=[]
hash_values= []
datas=[]

# Obtain x=100 different sequences 
for i in range(100):
    
        seq, seq_n, hash, data= enc.random_seq(cipher,i)
        fragments.append(seq_n)
        fragmentsc.append(seq)
        #print(len(fragmentsc[i])) 376
        hash_values.append(hash)
        datas.append(data)

print("A random fragment with key 1 and random data encrypted:\n")
print(fragmentsc[0])
print("\nOriginal data:\n")
print(datas[0])
print("\nConverted to nucleotid:\n")
print(fragments[0])

# Retrieve x=100 sequences
#I have to bin it, extract the data and decrypt it.
data_bin=[]
data=[]
data_array=[]
for i in range(len(fragments)):
        data_bin.append(dec.nuc_to_bin(fragments[i]))
        data.append(dec.sep_data(data_bin[i]))
        data_array.append(dec.decrypt_data(cipher,dec.string2bits(data[i])))

print("\nFragment converted to binary:\n")
print(data_bin[0])
print("\nData decrypted:\n")
print(data_array[0])  

# Check if the data is correctly retrieved
verif=[]
for i in range(len(data_array)):
        byte_data = data_array[i].encode('utf-8')
        enc_data = enc.encrypt_data(cipher, byte_data)
        computed_hash = enc.compute_hash(enc_data)
        verif.append (computed_hash == hash_values[i]) 

print("\nVerification if the hash is correct:\n")
print(verif[0])


  





