#exception: exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.
#exception handling: it is a process of responding to the occurrence of exceptions.
#it is used to handle runtime errors so that the normal flow of the application can be maintained.

#example:
# a=5       
# b=0
# c=a/b 
# print(c)  #it throws ZeroDivisionError: division by zero.



#try block: it is used to wrap the code that may throw an exception.

#except block: it is used to handle the exception that occurs in the try block.

#else block: it is used to execute the code that needs to be executed if no exception occurs in the try block.

# #finally block: it is used to execute the code that needs to be executed regardless of whether an exception occurs or not.

# from numpy import rint


# try:
#     x=int(input("enter numerator:"))
#     ans=10/x

# except ZeroDivisionError:
#     print("denominator cannot be zero.")

# except ValueError:
#     print("invalid input. please enter an integer value.")
# else:
#     print(f"the answer is {ans}")


# finally:
#     print("execution completed.")




# # #list comprehension: is a concise way to create lists.
# # #syntax:[output for item in iterable if condition]


# # l=[i*i for i in range(6)]
# # print(l)

# l=[i*i for i in range(6) if i%2!=0]
# print(l)


# l1=[-2,-4,3,5,-7,8,-1]
# l1=[0 if i<0  else i for i in l1 ]
# print(l1)




# JASON: JavaScript Object Notation
# it is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.
# it is used to transmit data between a server and a web application as an alternative to XML.  
# it is language independent but uses conventions that are familiar to programmers of the C family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others.