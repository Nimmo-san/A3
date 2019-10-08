
import math

s = float(input("Enter a float: "))
c = float(input("Enter a float: "))
print("Angle: ", math.atan(s/c) * 180/math.pi)
print("Hypotenuse: ", math.sqrt(math.pow(s, 2) + math.pow(c, 2)))
