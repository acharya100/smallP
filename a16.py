
name = input("Enter your name: ")

while name == "":
    print("name cannot be empty")
    name = input("Enter your name: ")

print(f"Your name is {name}")



age = int(input("Enter your age: "))

while age < 0:
    print("enter valid age.")
    age = int(input("Enter your age: "))

print(f"The age of user is {age}")




while True:
    umer = input("Enter age of user: ")

    if umer == "":
        print("age cannot be empty")
    elif umer.isdigit() and int(umer) >= 0:
        age = int(umer)
        print(f"The age of user is {umer} years old.")
        break
    else:
        print("Enter a non-negative number.")