#calculator

operator = input("Enter a operator required (+,-,/,*): ")

first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))

if operator == "+":
    result = first_num + second_num
    print(f"The sum of {first_num} and {second_num} is {result}")
elif operator == "-":
    result = first_num - second_num
    print(f"The difference of {first_num} and {second_num} is {result}")
elif operator == "*":
    result = first_num * second_num
    print(f"The product of {first_num} and {second_num} is {round(result, 3)}")
elif operator == "/":
    result = first_num / second_num
    print(f"The division of {first_num} and {second_num} is {round(result, 3)}")
else:
    print("Invalid operator bastards")