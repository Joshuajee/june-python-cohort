print(10 == 10)
print(10 == 10.0)
print(10 == 7)

print(10 != 8)
print(8 != 8)

print(10 > 8)
print(10 > 11)

print(10 >= 10)
print(10 >= 11)
print(10 >= 8)

print(10 is 10)
print(10 is 10.0)

x = 10

y = 10.0

print(x is not y)


print(10 > 5 and 5 < 6) # True
print(10 > 50 and 5 < 6) # False
print(10 > 5 and 50 < 6) # False
print(1 > 5 and 50 < 6) # False
print(10 > 5 and 50 < 6 and 20 > 6) # False

print("====OR=====")

print(10 > 5 or 5 < 6) # True
print(10 > 50 or 5 < 6) # True
print(10 > 5 or 50 < 6) # True
print(1 > 5 or 50 < 6) # False
print(10 > 5 or 50 < 6 or 20 > 6) # True



print(not False)
print(5 == 5.0)
x = 5
y = 5.0
print(x is not y)
my_str = "Hello, World"

print("h" not in my_str)

my_list = [1, 3, 6, "3"]

print(5 in my_list)

result = (4 + 4) ** 2 / 3 * (2 + 6) - 5 
# 4 + 4 ** 2 / 3 * 8 - 5
# 4 + 16 / 3 * 8 - 5
# 4 + 5.33 * 8 - 5
# 4 + 42.64 - 5
# 41.64

print(4 + 4 ** 2 / 3 * (2 + 6) - 5  < 5 * 6)


print(5 is 5.0)