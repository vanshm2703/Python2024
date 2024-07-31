#WAF to find factorial of n.(n is the parameter)

def find_fact(n):
    fact=1
    for el in range(1,n+1):
        fact*=el
    print(fact)

find_fact(5)


