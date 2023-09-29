# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 20:29:22 2022

Functions_3

@author: Ajay_
"""

# Passing arguments by position

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

# Passing arguments by name


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

seq="aaatgagcggccggct"

has_stop_codon(frame=0, dna=seq)

# A More Complex Function Example
# Write a function to reverse complement a DNA sequence

# General format of the function

def reversecomplement(seq):
    """Return the reverse complement of the dna 
    string"""
    
    seq = reverse_string(seq)
    seq = complement(seq)
    return seq

reversecomplement('CCGGAAGAGCTTACTTAG')

# But first you have to define the reverse_string function
# and complement function

# Reversing A String 

# Regular Slices

dna="AGTGTGGGGCG"

dna[0:3]

# Extended Slices

dna[0:3:2]

# Reversing a string using an extended slice and the copy [:] slice

dna[::-1]

# A function to complement a DNA sequence

dna="AGTGTGGGGCG"

def complement(dna):
    """Return the complementary sequence string
    """
    basecomplement = {'A':'T','C':'G','G':'C','T':'A',
                      'N':'N','a':'t','c':'g','g':'c',
                      't':'a','n':'n'}
    
    letters = list(dna)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)

dna
complement(dna)

# Split and join

sentence="enzymes and other proteins come in many shapes"

sentence.split()

sentence.split('and')

'-'.join(['enzymes', 'and', 'other', 'proteins', 'come', 'in', 'many', 'shapes'])

# Variable Number Of Function Argument

def newfunction(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... ", therest)
    return

newfunction(1,2,3,4,5,6,7,8,9)

# Finished Function

def complement(seq):
    """Return the complementary sequence string
    """
    basecomplement = {'A':'T','C':'G','G':'C','T':'A',
                      'N':'N','a':'t','c':'g','g':'c',
                      't':'a','n':'n'}
    
    letters = list(seq)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)

complement(seq)

def reverse_string(seq):
    return seq[::-1]

reverse_string(seq)

def reversecomplement(seq):
    """Return the reverse complement of the dna 
    string"""
    
    reverse_string(seq)
    complement(seq)
    
    return complement
    


seq='CCGGAAGAGCTTACTTAG'
    
reversecomplement(seq)


