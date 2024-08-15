def factorial(num):
    if num > 1:
        return  num * factorial(num - 1)
    else:
        return 1

# fac(4)    
# 4 * fac(3)
# 4 * 3 * fac(2)
# 4 * 3 * 2 * fac(1)
# 4 * 3 * 2 * 1

print(factorial(5))
