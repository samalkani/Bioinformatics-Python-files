# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:52:40 2022

This is my first Python program.
It computes the GC content of the DNA sequence

@author: Ajay_
"""

# read DNA sequence from user

dna = 'acgctcgcgcggcgatagctgatcgatcggcgcgctttttttttaaaag'

# count the number of C's in the DNA sequence

no_c=dna.count('c')

# count the number of G's in the DNA sequence

no_g=dna.count('g')

# determine the length of the DNA sequence

dna_length=len(dna)

# compute the GC%

gc_percent=(no_c+no_g)*100.0/dna_length

# print GC%

print(gc_percent)




