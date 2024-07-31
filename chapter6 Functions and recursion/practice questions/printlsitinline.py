#WAF to print the elements of a list in a straight line

cities=["delhi","mumbai","chennai","noida","gurgaon","pune"]
heroes=["thor","captain America","hulk","ironman"]
def print_el(list):
    for el in list:
        print(el,end=" ")
        
print_el(heroes)
print_el(cities)

