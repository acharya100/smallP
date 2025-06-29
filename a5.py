import math

first_radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * first_radius

print(f"The circumference of the circle is {round(circumference, 3)} cm")




second_radius = float(input("Enter the radius of the circle: "))
area = math.pi * second_radius ** 2

print(f"The area of the circle is {round(area, 3)} cm^2")




p = float(input("Enter the value of p: "))
b=float(input("Enter the value of b: "))

h = math.sqrt(p**2 + b**2)
print(f"The hypotenuse of the right angled triangle is {h} cm")




a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

c = math.pow(a**3 + b**3, 1/3)
print(f"The cube root of the sum of cubes of (a^3+b^3) is {round(c, 3)}")