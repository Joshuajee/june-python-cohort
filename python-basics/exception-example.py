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

def get_user_age():
    try:
        age = float(input("What is your age? "))
        print(age)
    except:
        print("Invalid! age must be a number")
        get_user_age()

get_user_age()