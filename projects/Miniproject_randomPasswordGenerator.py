import random
import string 

str=string.ascii_letters+string.digits+string.punctuation

pass_len=12
password=""
for i in range(pass_len):
    password+=random.choice(str)

print("your random password is :",password)    