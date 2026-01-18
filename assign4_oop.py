
# #Q1
# class BankAccount:
#     def __init__(self,account,owner_name,balance):
#         self.account=account
#         self.owner_name=owner_name
#         self.balance=balance
#     def Deposit(self,newbalance):
#         self.balance=self.balance+newbalance
#         print(f"you successfully deposit :{newbalance}.Rs")
#         print(f"Total balance is:{self.balance}.Rs")

#     def withdraw(self,amount):
#         self.balance=self.balance-amount
#         print(f"you successfully withdraw :{amount}.Rs")
#         print(f"remaning balance is:{self.balance}.Rs")
#     def check_balance(self):
#         print(f"Total balance is:{self.balance}.Rs")
        

       

# acc1=BankAccount(123456789,"adarsh",500)
# acc1.Deposit(1000)

# acc1.withdraw(500)
# print(acc1.balance,acc1.owner_name)


#Q2:
class Book:
    def __init__(self,title,author,list_of_reviews):
        self.title=title
        self.author=author
        self.list_of_reviews=list_of_reviews
        
        



#add method,a new review,count review,display all reviews     
    def Add_new_review(self,newreview):
        review_list=[]
        self.list_of_reviews=self.list_of_reviews+" "+newreview
        review_list.append(self.list_of_reviews)


bk1=Book("python","adarsh","good")
print(bk1.author,bk1.title,bk1.)