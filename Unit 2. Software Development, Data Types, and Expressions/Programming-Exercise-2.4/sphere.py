# Put code here
#user import
radius = float(input("Radius: "))
import math

#math stuff
diameter = (2*(radius))
circumference = ((diameter) * math.pi)
surfaceArea = (4 * (math.pi) *(radius)**2)
volume = ((4/3) * (math.pi) * (radius)**3)

#output
print("Diameter : ", (diameter))
print("Circumference: ", (circumference))
print("Surface area: ", (surfaceArea))
print("Volume: ", (volume))


