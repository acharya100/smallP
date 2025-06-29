
for a in range(1,11):
    print(a)
print("hello ok!")



for b in reversed(range(1,11)):
    print(b)
print("Happy birthday ok!")



for c in range(1,21,2):
    if c == 15:
        break
    else:
        print(c)

print("gap of 2")


for d in reversed(range(1,21,3)):
    if d == 13:
        continue
    else:
        print(d)

print("gap of 3")



phone_number = "1234-567-890"

for x in phone_number:
    print(x)