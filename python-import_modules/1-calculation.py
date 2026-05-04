#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    print("{a} + {b} = {c}".format(a=a, b=b, c=cal.add(a, b)))
    print("{a} - {b} = {c}".format(a=a, b=b, c=cal.sub(a, b)))
    print("{a} * {b} = {c}".format(a=a, b=b, c=cal.mul(a, b)))
    print("{a} / {b} = {c}".format(a=a, b=b, c=cal.div(a, b)))
