#WAF for n entered by the user to tell its odd or even

def odd_even(n):
    if(n%2==0):
        return "even"
    else:
        return "odd"

n=int(input("enter the number"))
result=odd_even(n)
print(result)