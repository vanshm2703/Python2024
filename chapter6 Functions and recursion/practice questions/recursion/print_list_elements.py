#WA recursive function to print all the elements in a list.(hint list and idex are the parameters)

def print_list(list,index=0):
    if(index==len(list)):
        return
    print(list[index],end=" ")
    print_list(list,index+1)

fruits=["banana","litchi","pineapple","mango"]
print_list(fruits)