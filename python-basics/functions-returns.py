def func():
    print("Hello, World!")
    print("How is it going.")
    print("Hope all is well")
    
func()
func()

def greetings(name):
    print("Goodmorning", name)
    
greetings("John")
greetings("Mike")

def add(x, y):
    print(x + y)
    
    
add(10, 5)

add(10, 8)

def add_or_ten(x, y = 10):
    print(x + y)
    
add_or_ten(3)

add_or_ten(2, 3)

def full_name(fname, lname):
    print(fname, lname)
    
full_name("John", "Doe")


full_name(lname="Doe", fname="John")

full_name(lname='Doe', fname='John')


#Arbituary arguments

def args(*values, index = 0):
    print(values)
    print(values[index])
    
    
args(1, 3, 4, 5, 6, 7, 8, 10, 8 ,9)

args(6, 7, 8, 9, 10, index=3)

print('hello', "3", 5, sep="*",)