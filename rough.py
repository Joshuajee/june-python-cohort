x = 10

y = 2

try:
    z = x / y
    print(z)
    print(z + "")
except ZeroDivisionError:
    print("Zero Error")
except:
    print("Error")
finally:
    print("DONE")


print("Another one")