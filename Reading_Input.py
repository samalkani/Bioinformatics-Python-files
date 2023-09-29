# -*- coding: utf-8 -*-
"""
Created on Tue May 24 21:51:01 2022

Reading Input

@author: Ajay_
"""

# Reading in a string into dna 

dna = input("Enter a DNA sequence, please: ")

# print value of dna

print(dna)

# Reading in a number into my_number

my_number = input("Please enter a number: ")

# print value of my_number

print(my_number)

# What is the type of the variable my_number

type(my_number)

# Coverting a string to a number

actual_number=int(my_number)

# What is the type of the variable actual_number

type(actual_number)

# Using the CHR function

chr(65)

# Fancier Formatting using the variable GC_PERC

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

print("The DNA sequence's GC content is",gc_percent, "%")

# formatting gc_percent to three decimal places only

print("The DNA sequence's GC content is %5.3f %%" % gc_percent)

# 10.6 is first transformed into an integer

print("%d" % 10.6)

# notice the space in front of 10

print("%3d" % 10.6)

# use %o for an octal/%x for a hexadecimal integer

print("%o" % 10)

# 'E' notation uses powers of 10

print("%e" % 10.6)

# printing a string

print("%s" % dna)

print(dna)

type(0x12)
type(1.)
type(1e10)
