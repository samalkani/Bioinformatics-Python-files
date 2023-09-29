# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:33:59 2022

#! /usr/bin/python

@author: Ajay_
"""

# define has_stop_codon function here

dna=input("Enter a DNA sequence, please: ")

if(has_stop_codon(dna)):
    print("Input sequence has an in frame stop codon.")
else:
    print("Input sequence has no in frame stop codons.")