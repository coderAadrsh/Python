# what is oop :- maping the real world object with code.
# what is class and object.:-calss is a blueprint on object means (in class we can be define two things 1.properties/attributes,2.methods/behaviours) and object is instance of class.
#how to create a class and object.
# class student:
#     #properties/attributes.
#     subject="python"
#     college="abc"
#     cgpa=9.8
# #create a object just like variable.
# stu1=student()
# print(stu1)# reference of memory
# print(stu1.subject,stu1.college,stu1.cgpa)
 
#constructor:-a function use to condtruct the object.
#method __init__(self):avaliable in all class in by default.

# class student:
#     def __init__(self,name,cgpa):
#         self.name=name
#         self.cgpa=cgpa
#     def get_cgpa(self):
#         return self.cgpa
#     print("this constructor call....")
    

# stu1=student("adarsh",8.1)
# print(stu1.name)
# print(stu1.get_cgpa())



# #QUETION 1:
# class Product:
#     def __init__(self,model,price):
#         self.model=model
#         self.price=price
#     def __init__(self):
#         print(f"product is{self.model} & price is{self.price}")    

# lenevo=Product("tz series",70000)
# vivo=Product("t4x 5g",14999)
# vivo.model()

#-------------------------------------OOP------------------------------------------------
# #1.ENCAPTULATION:-Wapping data and function into a single unite.and also use in data hidding.
# class BankAccount:
#     def __init__(self,name,account_id,balance):
#         self.name=name
#         self.account_id=account_id
#         self.__balance=balance #private-data mangling
#         #self._balance=balance(protected)//acc1._balance(access)
#     def get_balance(self):#getter
#             return self.__balance
#     def set_balance(self,newbalance):#setter
#             self.__balance=newbalance


# acc1=BankAccount("adarsh",100014548,455578558)
# acc1.set_balance(1000000000000)

# print(acc1.get_balance())
# #print(acc1.name,acc1.account_id,acc1._BankAccount__balance)#private access without getter and setter.


# #1.SINGLE LEVEL

# class Employee:
#     start_time="10am"
#     end_time="6pm"
#     def change_time(self,newend_time):
#         self.end_time=newend_time
# class Teacher(Employee):
#     def __init__(self,subject):
#         self.subject=subject
# t1=Teacher("math")
# t1.change_time("5pm")
# print(t1.subject,t1.start_time,t1.end_time)


# ##2.MULTI LEVEL

# class Employee:
#     start_time="10am"
#     end_time="6pm"
#     def __init__(self,id):
#         self.id=id
   
# class AdminsStaff(Employee):
#     def __init__(self,role):
#          self.role=role
# class Accountant(AdminsStaff):
#     def __init__(self,salary,role,id):
#         super().__init__(role)
#         Employee.__init__(self,id)
#         self.salary=salary
              

# acc1=Accountant(400000,"CA","Xtz0123")
# print(acc1.salary,acc1.role,acc1.start_time,acc1.id)
# #3.MULTIPLE LEVEL
# class Teacher:
#     def __init__(self,salary):
#         self.salary=salary
# class Student:
#     def __init__(self,cgpa):
#         self.cgpa=cgpa
# class TA(Teacher,Student):
#     def __init__(self, salary,cgpa,name):
#         super().__init__(salary)
#         Student.__init__(self,cgpa)
#         self.name=name
# ta1=TA(40000,8.1,"adarsh")
# print(ta1.name,ta1.cgpa,ta1.salary)

# #3.ABSTRACTION:-Hiding internal details & showing only essaential faetures.
# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def make_sound():
#         pass
# class Lion(Animal):
#     def make_sound(self):
#         print("Roar!")
# class Cow(Animal):
#     def make_sound(self):
#         print("Moo!")

# cow=Cow()
# cow.make_sound()



# #creation of class.
# class Student:
    
    


#     def __init__(self,name,cgpa):
#         self.name=name
#         self.cgpa=cgpa
#         print("constructor was call")

#     def get_cgpa(self):
#         return self.cgpa

# #object creation
# stu1=Student("adarsh",8.1)
# stu2=Student("naveen",8.2)
# print(stu1.name,stu1.cgpa)
# print(stu2.name,stu2.cgpa)
# print(stu1.get_cgpa())
# print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")

# class products:
#     track=0 # class attribute
#     def __init__(self,name,price):# instance attribute
#          products.track+=1
        
#          self.name=name
#          self.price=price

#     def get_info(self):# instance method
#         print(f"product name is {self.name} & price is {self.price} ")

#     def get_track(cls):# class method
#         return cls.track
    
#     @staticmethod
#     def discount(price,discount):# static method
#         final_price=price-(price*discount)/100
#         print(f"after {discount} % discounttotal price {final_price}")


