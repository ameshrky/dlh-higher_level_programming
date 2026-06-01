#!/usr/bin/python3
Student = __import__('10-student').Student

student = Student("John", "Doe", 23)
print(student.to_json())
print(student.to_json(["first_name", "age"]))
print(student.to_json(["middle_name", "age"]))
