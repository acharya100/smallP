food = input("enter the food you like(q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("enter another food you like(q to quit): ")
print("i quit!")



number = int(input("Enter number between 1 and 10: "))

while number <= 0 or number >= 10:
    print(f"{number} is not required!")
    number = int(input("Enter another number between 1 and 10: "))

print(f"The number {number} is valid")