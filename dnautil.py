# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 17:38:50 2022

Modules_&_Packages 

The dnautil.py Module

dnauntil module contains a few useful functions for dna sequence

@author: Ajay_
"""

def gc(dna):
    "This function computes the GC percentage of a dna sequence"
    nbases=dna.count('n')+dna.count('N')
    gcpercent=float(dna.count('c')+dna.count('C')+dna.count('g')
                    +dna.count('G'))/(len(dna)-nbases)
    return gcpercent

def has_stop_codon(dna,frame):
    """This function checks if given dna sequence 
    has in frame stop codons"""
    
    stop_codon_found=False
    stop_codons=['tga','tag','taa']
    for i in range(frame, len(dna), 3):
        codon=dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found=True
            break
    return stop_codon_found