#WAP to find the greatest of 3 numbers entered by the user

a=int(input("enter first number:"))
b=int(input("enter Second number:"))
c=int(input("enter Third number:"))
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else:
    print(c)