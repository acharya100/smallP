
# lists

fruits = ["apple","mango","orange","banana","guava","papaya"]

print(fruits[::2])

print(fruits[::-1])

for x in fruits:
    print(x)

print(len(fruits))

print("pineapple" in fruits)

print(fruits.index("guava"))


cars = ["tata","maruti","suzuki","audi"]

cars.append("bmw")
print(cars)

cars.insert(2,"scorpio")
print(cars)

cars[1] = "nano"

for car in cars:
    print(car)



bikes = ["honda","hero","pulsar","bullet","duke"]

print(bikes.count("honda"))

bikes.sort()
print(bikes)

bikes.reverse()
print(bikes)