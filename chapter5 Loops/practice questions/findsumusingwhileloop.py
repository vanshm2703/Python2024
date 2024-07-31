#wap to find sum of first n numbers.(using while)

n=int(input("enter the value of n"))
sum=0
i=1

while i<n:
    sum+=i
    i+=1

print("total sum:",sum)
