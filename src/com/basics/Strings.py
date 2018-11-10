'''
Created on 10-Nov-2018

@author: skp4j
'''
str1="Sunil"
str2="Sunil"
print(id(str1))
print(id(str2))

s = "this is bad spam " * 3
print(s)

# Iterating String
s = "hello"
for i in s:
    print(i, end="")
    
string1="Sunil Pandey"
print(string1.isalnum())