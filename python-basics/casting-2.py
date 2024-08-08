"""
CASTING LISTS, TUPLES, SETS, AND DICTIONARIES
"""

my_list = [1, 2, 3, 5]
my_tuple = (1, 2, 3, 5)
my_set = {1, 2, 3, 5}

# list

list_to_tuple = tuple(my_list)

print(list_to_tuple)
print(type(list_to_tuple))

list_to_set = set(my_list)

print(list_to_set)
print(type(list_to_set))


# tuples

tuple_to_list = list(my_tuple)

print(tuple_to_list)
print(type(tuple_to_list))

tuple_to_set = set(my_tuple)

print(tuple_to_set)
print(type(tuple_to_set))


## Dictionary

my_dict = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2009,
    "doors": 4,
}

print(list(my_dict))

print(tuple(my_dict))

print(set(my_dict))

list_to_dict_example = [
    ("name", "John Doe"),
    ("age", 20),
    ["school", "UI"],
    [40, 8]
]

print(dict(list_to_dict_example))

