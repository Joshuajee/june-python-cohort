single_str = "This is my string"
print(single_str)
mutiline_ste = '''
    This is my multiline 
    string

'''

print(mutiline_ste)

print(single_str[3])

print(len(single_str))

print(single_str[len(single_str) - 1])


for x in single_str:
    print(x)
    
print("sih" not in single_str)


# String slicing

print(single_str[0:4])
print(single_str[:4])

print(single_str[11:17])
print(single_str[11::2])


boy = "This is a boy"


print(boy[-8:-6])

print(boy.upper())
print(boy.lower())

print(boy.endswith("boy"))


print("      Hello World      ".replace("ll", "b"))
print("      Hello World      ".strip())

print("5.5".isnumeric())

csv = "1,2,3,4,5,6,7,8"


print(csv.split(","))

wsv = "1 2 3 4 5 6 7 8"

print(wsv.split(" "))

first_name = "Jon"
last_name = "Doe"

full_name = first_name + " " + last_name

print(full_name * 4)



# STRING FORMART

quantity = 3
itemno = 567
price = 49.95

order = "I want to pay {} dollars for {} pieces of item {}" 

print(order.format(price, quantity, itemno))

order2 = "I want to pay {1} dollars for {2} pieces of item {0}" 

print(order2.format(itemno, price, quantity))

order3 = "I want to pay {0} dollars for {1} pieces of item, {0} is a steal for {1} items" 

print(order3.format(price, quantity))


print("Jon said \"Be Kind\"")


txt = "Albert Einstein said \"Everybody is a Genius. But If You Judge a Fish by Its Ability to Climb a Tree, It Will Live Its Whole Life Believing that It is Stupid\" "


print(txt)