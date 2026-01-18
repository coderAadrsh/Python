# Lists 
# What is a List? 
# • A list is a collection of items in Python. 
# • Items in a list are ordered, changeable (mutable), and can contain duplicates. 
# • Lists can hold any data type: numbers, strings, other lists, etc. 
# • Lists are written using square brackets  [] 

 
# Example: 
# my_list = [1, 2, 3, 4, 5]  
# print(my_list)  
# print(type(my_list))     
# # <class 'list'>  
# my_list2 = [10, "Hello", 3.14, True, 10]    
# print(my_list2) 
# # heterogenous list  
# List Characteristics 
# 1. Ordered – Items have a defined order and can be accessed by index. 
# 2. Mutable – Items can be changed after the list is created. 
# 3. Allows duplicates – Same value can appear more than once. 
# 4. Heterogeneous – Can contain different data types. 
# List Indexing 
# Index in list is the position value of an item. Index starts from     .  
# We can use index to access elements, modify the list or even slice it. 
# Access Elements 
# my_list = ["apple", "banana", "cherry"]  
# print(my_list[0])  # apple  
# print(my_list[1])  # banana  
# θ 
# print(my_list[-1]) # cherry (last element) 
# Modify Elements 
# my_list = [1, 2, 3, 4]  
# my_list[0] = 10  
# print(my_list) # [10, 2, 3, 4] 
# Slicing - Slicing in lists is same as slicing in strings.  
# The general syntax for slicing a list is: 
# list[start:stop:step] 
# • start - inclusive 
# • end - exclusive 
# adarsh7373singh@gmail.com
#  • step - optional (default = 1) 
# 4 
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
# # Simple Slice  
# print(numbers[2:5])  # Output: [2, 3, 4]  
# print(numbers[:4])   # Output: [0, 1, 2, 3] (from start to index 3) 
# print(numbers[5:])   # Output: [5, 6, 7, 8, 9] (from index 5 to end) 
# print(numbers[:])    
# # Output: [0,1,2,3,4,5,6,7,8,9] (copy of the whole list) 
# # using STEP  
# print(numbers[::2])  # Output: [0, 2, 4, 6, 8] (every2nd element) 
# print(numbers[1::3])  
# # Output: [1, 4, 7] (start at 1, every 3rd element)  
# # NEGATIVE slice  
# print(numbers[-5:-2]) # Output: [5, 6, 7] (negative indexing from end) 
# List Methods 
# len() 
# We have a lot of useful functions that are associated with lists. Let’s have a look at 
# some of them: 
# 1.         - returns the number of elements in a list i.e. length of the list. 
# 2.                          
# append(element) 
# 3.                                     - adds an elements to the end. 
# 4.            
# 5.                 
# insert(element, idx) 
# sort() 
# reverse() - adds at a specific position. - sorts in ascending/alphabetical order. - flips the order of elements. 
# nums = [5, 2, 9]  
# print(len(nums)) # 3  
# nums.append(7)  
# print(nums) # [5, 2, 9, 7]  
# nums.insert(1, 4)  
# print(nums) # [5, 4, 2, 9, 7]  
# nums.sort()  
# print(nums) # [2, 4, 5, 7, 9]  
# nums.reverse()  
# print(nums) # [9, 7, 5, 4, 2] 
# There are many more methods associated with lists. It doesn’t make a lot of sense to 
# cover all of them theoretically here, so we’ll be covering them whenever we use them 
# in coming chapters. 
# adarsh7373singh@gmail.com
#  5 
# Loops on Lists 
# for 
# We use the classical     loop to traverse the entire list element-wise. 
# The most common way is using a loop in lists is to print elements. 
# numbers = [10, 20, 30, 40, 50]  
# for num in numbers:  
# print(num) 
# Linear Search 
# A linear search checks each element one by one to find a target (x). 
# numbers = [5, 12, 7, 3, 18, 9]  
# x = 18  
# idx = 0  
# for num in numbers:  
# if num == target:  
# print(f"{x} found at index={idx}")  
# break  
# idx         1 
# += 
# In the above code, we are assuming that     always exists in the list. 
# x

#---------------------------------------------------MY WORK----------------------------------------------------------------------------


#list :collection of items in python,list is orderd ,changeable(mutable),and contaning different data types (hetrogenous) like  string ,int ,boolean etc.
#creation of list.
l1=[12.1,10,"adarsh",'a',True,[1,2,3]]
print(l1)
#modify
l1[0]="dipu"
print(l1)
#indexing
print(l1[5])
#slicing
print(l1[:])
print(list[0:])
print(l1[:len(l1)])
print(l1[::2])
print(l1[::-1])
#-----------------------------------------method on list------------------------------------------
#len()
print(len(l1))


#clear() functionl1t.clear()
# print(l1.clear())
#append(element)
# for i in range(1,11):
#    num=int(input(f"enter number 10 times:{i}:="))
#    l1.append(num)
# print(l1)
l1.append(7)
print(l1)
#l1.insert(indx,element)
l1.insert(5,11)
print(l1)
l1.clear()
l1=[7,6,5,1,2,3,4]
l1.sort(reverse=True)
print(l1)
l1.reverse()
print(l1)
# Question1:apply searching algorithm
def linearsearch(items,search):
     indx=0
     for i in items:
          if(search!=i):
               indx+=1
     return indx

items=[1,3,4,6,8,9,10]
x=int(input("enter the number you want to search"))
print(linearsearch(items,x))
                   # num=[90,95,91,96,97,99]

# idx=0
# search=100
# for i in num:
#     if(i==search):
#          print(idx)
#          break
    
#     idx+=1
# else:
#      print("not found")

# item=[1,2,3,4,5]
# x=5
# for i in range(len(item)):
#      if(item[i]==x):
#          print(f"{item[i]} found at index {i}")
#          break
# el