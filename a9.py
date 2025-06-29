# temperature convertor

temperature = float(input("Enter value of temperature: "))
unit = input("Enter value of unit (c or f): ").lower()

if unit == "c":
    result = round((temperature*9)/5+32, 2)
    print(f"The temperature of patient is {result} fahrenheit")
elif unit == "f":
    result = round((temperature-32)*5/9, 2)
    print(f"The temperature of patient is {result} celsius")
else:
    print("the unit entered is invalid!")