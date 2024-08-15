# Without function


## Doing 6 factorial,
result = 1
## Starting from 1 because multiplication of 0 is 0
## Ending at 7 instead 6 because the range function excludes the limit
for i in range(1, 7):
    result *= i
print(result)


# Doing it with function 

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
    
    

print(factorial(5))

print(factorial(6))

print(factorial(7))

## Refer to the recursion.py file to see it being done with recursion.

