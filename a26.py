#lists

course = ['english','computer','nepali','social','health']

for index, x in enumerate (course):
    print(index, x)

for index, x in enumerate (course, start=1):
    print(index, x)


courses = ['english','computer','nepali','social','health']

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)



course_2 = ['math','nepali','english','social','science']

print(course_2[1:])
print(course_2[:4])
print(course_2[:2:2])
print(course_2[1::2])