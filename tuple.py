#creation:
t1=(1,2,3.4,True,"adarsh",[1,2,3])
print(t1)

#empty tuple
t2=()   
print(t2)
#single element tuple       
t3=(5,)
print(t3)

#MODIFICATION IS NOT POSSIBLE
# t1[1]="naveen" #TypeError: 'tuple' object does not support item assignment
# print(t1)
#INDEXING
print(t1[1])
#SLICING
print(t1[::2])# every 2nd element
print(t1[::-1]) #reverse order  
print(t1[:])# full tuple

#LOOPS ON TUPLE
for i in t1:
    print(i)

#METHODS ON TUPLE
print(len(t1))  
print(t1.index(3.4))
print(t1.count(2))
t1[5].append(4)
t1[5].pop()
print(t1) # we can modify the mutable element inside tuple

# unpacking
t2=(1,2,3,4,5)
a,b,c,d,e=t2
print(a,b,c,d,e,type(a))

#star unpacking
t2=(1,2,3,4,5,6,7,8,9)
a,*b,c=t2
print(a,b,c,type(b))

#packing
t3=a,b,c,d,e    
print(t3,type(t3))

#bulit in functions use in tuple
print(sum(t2))
print(max(t2))
print(min(t2))
print(sorted(t2))
print(tuple(range(1,11)))

