# -*- coding: utf-8 -*-
"""
Created on Sun May 29 17:20:35 2022

Find the donor splice site of a DNA sequence

@author: Ajay_
"""

dna=input('Enter DNA sequence: ')

pos=dna.find('gt', 0) # position of donor splice site

while pos>-1 :
    
    print("Donor splice site candidate at position %d" % pos)
    
    pos=dna.find('gt', pos+1)