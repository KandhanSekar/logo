import sys
import re

i=0
b=[]
var=input("Enter")
print(var)
var = re.sub('"', '', var)
print(var)
a=var.split('|')
print(len(a))
print(a[2])
while(i<len(a)):
      print(i)
      print(a[i])
      b.append(a[i])
      i=i+1
      
print(b)




