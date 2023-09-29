# -*- coding: utf-8 -*-
"""
Created on Thu May 26 21:44:24 2022

Tuples, Sets & Dictionaries

@author: Ajay_
"""
# Tuples - Without parentheses

t=1,2,3
t

# Tuples - With parentheses

t=(1,2,3)
t

# Sets are lists with no duplicate entries

brca1={'DNA repair','zinc ion binding','DNA binding',
       'ubiquitin-protein transferase activity','DNA repair',
       'protein ubiquitination'}

brca1

brca2={'protein binding','H4 histone acetyltransferase activity',
       'nucleoplasm','DNA repair','double-strand break repair',
       'double-strand break repair via homologous recombination'}

brca2

# Union operation | combines the annotation 
# terms of both brca1 and brca2

brca1 | brca2

# Use the & (and) operation to find out which terms are in common
# in both brca1 and brca2

brca1 & brca2

# Terms associated with brca1 but NOT in brca2

brca1 - brca2

# Dictionaries

TF_motif = {'SP1':'gggcgg',
 'C/EBP':'attgcgcaat',
 'ATF':'tgacgtca',
 'c-Myc':'cacgtg',
 'Oct-1':'atgcaaat'}

# Accessing Dictionary values

print("The recognition sequence for the ATF trancription is %s" 
      % TF_motif['ATF'])

# Accessing Dictionary values with where there is no corresponding
# dictionary key gives an error

print("The recognition sequence for the NF-1 trancription is %s" 
      % TF_motif['NF-1'])

# Checking whether a key is present in a dictionary

'NF-1' in TF_motif

# Adding a new key:value pair to the dictionary

TF_motif['AP-1']='tgagtca'
TF_motif

# Modifying an existing entry

TF_motif['AP-1']='tga(g/c)tca'
TF_motif

# Delete a key from the dictionary

del TF_motif['SP1']
TF_motif

# Adding another dictionary (multiple key:value pairs) 
# to the current one

TF_motif.update({'SP1':'gggcgg', 'C/EBP':'attgcgcaat',
                 'Oct-1':'atgcaaa'})
TF_motif

# Finding out the length of a dictionary

len(TF_motif)

# List all the keys in the dictionary

list(TF_motif.keys())

# Sorted list of keys from the dictionary

sorted(TF_motif.keys())

# Sorted list of values from the dictionary

sorted(TF_motif.values())



 
 