#functions

# def calc_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum

# calc_sum(5,10)


#function defination where a and b are parameters
# def calc_sum(a,b):
#     return a+b

# sum=calc_sum(10,5)
# print(sum)


# def print_hello():
#     print("hello")

# print_hello()


#average of 3 number

# def calc_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print("average is:",avg)
#     return avg

# calc_avg(1,5,16)


#default parameters

# def calc_prod(a=1,b=1):#default values or parameters
#     print(a*b)
#     return a*b

# calc_prod(10,20)
# calc_prod()


#recursion

# def show(n):
#     if(n==0):#base condition
#         return
#     print(n)
#     show(n-1)
#     print("end")

# show(5) #5,4,3,2,1

#factorial

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n

print(fact(5))