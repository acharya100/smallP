age = int(input("Enter your age: "))

if age>=18 and age<100:
    print("You are able to register.")
elif age<0:
    print("This age is invalid or the person is not born yet.")
elif age>=100:
    print("Party is over grandpa you can retire asshole.")
else:
    print("You are not able to register.")




response = input("Do you want some beer?: ").lower()
if response == "yes":
    print("Here take your beer.")
elif response == "no":
    print("No problem, you can have a soft drink.")
else:
    print("You have not responded yet asshole.")



name = input("Enter your name: ")
if name == "":
    print("You have not entered your name.")
else:
    print(f"Hello MR. {name}")




is_working = True
if is_working:
    print("This switch board is apppicable.")
else:
    print("It is not applicable.")



is_student = False
if is_student == False:
    print("You are a student.")
else:
    print("You are not a student.")