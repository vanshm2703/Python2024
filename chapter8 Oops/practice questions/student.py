#create student class that takes name and marks of subjects as arguments in constructor.then create a method to print the average.

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi ",self.name,"your marks marks is",sum/3)



s1=student("vansh",[91,92,93])
print(s1.marks)
print(s1.name)
s1.average()