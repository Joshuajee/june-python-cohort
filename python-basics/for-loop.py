my_list = [1, 5, 6, 7, 8, 90]
empty_list = []

my_tuple = (10, 40, 50, 3, 4, 60, 7)
empty_tuple = []

for x in my_list:
    print(x)
    empty_list.append(x)
    print(empty_list)
    if x == 7:
        break

    
print(empty_list)

for x in my_tuple:
    print(x)
    if x < 10:
        continue
    empty_tuple.append(x)
    
print(empty_tuple)


# 0 to (100 - 1), increment by 1
for i in range(100):
    print(i)

# 50 to (100 - 1) increment by 1    
for i in range(50, 100):
    print(i)
    
# 10 to (100 - 1) increment by 5
for i in range(10, 100, 5):
    print(i)
 
print(my_list)
    
for i in range(len(my_list)):
    #my_list[i] = my_list[i] * 2
    my_list[i] *= 2
    
    
print(my_list)


for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
  
##NESTED FOR LOOP

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
nums = [1, 2, 3]
for x in adj:
  for y in fruits:
    for z in nums:
        print(x, y, z)