i = 1
while i < 6:
  print(i)
  i += 1
  
  
ask_question = True


while ask_question:
    name = input("Please enter your name or enter q to quit ")
    if name == "q":
        ask_question = False
        continue
    print(f"Your name is {name}")