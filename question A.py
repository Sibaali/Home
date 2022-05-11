# -*- coding: utf-8 -*-



"""
Spyder Editor

This is a temporary script file.
"""

l=['siba','ali','ammar','reem','nour']
sname= input('inter student name:')
for i in range(len(l)):
     if sname in l:
        print(sname,'this student graduated ')
        break
     else:
       print('this name didnt graduated')
       break
    