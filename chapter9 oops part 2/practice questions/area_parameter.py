#define a Circle class to create a circle with radius r using the constructor.
  #define an area() method of the class which calculates the area of the circle
  # Define a paameter() method of the class which allows you to calculate th parameter of the circle. 

class circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return (22/7)*self.radius**2
    
    def parameter(self):
        return 2 * (22/7)*self.radius
    
c1=circle(7)
print(c1.area())
print(c1.parameter())

    