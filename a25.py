#lists

course = ['math','nepali','english','social','arts']
course_2 = ['physics','chemistry','computer']

course.insert(2, course_2)
print(course)



course = ['math','nepali','english','social','arts']
course_2 = ['physics','chemistry','computer']

course.append(course_2)
print(course)



course = ['math','nepali','english','social','arts']
course_2 = ['physics','chemistry','computer']

course.extend(course_2)
print(course)

print('biology' in course)

course = ['math','nepali','english','social','arts']
course_2 = ['physics','chemistry','computer']

course.remove('math')
print(course)

popped = course_2.pop()
print(popped)
print(course_2)



nums = [2,6,3,4,1,5]

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

print(9 in nums)