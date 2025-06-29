#weight conversion

weight = float(input("Enter value for weight: "))
unit = input("Enter the value of unit (kgs or lbs): ").lower()

if unit == "lbs":
    result = weight/2.205
    new_unit = "kgs"
    print(f"The weight of the person is: {round(result, 2)} {new_unit}")
elif unit == "kgs":
    result = weight * 2.205
    new_unit = "lbs"
    print(f"The weight of the person is: {round(result, 2)} {new_unit}")
else:
    print("The user has entered wrong unit")