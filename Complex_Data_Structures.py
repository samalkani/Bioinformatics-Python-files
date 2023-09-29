# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:31:11 2022

Complex data structures

@author: Ajay_
"""

# Lists

['gene', 5.16e-08, 0.000138511, 7.33e-08]

gene_expression=['gene', 5.16e-08, 0.000138511, 7.33e-08]

# Access individual elements of the list

print(gene_expression[2])

print(gene_expression[-1])

# Modifying Lists

gene_expression[0]='Lif'

print(gene_expression)

# Don't Change an element in a string it is immutable

motif = 'nacgggtc'
motif[0]='a'
motif[4]

# Slicing Lists

gene_expression
gene_expression[-3]
gene_expression[:]

# Assignment using slicing

gene_expression
gene_expression[1:3]=[6.09e-07]
gene_expression

# clearing the list

gene_expression
gene_expression[:]=[]
gene_expression

# List Concatenation

gene_expression = ['Lif', 6.09e-07, 7.33e-08]
gene_expression+[5.16e-08, 0.000138511]

# List length of gene_expression

len(gene_expression)
gene_expression

# Delete an element of the list

gene_expression
del gene_expression[1]
gene_expression

# Lists as objects

# Using extend() method

gene_expression
gene_expression.extend([5.16e-08, 0.000138511])
gene_expression

# Using count() method

print(gene_expression.count('Lif'), gene_expression.count('gene'))

# Using reverse() method

gene_expression
gene_expression.reverse()
gene_expression

# Find all the methods

help(list)

# Using Lists as Stacks

stack=['a','b','c','d']

# Add item to the top of the stack using append() method

stack.append('e')
stack

# To retrieve the item at the top of the stack use the pop() method

elem=stack.pop()
elem
stack

# Sorting Lists using sorted() function

mylist=[3, 31, 123, 1, 5]
mylist
sorted(mylist)
mylist

# Alternative sorting using sort() method, 
# Object Orientated Programming (OOP)

mylist.sort()
mylist

# Sorting a list of strings using sorted() function

mylist=['c','g','T','a','A']
print(sorted(mylist))
mylist

# Alternative sorting using sort() method,
# Object Orientated Programming (OOP)

mylist=['c','g','T','a','A']
mylist.sort()
mylist




