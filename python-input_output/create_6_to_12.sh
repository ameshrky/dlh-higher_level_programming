#!/bin/bash

cat > 6-load_from_json_file.py <<'PY'
#!/usr/bin/python3
"""Load object from JSON file."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
PY

cat > 6-main.py <<'PY'
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)
print(load_from_json_file(filename))
print(type(load_from_json_file(filename)))
PY

cat > 7-add_item.py <<'PY'
#!/usr/bin/python3
"""Add arguments to a Python list and save them to a file."""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
PY

cat > 7-main.sh <<'SH'
#!/bin/bash
rm -f add_item.json
./7-add_item.py Best School
cat add_item.json
echo ""
./7-add_item.py 89 Python C
cat add_item.json
echo ""
SH

cat > 8-class_to_json.py <<'PY'
#!/usr/bin/python3
"""Return dictionary description of an object."""


def class_to_json(obj):
    """Return the dictionary description with simple data structures."""
    return obj.__dict__
PY

cat > 8-main.py <<'PY'
#!/usr/bin/python3
class_to_json = __import__('8-class_to_json').class_to_json

class MyClass:
    number = 89

    def __init__(self, name):
        self.name = name

m = MyClass("John")
m.number = 12
print(type(class_to_json(m)))
print(class_to_json(m))
PY

cat > 9-student.py <<'PY'
#!/usr/bin/python3
"""Student class."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of Student."""
        return self.__dict__
PY

cat > 9-main.py <<'PY'
#!/usr/bin/python3
Student = __import__('9-student').Student

students = [
    Student("John", "Doe", 23),
    Student("Bob", "Dylan", 27)
]

for student in students:
    print(student.to_json())
PY

cat > 10-student.py <<'PY'
#!/usr/bin/python3
"""Student class with filtered JSON."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation, optionally filtered by attrs."""
        if isinstance(attrs, list):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__
PY

cat > 10-main.py <<'PY'
#!/usr/bin/python3
Student = __import__('10-student').Student

student = Student("John", "Doe", 23)
print(student.to_json())
print(student.to_json(["first_name", "age"]))
print(student.to_json(["middle_name", "age"]))
PY

cat > 11-student.py <<'PY'
#!/usr/bin/python3
"""Student class with reload from JSON."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation, optionally filtered by attrs."""
        if isinstance(attrs, list):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of Student from json dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
PY

cat > 11-main.py <<'PY'
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
PY

cat > 12-pascal_triangle.py <<'PY'
#!/usr/bin/python3
"""Pascal triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
PY

cat > 12-main.py <<'PY'
#!/usr/bin/python3
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

print_triangle(pascal_triangle(5))
PY

chmod +x 6-main.py 7-add_item.py 7-main.sh 8-main.py 9-main.py 10-main.py 11-main.py 12-main.py
chmod +x 6-load_from_json_file.py 8-class_to_json.py 9-student.py 10-student.py 11-student.py 12-pascal_triangle.py
