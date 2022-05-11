# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:31:06 2022

@author: Windows.10
"""

s=int(input("s="))
a=res=0
while s!=0:
    res=res+(s%2)*(10**a)
    s=s//2
    a+=1
print (f"the binary number={res}")   
 