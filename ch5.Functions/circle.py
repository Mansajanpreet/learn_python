# The circle module has function that perform
# calculations related to circles.
import math

# The area function accepts a circle's radius as an 
# argument and return the area of the circle.
def area(radius):
    return math.pi * radius**2

# The circumference function accpets a circle's
# radius and returns the circle's circumference.
def circumference(radius):
    return 2 * math.pi * radius

area()