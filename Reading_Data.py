# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:03:18 2022

Reading & Writing data

@author: Ajay_
"""




# Reading from a file

f=open(r'C:\Users\Ajay_\OneDrive\Documents\Python_Scripts\myfile.txt', 'r') # r=read

f=open(r'C:\Users\Ajay_\OneDrive\Documents\Python_Scripts\myfile.txt') # default = read no need for 'r'

# Writing into file

f=open('myfile', 'w') # w=write

f=open('myfile', 'a') # a=append data to a file

# Checking before opening the file!

try:
    f=open(r'C:\Users\Ajay_\OneDrive\Documents\Python_Scripts\myfile.txt')
except IOError:
    print("The file myfile does not exist!!")
    
# The most efficient way of reading a file is to use a loop

for line in f:
    print(line)
    
# Alternative using the read method of the file object

f.read()

# Using the seek() method to go back to the beginning of the file

f.seek(0)

# Use the read() method again, displays the beginning of the file

f.read()

# Read one line at a time

f.seek(0)
f.readline()

# Writing to a file, writing in append mode

f=open(r'C:\Users\Ajay_\OneDrive\Documents\Python_Scripts\myfile.txt', 'a')
f.write('This is a third line')

f.seek(0)
f.read(0)


# Closing a file object

f.close()

# Error message is generated if you try to read a closed file

f.read()
