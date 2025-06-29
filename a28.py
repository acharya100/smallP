nums = [1,3,4,2,5]
nums.sort()
print(nums)

for num in nums:
    if num == 3:
        print('got it')
        continue
    print(num)


nums_2 = [6,7,8,9,10]

for num in nums:
    for letter in 'def':
        print(num,letter)


for i in range(1, 11):
    print(i)


x = int(input("Enter a number: "))

while(x<10):
    print(x)
    x+=1


y = int(input("Enter a number: "))

while(y<10):
    if y == 7:
        print("found it")
        break
    print(y)
    y+=1