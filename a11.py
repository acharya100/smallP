temperature = int(input("Enter current temperature: "))
is_sunny = False

if 5 <= temperature <=35 and not is_sunny:
    print("It is nice weather.")
    print("it is cloudy")
elif 35 < temperature < 55 and is_sunny:
    print("It is very hot")
    print("It is extremely sunny")
elif -29<=temperature<=4 and not is_sunny:
    print("it is very cold weather.")
    print("it is gloomy with black clouds and fog")
else:
    print("people will die.")

# in elif 35 < temperature < 55 and is_sunny ma and use gariyeko le sabae match hunuparchha tara is_sunny match hudaina
# teivara else ko condition execute hunchha


# print(help(str))