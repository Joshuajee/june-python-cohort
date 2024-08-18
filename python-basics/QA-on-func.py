def display():
    print(1)
    print(2)
    print(3)
    
display()

def triangle():
    print("    *")
    print("   ***")
    print("  *****")
    print(" *******")
    print("*********")
    
triangle()
triangle()
triangle()

def add(x, y):
    z = x + y
    print(z, x, y)
    
add(10, 5)    

var1 = 90
var2 = 80

add(var1, var2)

add(y=var1, x=var2)





def sub(x, y):
    z = x - y
    return z
    
diff = sub(20, 15)

print(diff)

# x = input("What is x? ")

# y = print(x)

# print(y)

# def print_name(name):
#     print(f"Your name is {name}")
    
# print_name(input("what is your name? "))


def can_vote(age):
    if age >= 18:
        return "You can vote"

    return "You cannot vote"

print(can_vote(18))


print(can_vote(16))


def return_something():
    return 0
    return 2

print(return_something())