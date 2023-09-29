# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:07:34 2022

Functions_1

@author: Ajay_
"""
# A Function To Compute The GC Percentage Of A DNA Sequence

# Input: sequence

# Output: GC percentage

def gc(dna):
    "This function computes the GC percentage of a dna sequence"
    nbases=dna.count('n')+dna.count('N')
    gcpercent=float(dna.count('c')+dna.count('C')+dna.count('g')
                    +dna.count('G'))*100.0/(len(dna)-nbases)
    return gcpercent

gc('AAAGTNNAGTCC')

help(gc)

print(nbases)
