#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            uppercase_char = ord(i) - 32
        else:
            uppercase_char = ord(i)

        print("{}".format(chr(uppercase_char)), end="")
    print("")
