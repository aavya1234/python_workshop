student={'name': 'aavya', 'age': 26, 'grade': 'A', 'city': 'new york'}
del student["grade"]
print(student)
#del student["phone"]
#print(student)
for key in student.keys():
    print(f"{key}")
for value in student.values():
    print(f"{value}")
for key,value in student.items():
    print(f"{key}:{value}")
del student["age"]
print(student)
student["address"]="mathura"
print(student)
name=student.get["name"]
print(name)


squares={num:num**2 for num in range(1,6)}
print(squares)
cubes={num:num**3 for num in range(1,6)}
print(cubes)