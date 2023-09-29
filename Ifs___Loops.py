# -*- coding: utf-8 -*-
"""
Created on Sat May 28 15:13:36 2022

Ifs and Loops

@author: Ajay_
"""

# The if Statement

dna=input('Enter DNA sequences:')

if 'n' in dna:
    
    nbases=dna.count('n')
    
    print("dna sequence has %d undefined bases " % nbases)
    
# Boolean Expressions, use;
# Comparison, Identity and Membership operators

0<1

len('atgcgt')>=10

# Comparison operators

'a' == 'A'

'GT' != 'AG'

'A' < 'C'

10+1 == 11

# Membership operators

motif = 'gtccc'

dna = 'atatattgtcccattt'

motif in dna

# Identity Operators

alphabet=['a','c','g','t']

newalphabet=alphabet[:] # Copy of alphabet object

alphabet == newalphabet # == operator signifies all elements
                        # of object are the same

alphabet is newalphabet # is operator indicates they are 
                        # not the same object


# For Loops

motifs=["attccgt","agggggtttttcg","gtagc"]

for m in motifs:
    print(m, len(m))
    
# The range function with for loop

for i in range(4):
    print(i)
    
for i in range(1, 10, 2):
    print(i)
    
motifs=["attccgt","agggggtttttcg","gtagc"]

for i in range(len(motifs)):
    print("Element:", i, "Sequence:", motifs[i], "length:", len(motifs[i]))
    
# Using the range function to validate a protein sequence
# of amino acids

protein='SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'

for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ' :
        print("protein contains invalid amino acid %s at position %d" %(protein[i], i))

# Breaking Out Of Loops - if you only want to find out whether
# the protein sequence is valid.

protein='SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'

for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ' :
        print("This is not a valid protein sequence!")
        break

# Using Continue statement to move on to 
# the next character in the sequence

protein='SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'
corrected_protein=''

for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ' :
        continue
    corrected_protein=corrected_protein+protein[i]

print("Protein:%s" % protein)    
print("Corrected protein:%s" % corrected_protein)


# Example of using ELSE with a FOR LOOP

N=10
for y in range(2, N):
    print(y)
    for x in range(2, y):
        print(y, x)
        if y % x == 0:
            print(y, 'equals', x, '*', y//x)
            break
    else:
        # loop fell through without finding a factor
        print(y, 'is a prime number')
        















 
    







