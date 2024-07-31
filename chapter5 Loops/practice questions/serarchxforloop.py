#search elemwnt x in this tuple using loop (linear search)
#(1,4,9,16,25,36,49,64,81,100)

x=36
tup=(1,4,9,16,25,36,49,64,81,100)
index=0
for val in tup:
    if(val==x):
        print("found at index:",index)
        break
    index+=1