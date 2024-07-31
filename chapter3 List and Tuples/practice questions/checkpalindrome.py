#WAP to check if alist contains a palindrome of elemnets. (hint: use copy() method)

list=[1,2,3,2,1]
copylist=list.copy()
copylist.reverse()
if(list==copylist):
    print("palindrom")
else:
    print("not a palindrom list")