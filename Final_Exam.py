# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:27:14 2022

Final Exam

@author: Ajay_
"""
# Open file

try:
    f=open(r'C:/Users/Ajay_/OneDrive/Documents/Python_Scripts/dna2.fasta', 'r')
except IOError:
    print("File dna.example.fasta does not exist!!")
    

    
# Reading the FASTA file

seqs={}
for line in f:    
    # let's discard the newline at the end (if any)
    line=line.rstrip()
    # distinguish header from sequence
    if line[0]=='>':
        words=line.split() # splits the words in the line into elements of a list
        name=words[0][1:] # the 1st word [0] in the list is the name - '>' sign [1:]
        seqs[name]='' # initialize the name of the sequence to be an empty string
    else:
        seqs[name]=seqs[name]+line # dna sequence    
f.close()

# Retrieving data from dictionaries

for name, seq in seqs.items():
    print(name)
    
# The number of records in the file


Length_of_seqs=len(seqs)
print("Number of records in seqs dictionary: %d" % Length_of_seqs)

    
# Lengths of sequences in the records are in the file &
# Maximum and Minimum length of all the sequences in the file

for name, seq in seqs.items():
    Length_of_seq=len(seq)
    print(name, Length_of_seq)

# Identifying open reading frames (ORF), an ORF is a DNA sequence does NOT have a STOP codon at
# the end of the sequence, The reading frame starts at the START codon and canhave position 1, 2 or 3


    
def start_codon(dna,frame):
    

    
    """ TO CHECK THE PRESENCE OF START CODON AND ITS POSITION"""
    
    start_codons=['ATG','atg'] #referece list of start and stop codons
    for i in range(frame,len(dna),3):
        codon1=dna[i:i+3]
        if codon1 in start_codons:            
            position1=dna.index(codon1)#getting the index of the start codon
            ORF_start=position1+1
            break
    try:
        return ORF_start
    except UnboundLocalError:
        None  

for name, seq in seqs.items():
    Sequence=start_codon(seq, 0)
    print(name, Sequence)
    


# Maximum length of ORF, starting codon, reverse_complement and id


from Bio import SeqIO
import re
records = SeqIO.parse('dna2.fasta', 'fasta')

for record in records:
    for strand, seq in (1, record.seq), (-1, record.seq.reverse_complement()):
        for frame in range(3):
            index = frame
            while index < len(record) - 6:
                match = re.match('(ATG(?:\S{3})*?T(?:AG|AA|GA))', str(seq[index:]))
                if match:
                    orf = match.group()
                    index += len(orf)
                    if len(orf) > 1300:
                        pos = str(record.seq).find(orf) + 1 
                        print("{}...{} - length {}, strand {}, frame {}, pos {}, name {}".format\
                           (orf[:6], orf[-3:], len(orf), strand, frame, pos, record.id))
                else: index += 3

# Find Repeat sequences using hash sets, to avoid listing repeats of the repeat sequences

def findRepeatedDnaSequences(s):
    seen, res = set(), set()
    for l in range(len(s)-5):
        cur=s[l:l+6]
        if cur in seen:           
            res.add(cur)
        seen.add(cur)
    return list(res)

s = "ccccaaccccaaccccccccaaccccaaccccccccaaccccaacccc"

findRepeatedDnaSequences(s)

for name, seq in seqs.items():
    s=seq
    result=findRepeatedDnaSequences(s)
    print(name, result)
    
# Finding how many repeats there are of repeat sequences

def findRepeatedDnaSequences1(s):
    seen, res = list(), list()
    dict_of_counts = {}
    string_found=False
    string2_found=False
    string3_found=False
    string4_found=False
    list_seq=[]
    
    
    for l in range(len(s)-5):
        cur=s[l:l+6]
        if cur in seen:
            
            res.append(cur)
        else:
            seen.append(cur)
    
    dict_of_counts = {item:res.count(item) for item in res}    
    sorted_counts = sorted(dict_of_counts.values())
    list_seq = dict_of_counts.keys() 
    
    string = 'TGCGCGC'
    string2 = "CGCGCCG"
    string3 = "GCGCGCA"
    string4 = "CATCGCC"
    
    if string in list_seq:
        string_found=True
        print(dict_of_counts['TGCGCGC'])
    elif string2 in list_seq:
        string2_found=True
        print(dict_of_counts["CGCGCCG"])
    elif string3 in list_seq:
        string3_found=True
        print(dict_of_counts["GCGCGCA"])
    elif string4 in list_seq:
        string4_found=True
        print(dict_of_counts["CATCGCC"])
 
    

    return  dict_of_counts, sorted_counts #string_found, string2_found, string3_found, string4_found
 
    
for name, seq in seqs.items():
    s=seq
    result=findRepeatedDnaSequences1(s)
    print(name, result)
    
s = "ccccaaccccaaccccccccaaccccaaccccccccaaccccaacccc"

findRepeatedDnaSequences1(s) 
    