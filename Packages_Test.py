# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 21:14:08 2022

@author: Ajay_
"""

import random

def create_dna(n, alphabet='acgt'):
    return ''.join([random.choice(alphabet) for i in range(n)])

dna = create_dna(1000000)

print(dna)

count_dna = dna.count()

def count1(dna, base):
    i = 0
    for c in dna:
        if c == base:
	        i += 1 
    return i

count1(dna, 'c')


def count2(dna, base):
    i = 0 
    for j in range(len(dna)):
        if dna[j] == base:
	        i += 1 
    return i 

count2(dna, 'c')

def count3(dna, base):
    match = [c == base for c in dna]
    return sum(match)

count3(dna, 'c')

def count4(dna, base):
    return dna.count(base)

count4(dna, 'c')

def count5(dna, base):
    return len([i for i in range(len(dna)) if dna[i] == base])

count5(dna, 'c')

def count6(dna,base):
    return sum(c == base for c in dna)

count6(dna, 'c')

import time

start = time.time()
count1(dna, 'c')     # 1st slowest
end = time.time()
print(end - start)

start = time.time()
count2(dna, 'c')    # 2nd Slowest
end = time.time()
print(end - start)

start = time.time()
count3(dna, 'c')     # 3rd Slowest
end = time.time()
print(end - start)

start = time.time()
count4=(dna, 'c')   # fastest just a built-in function
end = time.time()
print(end - start)

start = time.time() 
count5(dna, 'c')    # 4th Slowest
end = time.time()
print(end - start)

start = time.time()
count6(dna, 'c')  # Slowest
end = time.time() 
print(end - start)

