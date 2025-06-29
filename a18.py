# compond interest calculator

Principle = 0
Interest_rate = 0
Time = 0

while True:
    Principle = float(input("Enter the priciple amount: "))
    
    if Principle < 0:
        print("Principle cannot be zero or negative value!")
    else:
        break

while True:
    Interest_rate = float(input("Enter the Interest_rate amount: "))

    if Interest_rate < 0:
        print("Rate of interest cannot be zero or negative values!")
    else:
        break

while True:
    Time = float(input("Enter time required (in years): "))

    if Time < 0:
        print("Time cannot be zero or negative values!")

    else:
        break

Total_amount = Principle * pow((1+Interest_rate/100), Time)
print(f"The total amount of principle {Principle} in {Interest_rate} rate within {Time} years is: {round(Total_amount, 2)}")






principle = 0
interest_rate = 0
time = 0

while principle <=0 :
    principle = float(input("enter value of principle: "))
    
    if (principle <= 0):
        print("principle amount in this scenario cannot be zero or negative values")
    
    
while interest_rate <=0 :
    interest_rate = float(input("enter value for rate of interest: "))
    
    if (interest_rate <= 0):
        print("rate of interest in this scenario cannot be zero or negative values")


while time <= 0:
    time = float(input("enter the time involved (in years): "))
    
    if (time <= 0):
        print("time involved (in years) in this scenario cannot be zero or negative values")

        
total_amount = principle * pow((1+interest_rate/100), time)

print(f"The total amount fetched while giving {principle} as principle in {interest_rate} rate within {time} years is:{total_amount:.2f}")    