# #question 1:
# salary=float(input("Enter salary:"))
# tax=0
# if(salary<30000):
#     tax=.05*salary
#     print("tax is:",tax)
# elif(salary>=30000 or salary<70000):
#      tax=.15*salary
#      print("tax is:",tax)  
# else:
#      tax=.25*salary
#      print("tax is:",tax)  
# #question 2:
# num1=int(input("enter num1:"))          
# num2=int(input("enter num2:"))
# count_even=0
# sum_even=0   
# for i in range(num1+1,num2):
#      if(i%2==0):
#           sum_even+=i
#           count_even+=1
#           print(i)
# print("count_even:",count_even) 
# print("total even Sum:",sum_even)
# #Question 3 and 4:
# def Digit(num):
#      count=0
#      while(num>0):
#         digit=num%10
#         count+=1
#         print(digit)
#         num//=10
#      print("total digit:",count)

# num=int(input("enter digit:"))
# Digit(num)
#question 7:
def check():
     
    while(True):
        s=input("enter number or 'Quit' of exist:")  
        if(s=="Quit"):
            break
        else:
            num=int(s)

            if(num>0):
                print("postive")
            else:
                print("negative") 
        
        


check()
