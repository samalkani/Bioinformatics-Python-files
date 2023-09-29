# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:27:05 2022

Functions_2

@author: Ajay_
"""

# Defining the function that checks for Stop Codons

def has_stop_codon(dna):
    
    """This function checks if given dna sequence 
       has in frame stop codons."""
       
    stop_codon_found=False
    stop_codons=['tga','tag','taa']
    for i in range(0, len(dna, 3)):
        codon=dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found=True
            break
    return stop_codon_found

# Defining the function Default values

def has_stop_codon(dna, frame):
    
    """This function checks if given dna sequence 
       has in frame stop codons."""
       
    stop_codon_found=False
    stop_codons=['tga','tag','taa']
    for i in range(frame, len(dna), 3):
        codon=dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found=True
            break
    return stop_codon_found

# Calling has_stop_codon

dna="atgagcggccggct"

has_stop_codon(dna, 0)

has_stop_codon(dna, 1)

# Defining the function with a default value of zero

def has_stop_codon(dna, frame=0):
    
    """This function checks if given dna sequence 
       has in frame stop codons."""
       
    stop_codon_found=False
    stop_codons=['tga','tag','taa']
    for i in range(frame, len(dna), 3):
        codon=dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found=True
            break
    return stop_codon_found

dna="aaatgagcggccggct"

has_stop_codon(dna)

has_stop_codon(dna, 1)




       