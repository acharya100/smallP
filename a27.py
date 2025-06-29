
# dictionary

student = {'name':'ram','age':23,'course':'bit'}

print(student)
print(student.get('age'))
print(student.get('caste'))
print(student.get('religion','not found'))

student.update({'name':'hari','phone_number': '333-444'})
print(student)

del student['age']
print(student)

teacher = {'name':'ramesh','age':43,'course':'bba'}

age = teacher.pop('age')
print(teacher)
print(age)



student_2 = {'name':'kumar','age':25,'course':'engineering','address':'jhapa'}

print(student_2.keys())
print(student_2.values())
print(student_2.items())

for key,values in student_2.items():
    print(key,values)