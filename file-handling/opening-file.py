my_file = open("./text.txt", "r")

print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

my_file.close()

print(my_file.read())