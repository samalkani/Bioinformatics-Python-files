# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 15:16:18 2022

Fasta file

@author: Ajay_
"""

# Open file

try:
    f=open(r'C:/Users/Ajay_/OneDrive/Documents/Python_Scripts/upstream10.fa', 'r')
except IOError:
    print("File myfile.fa does not exist!!")
    

    
# Reading the FASTA file

seqs={}
for line in f:    
    # let's discard the newline at the end (if any)
    line=line.rstrip()
    # distinguish header from sequence
    if line[0]=='>':
        words=line.split() # splits the words in the line into elements of a list
        name=words[0][1:] # the 1st word [0] in the list is the name - '>' sign [1:]
        seqs[name]='' # initialize the name of the sequence to be an empty string
    else:
        seqs[name]=seqs[name]+line # dna sequence    
f.close()

# Retrieving data from dictionaries

for name, seq in seqs.items():
    print(name, seq)

# Command Line Arguments

import sys
print(sys.argv)
