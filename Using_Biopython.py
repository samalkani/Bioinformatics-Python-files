# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:59:48 2022

Using Biopython

@author: Ajay_
"""
# Use command below to install biopython on Anaconda
# conda install -c conda-forge biopython

import Bio
print(Bio.__version__)

# Example of using biopython to solve a problem

# Problem - Find out from what species an unknown
# DNA sequence came from see myseq.fa 

# The program below may take some time to run quite complex

from Bio.Blast import NCBIWWW 
fasta_string = open(r"C:\Users\Ajay_\OneDrive\Documents\Python_Scripts\myseq.fa").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

# Accessing Help

help(NCBIWWW)

# Looking at the Blast record

from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)

# Parsing BLAST Output

len(blast_record.alignments)

E_VALUE_THRESH = 0.01
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)
            







