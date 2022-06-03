import math
a = float(input("Enter the first side(cm): "))
b = float(input("Enter the second side(cm): "))
d = float(input("Enter the angle between a,b(degree): "))
C = math.radians(d)
c = math.sqrt((a ** 2) + (b ** 2) - (2 * a * b * math.cos(C)))
print("c = ", c, "cm.")