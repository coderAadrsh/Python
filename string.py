# Python Fundamentals (Part3) 
# Concepts : String, List, Tuple, Dictionary & Set 
# In this chapter we are going to dive deep into some of the not-so-simple data types of 
# Python. 
# Strings 
# What is a String? 
# A string in Python is a sequence of characters enclosed in quotes: 
# str1 = "hello world"  
# str2 = 'Prime' 
# Strings are immutable, meaning once created, their contents can’t be changed 
# directly. 
# len() 
# Function 
# len() 
# We can use the built-in              function to print the length of a string: 
# word = 'Prime'  
# print(len(word))  
# # 5 
# Concatenation 
# Just like we add numbers, we can concatenate (i.e. join) strings using the      operator. 
# str1 = "Apna"  
# str2 = "College"  
# word = str1 + " " + str2       
# print(word) 
# + 
# # concatenation  
# Loop on Strings 
# s = "Python"  
# for ch in s:  
# print(ch) 
# # ch will store individual chars - 'P', 'y', 't' & so on 
# Indexing in Strings 
# Index in a sequence (like strings) represents the position value of individual elements 
# i.e. characters in case of a string. So Indexing lets us access individual characters in 
# a string. 
# adarsh7373singh@gmail.com
#  1 
# Python follows Zero-based indexing i.e. first character is at index     . 
# 0 
# s = "Python"  
# print(s[0])  # 'P'  
# print(s[3])  # 'h'   
# print(s[-1]) # 'n' (negative index: last character) 
# Slicing in Strings 
# Slicing is a powerful feature of Python that lets us access multiple elements at once. 
# We can do slicing in strings & even on other sequences like lists & tuples. 
# The general syntax for slicing a string is: 
# string[start : end : step] 
# Where: 
# • start - index where the slice starts (inclusive). Defaults to     if omitted. 
# 0 
# • stop - index where the slice ends (exclusive). Defaults to the end of the string if 
# omitted. 
# • step - how many indices to move forward each time. Defaults to     . 
# 1 
# Example: 
# s = "Python"  
# print(s[0:2])   # 'Py'  
# print(s[2:])    
# # 'thon'  
# print(s[:3])    
# # 'Py t'  
# print(s[::2])   # 'Pto' (every second char)  
# print(s[::-1])  # 'nohtyP' (reversed string) 
# String Formatting 
# String formatting is the process of creating dynamic strings by inserting values from 
# variables or expressions into a predefined string template. This allows for the 
# construction of flexible and informative output based on changing data. 
# We have multiple ways to format a string, the most modern 2 are: 
# 1. using the                  function 
# 2. using 
# format() 
# f-strings 
# 1. Using 
# .format() 
# {} 
# In this way we use     as placeholders & pass placeholder replacement values in the 
# format function. 
# adarsh7373singh@gmail.com
#  2 
# name = "Rahul"  
# age = 25  
# text = "My name is {} and I am {} years old".format(name, age)  
# print(text) 
# We can also use positional & named placeholders: 
# "Coordinates: {1}, {0}".format("x", "y") # 'Coordinates: y, x' 
# "Name: {n}, Age: {a}".format(n="Bob", a=30) 
# 2. Using f-strings (Python 3.6+) 
# F-strings are concise, readable & will be our preferred way going forward. 
# In f-strings we prefix the string with       and put our variable or expressions inside       . 
# f 
# name = "Rahul"  
# age = 25  
# text = f"My name is {name} and I am {age} years old"  
# print(text) 
# {} 
# You can put any valid Python expression inside      : 
# {} 
# a = 5  
# b = 10  
# print(f"sum of {a} & {b} = {a + b}")  
# print(f"avg of {a} & {b} = {(a + b) / 2}")
#----------------------------------------------------------------------my work start frome here-----------------------------
# #create a string:single quotes,Double Quotes,Triple Quotes=poem way output.

# str1="12345678"

# str2='efgh'
# str3='''hello
# my name is adarsh

# '''
# a=10
# b=20
# sum=a+b
# #  take user input : use input()
# #str4=input("enter your name:")
# #-----------------------------------------operation and methods on strings--------------------------------------
# #length function: using len()
# print(len(str1))
# #concatenation using "+" operator join two or more string.
# print(str1+str2+str3)
# #indexing in string: follow Zero Based indexing also available on negative indexing which start with -1  .
# print(str1[len(str1)-1])#way to  change the negative index its corresponding postive index.len(str)-negative index
# print(str1[0])
# x=str1[1]
# print(x)
# print("------------------------")
# #loop  in string
# for ch in str1:
#     print(ch)
# #Slicing in string.
# print(str1[:],"  if did not give start ,stop value.")
# print(str1[0:],"  only give start value.")
# print(str1[:len(str1)],"  only give end value.")
# print(str1[0:10:2],"   give start ,stop,step value")
# print(str1[::])
# print(str1[::2])
# print(str1[::-1],"PRINT REVERSE ORDER.")
# #FORMATING IN STRING: 2 MODRDEN WAY USE MOST PROBBALY 1.format() function, 2. f-strinf functon.
# #1 format() function:intoduce in python 3, here use placeholder'{}' and placement value that replace the placeholder.
# print("sum is {}".format(sum))
# #multiple of format also avialable.
# print("sum is {} and {} is {}".format(a,b,sum))
# #index based formating.
# print("sum is {1} and {0} is {2}".format(a,b,sum))
# #value based formating
# print("sum is {a} and {b} is {sum}".format(a=10,b=20,sum=30))
# #2. F-string formating: use literal string interpolation. start with f" {variable} and/or { expression} ".
# print(f"sum of {a} and {b} is:{a+b}")


# #----------------------------------------------other operation in string-----------------------------------------------------------
# import math
# str1=" 12  34"
# str2="123    adarsh, How can Ielp you   "
# str4="adarsh, How can Ielp you ?"

# a=str2.casefold()
# b=str4.lower()
# print(str1.isspace())
# print(str1[::-1])
# # print palindrome string
# def palindrome(str3):
#     for i in range(int(len(str3)/2)):
#         if(str3[i]!=str3[len(str3)-i-1]):
#            return False
#     return True  
# def shortestpath(direction):
#     x=0
#     y=0
#     for ch in direction:
#         if ch=='E':
#             x+=1
#         elif ch=='W':
#             x-=1  
#         elif ch=='N':
#             y+=1
#         elif ch=='S':
#             y-=1
#     X=x*x
#     Y=y*y
#     path=math.sqrt(X+Y)
#     print(path)

# str3="RAAR"
# direction="WNEENESENNN"
# shortestpath(direction)
# print(palindrome(str3))
first_name=input("enter your name:")

last_name=input("enter your last name:")
full_name=first_name.strip()+ " "+last_name.strip()
print(full_name)
print(full_name)