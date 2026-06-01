#!/usr/bin/python3
Student = __import__('11-student').Student

student = Student("John", "Doe", 23)
print(student.to_json())

student.reload_from_json({
    "first_name": "Bob",
    "last_name": "Dylan",
    "age": 27
})

print(student.to_json())
