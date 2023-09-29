# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 20:07:03 2022

@author: Ajay_
"""
# Create dna sequence in a fasta file

f=open(r'C:/Users/Ajay_/OneDrive/Documents/Python_Scripts/myseq1.fa', 'w')


# In newly created file add the dna sequence provided

# Example of using biopython to solve a problem

# Problem - Find out from what species an unknown
# DNA sequence came from see myseq.fa 

# The program below may take some time to run quite complex

from Bio.Blast import NCBIWWW 
fasta_string = open(r"C:\Users\Ajay_\OneDrive\Documents\Python_Scripts\myseq1.fa").read()
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


from Bio.Seq import Seq

data='AGGCTGAAAG'

my_seq=Seq(data)

print(my_seq)


print('reverse complement is %s' % reverse(my_seq.complement()))

print('reverse complement is %s' % my_seq.reverse_complement())

print('reverse complement is %s' % complement(my_seq))

print('reverse complement is %s' % complement(my_seq.reverse()))


# question 5

data = """TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTACAATTAGGACCTCGATATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCTTCTCATTCTTCTTTGGCACCTACGGTAGAG"""
data = data.rstrip()

print(data)

from Bio.Seq import Seq
coding_dna = Seq(data)
coding_dna.translate()


help(Seq)








