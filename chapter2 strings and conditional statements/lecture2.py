# str1="this is the string.\nwe are creating it in python"
# print(str1)

#concatination

# str1="vansh"
# str2="mehta"
# finalstring=str1+" " +str2
# print(finalstring)
# print(len(str1))
# print(len(str2))
# print(len(finalstring))

#indexing

# str="vansh mehta"
# print(str[6])

#Slicing

# str="vansh mehta"
# print(str[1:4])
# print(str[6:len(str)])
# print(str[:4])
# print(str[1:])

# str2="apple"
# print(str2[-5:-1])


#string function

# str= "i am studying python from apnacollege"
# print(str.endswith("er."))#returns true if string ends with substr
# print(str.capitalize())#capitalize first character
# print(str.replace("python","javascript")) #replaces all occurences of old with new
# print(str.find("am")) #returns 1st index of first occurences
# print(str.count("am"))#counts the ocuurence of substr in string

#conditionals

# age=21

# if(age>=18):
#     print("can vote and apply for licence")
#     print("can drive")


# light="green"

# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# elif(light=="yellow"):
#     print("look")

# print("code end")

# marks=int(input("Enter you Marks:"))
# if(marks >= 90):
#     grade="A"
# elif(marks >=80 and marks <90):
#     grade="B"
# elif(marks >=70 and marks <80):
#     grade="C"
# else:
#     grade="D"

# print("Grade of the student is: ",grade)


#Nesting

age=21

if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")