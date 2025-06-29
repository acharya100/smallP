item = input("Enter name of item: ")
unit_price = float(input("Enter unit price of item per kg: "))
quantity = int(input("Enter quantity of item in total kg: ")) 

total_price = unit_price * quantity

print(f"The total price of {quantity} X {unit_price} is {total_price}")


first_adjective = input("Enter value for first adjective: ")
noun = input("Enter value for noun: ")
verb = input("Enter value for verb: ")
second_adjective = input("Enter value for second adjective: ")

print(f"Yesterday, I went to a {first_adjective} hotel")
print(f"In that hotel, I saw a {noun}")
print(f"That {noun} was {verb} strangely")
print(f"After seeing all this i felt {second_adjective}")