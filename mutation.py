#!/usr/bin/env python
# coding: utf-8



import random




seq='AAAGACACAAAATGATTCCTTGCCTCCGTGTCTCGTTGATTGACTGCGTGTATGCCTCTCTCACTCTTTCTATCTTTGCGTGCTTCTCTCCCTCTCTCCCTGCGTCCCAAAG'




def get_pos(leng):
    return random.randint(0,leng)





def nucl():
    ch= random.randint(0,3)
    if ch==0:
        w='A'
    elif ch==1:
        w='C'
    elif ch==2:
        w='G'
    elif ch==3:
        w='T'
    return w



#the type of mutation

def change(seq):
    leng=len(seq)
    pos= get_pos(leng)
    word= nucl()
    seq=  seq[:pos] + word + seq[pos+1:]
    return seq
        
def insert(seq):
    leng=len(seq)
    pos= get_pos(leng)
    word= nucl()
    seq=  seq[:pos] + word + seq[pos:]
    return seq

def delet(seq):
    leng=len(seq)
    pos= get_pos(leng)
    seq=  seq[:pos] + seq[pos+1:]
    return seq

#hamming error
#solo sirve para mismo len (insertion and elimination no sirve)
def errorh( val1, val2): 
    if val1==val2:
        return 0
    count=0
    for i in range(len(val1)):
        if not val1[i] == val2[i]:
            count+=1
    return count




seqc= change(seq)
seqi= insert(seq)
seqd= delet(seq)

#print(len(seqd))

h= errorh(seq, seqc)
#print(h)






