# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 17:53:21 2022

processfasta.py builds a dictionary with all sequences from a FASTA file

@author: Ajay_
"""

# Importing sys module into our program

import sys
import getopt
filename=sys.argv[1]


# Usage Definition For processfasta.py

def usage():
    print("""
    processfasta.py : reads a FASTA file and builds a dictionary with all sequences bigger than
    a given length
    
    processfasta.py [-h] [-l <length>] <filename>
    
    -h               print this message
    
    -l <length>      filter all sequences with a length smaller than <length>
                    (default <length>=0)
                    
    <filename>       the file has to be in FASTA format
    """)
    
o, a = getopt.getopt(sys.argv[1:], 'l:h')
opts = {}
seqlen = 0;

for k,v in o:
    opts[k] = v
if '-h' in opts.keys():
    usage(); sys.exit()
if len(a) < 1:
    usage(); sys.exit("input fasta file is missing")
if '-l' in opts.keys():
    if int(opts['l'])<0:
        print("Length of sequence should be positive!"); sys.exit(0)
    seqlen=opts['-l']

# Open file

try:
    f=open(r'C:/Users/Ajay_/OneDrive/Documents/Python_Scripts/upstream1000.fa', 'r')
except IOError:
    print("File %s does not exist!!" % filename)
    
  
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