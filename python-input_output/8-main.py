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
