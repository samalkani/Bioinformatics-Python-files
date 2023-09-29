# -*- coding: utf-8 -*-
"""
Created on Sat May 28 15:57:45 2022

Check_dna.py

@author: Ajay_
"""

# Using Else statement with the if statement

dna=input('Enter DNA sequences:')

if 'n' in dna:
    
    nbases=dna.count('n')
    
    print("dna sequence has %d undefined bases " % nbases)
    
else:
    
    print("dna sequence has no undefined bases")
    
# Using Elif statement with the if & else statement

dna=input('Enter DNA sequences:')

if 'n' in dna:
    
    print("dna sequence has undefined bases ")
    
elif 'N' in dna:
    
    print("dna sequence has undefined bases ")
    
else:
    
    print("dna sequence has no undefined bases")
    
# Using logical operators to count the number of undefined bases,
# whether its 'n' or 'N'

dna=input('Enter DNA sequences:')

if 'n' in dna or 'N' in dna:
    
    nbases=dna.count('n') + dna.count('N')
    
    print("dna sequence has %d undefined bases " % nbases)
    
else:
    
    print("dna sequence has no undefined bases")
    
    
    
    