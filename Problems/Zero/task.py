n = int(input())
denominator = int(input())
try:
    res = (n // denominator)
except ZeroDivisionError:
    print("Division by zero is not supported")
else:
    print(res)