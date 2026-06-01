#!/usr/bin/python3
Student = __import__('9-student').Student

students = [
    Student("John", "Doe", 23),
    Student("Bob", "Dylan", 27)
]

for student in students:
    print(student.to_json())
