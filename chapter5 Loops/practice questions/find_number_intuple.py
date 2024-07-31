#search number x in the tuple using loop
#(1,4,9,16,25,36,49,64,81,100)

tup=(1,4,9,16,25,36,49,64,81,100)
i=0
x=36
while (i<len(tup)):
    if(tup[i]==x):
        print("Found at index:",i)
        break
    else:
        print("finding..")
    i+=1


