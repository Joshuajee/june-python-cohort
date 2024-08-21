def div(x, y):
    if y == 0:
        raise Exception("Y should not be zero")
    return x / y

def div_with_type(x, y):
    if y == 0:
        raise ZeroDivisionError("Y should not be zero")
    return x / y

print(div(10, 2))

try:
    print(div(10, 0))
except:
    print("ERROR")