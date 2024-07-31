# f=open("E:\\python\\chapter7 file input or output in python\\demo.txt","r")
# data=f.read(5)
# print(data)

# print(type(data))

# line1=f.readline()
# print(line1)

# f.close()

#with syntax

# with open("E:\\python\\chapter7 file input or output in python\\demo.txt","r") as f:
#     data=f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data")


#deleting a file 

import os
os.remove("E:\\python\\chapter7 file input or output in python\\sample.txt")