username = input("Enter your username: ")

if len(username) > 12:
    print("username can't have more that 12 characters.")
elif " " in username:
    print("username shouldnot have spaces")
elif any(c in "0123456789" for c in username):
    print("username cannot contain digits")
else:
    print(f"{username} is correct")
