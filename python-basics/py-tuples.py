my_tuple = (1, 2, 7, "Hello", 1, 3, 4, { "some": 2})

print(my_tuple[5])


# Items in tuples cannot be reassigned
# my_tuple[5] = 90

print(my_tuple)

my_tuple[-1]["some2"] = 9

print(my_tuple)

my_tuple[-1] = {}