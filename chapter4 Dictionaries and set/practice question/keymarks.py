#WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary & add one by one . use subject name as a key marks as value.

marks={}

x=int(input("physics marks"))
marks.update({"phy":x})

y=int(input("maths marks"))
marks.update({"maths":y})

z=int(input("chem marks"))
marks.update({"chem":z})

print(marks)