# product2=products("pen",10)
# product1=products("BOOK",100)
# product1.discount(100,10)
# product1.get_info()

# print(products.track)
# #FOUR PILLARS OF OOP:-

# #1.Encapsulation: rapping data and methods into a single unit.

# #2.Inheritance: mechanism of acquiring properties and behaviors from parent class to child class.

# #3.Polymorphism: ability to take more than one form.

# #4.Abstraction: hiding internal details and showing only essential features.

# # #START WITH ENCAPSULATION.

# class BankAccount:
#     def __init__(self,name,account_id,balance):
#         self.name=name
#         self.account_id=account_id
#         self.set_balance(balance) #private-data mangling
#         #self._balance=balance(protected)//acc1._balance(access)


#     def get_balance(self):#getter
#             return self.__balance
        
#     def set_balance(self,newbalance):#setter
#             if newbalance<=0:
#                   print("You cant set negative balance or zero balance")
                  
#             else:
#                   self.__balance=newbalance
#                   print("balance updated successfully")
#             return "Check your balance using get_balance() method"
                     
       
# acc1=BankAccount("adarsh",100014548,455578558)

# print(acc1.name,acc1.account_id )
# #,acc1.__balance)#private access without getter and setter.

# #we can also access private  variable without using getter and setter using name mangling.like Syntax: object._ClassName__privateVariable
# print(f"way to direct access private variable: {acc1._BankAccount__balance}")
# print (acc1.set_balance(1000000000000000000000))
# print(acc1.get_balance())


# #2.Inheritence: is a mechanism of acquiring properties and behaviors from parent class to child class.

## types of inheritence:- there are 3 types of inheritence.
# #1.SINGLE LEVEL

# class vehicle:
      
#       def __init__(self,brand ,speed):
#             self.__brand=brand
#             self.__speed=speed

#       def set_brand(self,brand):
#             self.__brand=brand

#       def get_brand(self):
#             return self.__brand
      
#       def set_speed(self,speed):
#             self.__speed=speed

#       def get_speed(self):
#             return self.__speed
      
#       def info(self):
#             print(f"Vehicle Brand is {self.get_brand()} And Speed {self.get_speed()} Km/h.")


# class car(vehicle):
#       def __init__(self,brand,speed,door):
#             super().__init__(brand,speed)
#             self.door=door

#       @override
#       def info(self):
#           super().info()
#           print(f"car Brand is {self.get_brand()} And Speed {self.get_speed()} Km/h.")

#2.hierarchical LEVEL:

# from typing import override


# class vehicle:
      
#       def __init__(self,brand ,speed):
#             self.__brand=brand
#             self.__speed=speed

#       def set_brand(self,brand):
#             self.__brand=brand

#       def get_brand(self):
#             return self.__brand
      
#       def set_speed(self,speed):
#             self.__speed=speed

#       def get_speed(self):
#             return self.__speed
      
#       def info(self):
#             print(f"Vehicle Brand is {self.get_brand()} And Speed {self.get_speed()} Km/h.")


# class car(vehicle):
#       def __init__(self,brand,speed,door):
#             super().__init__(brand,speed)
#             self.door=door

#       @override
#       def info(self):
#           super().info()
#           print(f"car Brand is {self.get_brand()} And Speed {self.get_speed()} Km/h.")


# class motorcycle(vehicle):
#       def __init__(self,brand,speed,door):
#             super().__init__(brand,speed)
#             self.door=door

#       @override
#       def info(self):
#           super().info()
#           print(f"motorcycle Brand is {self.get_brand()} And Speed {self.get_speed()} Km/h.")
    

             
                  
            
# v1=car("toyota",120,5)
# v1=motorcycle("honda",100,0)
# v1.info()

#2.MULTI LEVEL

class Employee:
      start_time="10am"
      end_time="6pm"
      def __init__(self,id):
          self.__id=id

class AdminStaff(Employee):
      def __init__(self,role,id):
           self.role=role
           super().__init__(id)

class Accountant(AdminStaff):
      def __init__(self,salary,role,id):
            self.salary=salary
            super().__init__(role,id)
            #Employee.__init__(self,id)
            

acc1=Accountant(400000,"CA","Xtz0123")
print(acc1.salary,acc1.start_time,acc1.end_time ,acc1.role,acc1._Employee__id)

#3.MULTIPLE LEVEL
class Teacher:
      def __init__(self,salary):
          self.salary=salary
class Student:
      def __init__(self,cgpa):
          self.cgpa=cgpa

class TA(Teacher,Student):
      def __init__(self, salary,cgpa,name):
          super().__init__(salary)
          Student.__init__(self,cgpa)
          self.name=name
ta1=TA(40000,8.1,"adarsh")
print(ta1.name,ta1.cgpa,ta1.salary)