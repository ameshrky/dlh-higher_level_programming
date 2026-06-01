#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)
print(load_from_json_file(filename))
print(type(load_from_json_file(filename)))
