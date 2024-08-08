my_list = [1, 2, 7, "Hello", (1, 3, 4)]

print(my_list)

print(len(my_list))

print(my_list[2])

my_list[3] = 8

print(my_list)

print(my_list[-2])

## List Slicing
# list[start:end:step] start index is inclusive, end index is exclusive
# 

print(my_list[0:3])
print(my_list[:3])

print(my_list[1:])
print(my_list[1:5])

print(my_list[0::2])


## List Methods

my_list.insert(2, [3, 4, 6])

print(my_list)

my_list.append("hello")

print(my_list)

# Swaping item in index 0 and 6
my_list[0], my_list[6] = my_list[6], my_list[0]

# Swaping item in index 0 and 6
temp = my_list[0]
my_list[0] = my_list[6]
my_list[6] = temp

print(my_list)

# extending list
my_list.extend([2, 3, 4, 5, 5])

print(my_list)

my_list = my_list + ["Hello", "Good"]

print(my_list)

my_list.remove("hello")

print(my_list)

my_list.pop()

print(my_list)

my_list.pop(2)

del my_list[4]

my_list.pop()

print(my_list)

my_list.sort(reverse=True)

print(my_list)

print(my_list.count(5))

#my_list.clear()

print(my_list)

list_2 = ["Apple","Mango", "Banana", "Cherry"]

list_2.sort(reverse=True)

print(list_2)

## Looping throug a list

for fruit in list_2:
    if fruit == "banana":
        print(fruit)
        
total = 0    
empty_list = []    
for x in my_list:
    total += x
    empty_list.append(x * 3)


print(total)
print(total / len(my_list))
print(empty_list)


for i in range(len(my_list)):
    my_list[i] += my_list[i]


print(my_list)

new_list = [x for x in my_list if x == 10]

print(new_list)


new_list2 = []

for x in my_list:
    if x == 10:
        new_list2.append(x)
        
print(new_list2)

# [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]