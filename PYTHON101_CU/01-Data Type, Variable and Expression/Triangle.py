import math
a = float(input("Enter the first side(cm): "))
b = float(input("Enter the second side(cm): "))
c = float(input("Enter the angle between a,b(degree): "))
area = (a * b * math.sin(math.radians(c))) / 2
print("The area of the triangle is: ", area, "sq cm")