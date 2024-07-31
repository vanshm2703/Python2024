#wap to find the factorial of fist n numbers(using for)

n=int(input("enter the number:"))
fact=1

for el in range (1,n+1):
    fact*=el
print(fact)

# i=1
# while i<=n:
#     fact*=i
#     i+=1

# print(fact)