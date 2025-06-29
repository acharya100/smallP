
# temperature = int(input("Enter current temperature: "))
# is_raining = False

# if temperature > 35 or temperature < 5 or is_raining:
#     print("Event will be cancelled!")
# elif temperature >= 20 and temperature <= 25:
#     print("it is perfect environment for event.")
# else:
#     print("Event won't be cancelled.") 




tapkram = int(input("Enter current tapkram: "))
is_sunny = True

if tapkram >= 15 and tapkram <=30 and is_sunny:
    print("perfect temperature to go outside.")
    print("it is sunny.")
elif tapkram >0 and tapkram <15 and is_sunny:
    print("it is cold outside.")
    print("it may or maynot be sunny")
elif tapkram > 30 and tapkram <55:
    print("it is very hot")
    print("it is dangerously sunny")
elif tapkram <= 0 and tapkram >= -30 and is_sunny:
    print("it is very cold outside")
    print("there won't be any chance of being sunny")
else:
    print("people will die")