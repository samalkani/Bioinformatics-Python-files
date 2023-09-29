# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 15:52:43 2022

Functions_Test

@author: Ajay_
"""

def swap1(x,y) :
    x=y
    y=x
    return(x,y)

swap1(1,2)

def swap2(x,y) :
    return(y,x)

swap2(1,2)

def swap3(x,y) :
    z=x
    x=y
    y=z
    return(x,y)

swap3(1,2)

def swap4(x,y) :
    x,y=y,x
    return(x,y)

swap4(1,2)



def f1(x):
    if (x > 0):
        x = 3*x 
        x = x / 2
    return x

f1(-6)

def f2(x):
    if (x > 0):
        x = 3*x
    x = x / 2
    return x

f2(-6)

def function1(length):
    if length > 0:
        print(length)
        function1(length - 1)

function1(6)


def function2(length):
    while length > 0:
        print(length)
        function2(length - 1)
        
function2(6)

def compute(n,x,y) :
    if n==0 : return x
    return compute(n-1,x+y,y)

compute(3,1,1)

def valid_dna1(dna):
    for c in dna:
        if c in 'acgtACGT':
            return True
        else:
            return False

valid_dna1('atgga')

def valid_dna2(dna):
    for c in dna:
       if 'c' in 'acgtACGT':
            return 'True'
       else:
            return 'False'
        
valid_dna2('ccatgga')

def valid_dna3(dna):
    for c in dna:
        flag = c in 'acgtACGT'
    return flag

valid_dna3('atgga')

def valid_dna4(dna):
    for c in dna:
        if not c in 'acgtACGT':
            return False
    return True

valid_dna4('ccatgga')

L1 = [1,2,2,3,4,4,5]

L2 = [6,5,4,3,2,8]

L3 = [i for i in set(L1) if i in L2]

print(L3)

def f(mystring):
         print(message)
         print(mystring)
         message="Inside function now!"
         print(message)
message="Outside function!"
f("Test function:")

f()


