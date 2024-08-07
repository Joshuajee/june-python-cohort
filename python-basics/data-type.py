age = '50'
speed = "30.0"
name = "Jon Doe"
is_alive = False

print(type(age))
print(type(speed))
print(type(name))
print(type(is_alive))

is_alive = 10

print(type(is_alive))

my_list = [1, 4, 8, "Hello", True, [1, 2, 5]]

print(type(my_list))


print(my_list[0])
print(my_list[3])
print(my_list[5][1])

second_list = my_list[5]

print(second_list[1])

my_list[1] = 20

print(my_list)

my_tuple = (1, 2, 3, "Hello")

print(my_tuple[2])


my_list_1 = [1, 2, 3]
my_list_2 = [4, 5, 6]

#my_list_1.extend(my_list_2)

#print(my_list_1 + my_list_2)

my_dic = {
    "name": "Howard",
    "age": 70,
    "is_alive": True
}

print(my_dic["name"])
print(my_dic["age"])
print(my_dic["is_alive"])

my_dic["age"] = 71

print(my_dic)

my_set = { 1, 3, 4, 1, 1, 1, 1, 1.0, 6, 7,"hello"}

print(my_set)

none = None

ola = None

