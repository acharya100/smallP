age = 21
name = "om"

age = str(age)
age += "1"
print(age)
# age lai string ma convert garepachhi +1 garna khojda 21 rw 1 garera 211 hunchha string ma


is_student = False
name = "om"

name = bool(name)
print(name)
#kunae pani none empty string like name lai boolean ma convert garda name true hunchha


is_student = str(is_student)
print(is_student)
#is_student vanne boolean lai string ma convert garepachhi as a string false  hunchha

is_student = bool(is_student)
print(is_student)
#is_student vanne string lai boolean ma convert garepachhi as a boolean true hunchha


length = int(input("Enter value for length: "))
breadth = int(input("Enter value for breadth: "))

area = length * breadth
print(f"The area of rectangle is {area} cm^2")

