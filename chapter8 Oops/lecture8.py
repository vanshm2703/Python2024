#classes and objects

#creating class
# class student:
#             name="vansh mehta"

 #creating object(instance)
# s1=student()
# print(s1.name)

# class car:
#     color="blue"
#     brand="mercedes"

# car1=car()
# print(car1.color)
# print(car1.brand)


#constructor

#creating class
# class student:
#     #default constructor
#     # def __init__(self):
#     #     print("adding new student in Database..")

#     college="abc" #class attribute
#     # name="vansh mehta"
#     #parameterised constructor
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         #print(self) #tudent object at 0x0000022CA8D9D610
#         print("adding new student in Database..")

# s1=student("vansh",99) #adding new student in Database..
# print(s1.name,s1.marks) #vansh

# s2=student("arjun",98) #adding new student in Database..
# print(s2.name,s2.marks) #arjun

# print(s2.college)


# class student:
#     #default constructor
#     # def __init__(self):
#     #     print("adding new student in Database..")

#     college="abc" #class attribute
#     name="XYZ"#class attribute
#     #parameterised constructor
#     def __init__(self,name):
#         self.name=name
#         # self.marks=marks
#         #print(self) #tudent object at 0x0000022CA8D9D610
#         print("adding new student in Database..")

# s1=student("vansh") #adding new student in Database..
# print(s1.name) #vansh as obj precidence>>> class atrr precidence




#methods

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def welcome(self):#method for name
#         print("welcome student",self.name)

#     def getmarks(self):#method for marks
#         return self.marks

# s1=student("vansh",93) 
# print(s1.name) 
# print(s1.getmarks())


#Abstraction

# class car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.cluch=False

#     def start(self):
#         self.cluch=True
#         self.acc=True
#         print("car started..")

# car1=car()
# car1.start()


#Encapsulation
