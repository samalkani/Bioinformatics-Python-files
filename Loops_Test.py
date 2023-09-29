# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:49:26 2022

Test

@author: Ajay_
"""

fold=2

if fold > 2 : 
    print('condition A')

elif fold>100: 
    print('condition B')

if fold> 2 or fold<2 : 
    print('condition A')

else : 
    print('condition B')

# Question 5

# A - No adjustments

seq='tatc'
    
for i in range(len(seq)) :    # line 1
        for j in range(i) :        # line 2
                print(j, i, seq[j:i])     # line 3
                
# B - Add in line 1 for i in range(len(seq)+1) : 

seq='tatc'
    
for i in range(len(seq)+1) :    # line 1
        for j in range(i) :        # line 2
                print(j, i, seq[j:i])     # line 3

# C - Add in line 2 print(j, i, seq[j:i+1])

seq='tatc'
    
for i in range(len(seq)) :    # line 1
          for j in range(i) :      # line 2
                print(j, i, seq[j:i+1])     # line 3

# D - Add in line 2 for j in range(i+1) :
                
for i in range(len(seq)) :     # line 1
        for j in range(i+1) :        # line 2
                print(j, i, seq[j:i])     # line 3
                
# Question 6

# A - Does not produce a result

seq='tatc'
i=0 
while i<len(seq) :
      j=0 
      while(j<i) :
                print(seq[j:i]) 

# B - Only produces substrings containing the middle two letters

seq='tatc'                
i=1
while i<len(seq) :
      j=1
      while(j<i) :
                print(j, i, seq[j:i])
                j=j+1
      i=i+1

# C - Only produces substrings containing the first three letters
                
i=0 
while i<len(seq) :
      j=0 
      while(j<i) :
                print(j, i, seq[j:i])
                j+=1
      i+=1

# D - Produces the same output as the for loop
                
i=0
while i<len(seq)+1 :
      j=0
      while(j<i+1) :
                print(j, i, seq[j:i])
                j=j+1
      i=i+1
      
# E - Does not produce a result

i=1
while i<len(seq)+1 :
      j=1
      while(j<i+1) :
                print(seq[j:i])
                
# F - No result

i=0
while i<len(seq) :
      j=i
      while(j>0) :
                print(seq[j:i])
                j=j+1
      i=i+1

mylist=[1,2,3,4,4,5]
d = {} # set no duplicates
result = False
for x in mylist:
        if x in d:
            result=True
            break
        d[x] = True
        print(d)
print(d, result)

mylist=[1,2,3,4,4,5]
d = {}
result = False
for x in mylist:
       if not x in d:
	       d[x]=True
	       continue
       result = True
print(d, result)

i = 1
while i < 100:
          if i%2 == 0 : break
          i += 1
          print(i)
else:
     i=1000

x = 1000001

if x>10 or x<-10: print('big')
elif x>1000000: print('very big')
elif x<-1000000: print('very big')
else : print('small')