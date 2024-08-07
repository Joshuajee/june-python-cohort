grade = 100

if grade >= 70:
    print("A")
elif grade >= 60:
    print("B")
elif grade >= 50:
    print("C")
elif grade >= 40:
    print("D")
else:
    print("F")


print(grade)

print("A") if grade >= 70 else print("F")


#Tenary
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


print("=") if a == b else print("B")
# The above is same as the below

if a > b:
    print("A")
elif a == b:
    print("=")
else:
    print("B")

# same as     

if a > b:
    print("A")
else:
    if a == b:
        print("=")
    else:
        print("B")
        
    