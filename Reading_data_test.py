# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:34:35 2022

@author: Ajay_
"""

string = 'myfile.tar.gz'
string1 = 'myfile'

def get_extension1(filename):
    return(filename.split(".")[-1])

get_extension1(string)

get_extension1(string1)

def get_extension2(filename):
    import os.path
    return(os.path.splitext(filename)[1])

get_extension2(string)

get_extension2(string1)

def get_extension3(filename):
    return filename[filename.rfind('.'):][1:]

get_extension3(string)

get_extension3(string1)

