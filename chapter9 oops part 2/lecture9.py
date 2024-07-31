#del keyword//

# class student:
#     def __init__(self,name):
#         self.name=name

# s1=student("vansh")
# print(s1.name)
# del s1
# print(s1.name)


#private(like)//

# class account:
#     def __init__(self,acc_no,acc_pass) :
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass #for private

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1=account("123","abc")
# print(acc1.acc_no)
# #print(acc1.__acc_pass)
# print(acc1.reset_pass())


#private attriute
# class person:
#     __name="anonymous"

# p1=person()
# print(p1.__name)


#private method
# class person:
#     __name="anonymous"

#     def __hello(self):
#         print("hello")

#     def welcome(self):
#         self.__hello()
# p1=person()
# # print(p1.__name)
# # p1.__hello()
# p1.welcome()
# #internal methods within in the class can acces the private methods and attributes


#inheritance // 
#single inheritance
# class car:
#     color="black"

#     @staticmethod
#     def start():
#         print("car started")
    
#     def stop():
#         print("car stopped")

# class toyotaCar(car):
#     def __init__(self,name):
#         self.name=name

# car1=toyotaCar("fortuner")
# car2=toyotaCar("prius")

# print(car1.start())
# print(car1.color)

#multi level inheritance
# class car:
#     color="black"

#     @staticmethod
#     def start():
#         print("car started")
    
#     @staticmethod
#     def stop():
#         print("car stopped")

# class toyotaCar(car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(toyotaCar):
#     def __init__(self, type):
#         self.type=type
    


# car1=Fortuner("disel")
# car2=toyotaCar("prius")

# car1.start()
# print(car1.type)


#multiple inheritance

# class A:
#     varA="welcome to class A"

# class B:
#     varB="welcome to class B"

# class C(A,B):
#     varC="welcome to class C"

# obj1=C()
# print(obj1.varA)
# print(obj1.varB)
# print(obj1.varC)


#super method
# class car:
#     def __init__(self, type):
#         self.type=type

#     @staticmethod
#     def start():
#         print("car started")
    
#     def stop():
#         print("car stopped")

# class toyotaCar(car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start()

# car1=toyotaCar("fortuner","petrol")
# print(car1.name)
# print(car1.type)


class person:
    name="anonymous"

    # def changeName(self,name):
    #     self.name=name

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=person()
p1.changeName("vansh mehta")
print(p1.name)
print(person.name)#same i.e anonymous

#changing the class name attribute 

# method1:
# def changeName(self,name):
#         person.name=name

# method2:
# def changeName(self,name):
#         self.__class__.name="Vansh Mehta"

# method 3: is class method
# class Student: #example
#             @class method #decorator
#             def college(cls):
#                 pass

#@property

# class Student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths

#     # def percentage(self):
#     #     return str((self.phy+self.chem +self.maths)/3)+"%"

#     @property
#     def percentage(self):
#         return str((self.phy+self.chem +self.maths)/3)+"%"

# stu1=Student(98,93,90)
# print(stu1.percentage)
# stu1.phy=60

# print(stu1.percentage)


#polymorphysm////
# print(1+2)#3
# print("vansh"+ "mehta") #concatenation
# print([1,2,3] + [4,5,6]) #merge

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")
    
#     # def add(self,num2):
#     #     newReal=self.real+ num2.real
#     #     newImg=self.img + num2.img
#     #     return Complex(newReal,newImg)
    
#     def __add__(self,num2):
#         newReal=self.real+ num2.real
#         newImg=self.img + num2.img
#         return Complex(newReal,newImg)
    
#     def __sub__(self,num2):
#         newReal=self.real - num2.real
#         newImg=self.img - num2.img
#         return Complex(newReal,newImg)

# num1=Complex(5,2)
# num1.showNumber()

# num2=Complex(6,7)
# num2.showNumber()

# # num3=num1.add(num2)
# # num3.showNumber()

# #num3=(num1+num2) #error
# #thats why we use dunder function

# num3=(num1+num2)
# num3.showNumber()

