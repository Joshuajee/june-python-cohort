my_set = {1,30, 2, 7, 10, 15}

print(my_set)

my_set.add("banana")

print(my_set)

my_set.update({ 6, 8 })

print(my_set)

my_set.update([20, 25])

print(my_set)

my_set.update((21, 27))

print(my_set)

## Removing Items from a set

my_set.remove("banana")

print(my_set)

my_set.discard(21)

print(my_set)

my_set.discard(21)

my_set_2 = { 60, 70}

new_set = my_set.union(my_set_2)

print(my_set)

print(new_set)