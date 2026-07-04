# Question 1

student = {
    "name": input("Enter Name:"),
    "age": int(input("Enter Age:")),
    "City": input("Enter City:")
}
print(student)

# Question 2

student = {
    "name": "Abhishek",
    "age": 21,
    "course": "Python"
}

print(student.keys())

# Question 3
student = {
    "name": "Abhishek",
    "age": 21,
    "course": "Python"
}

print(student.values())

# Question 4

student = {
    "name": "Abhishek",
    "age": 21,
    "course": "Python"
}
for key, value in student.items():
    print(key, value)

# Question 5

student = {
    "name": "Abhishek",
    "age": 21,
    "course": "Python"
}
student.update({"City": "Jalandhar"})
print(student)

# Question 6

student = {
    "name": "Abhishek",
    "age": 21,
    "course": "Python"
}
student.update({"course": "Html"})
print(student)

# #Question 7
student = {
    "name": "Abhishek",
    "age": 21,
    "course": "Python"
}
student.pop("course")
print(student)

# Question 8
student = {
    "name": "Abhishek",
    "age": 21,
    "course": "Python"
}
student.pop("course")
print(student)
