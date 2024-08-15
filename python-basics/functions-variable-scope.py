# Variable Scope
"""
Variables outside functions have global scope, 
while variables inside the functions have local scope.
"""

score = 60

def printScore():
    #global score will be printed
    print(score)
    
printScore()

def print_score_2():
    # this score variable inside this function is different from the one above,
    # that has a value of 60.
    score = 10
    print(score)

print_score_2()


# will print 60, because the global variable wasn't updated inside the function call
print(score)

def update_score():
    #The global keyword tells python that we want to use the global variable.
    global score
    score = 30
    
update_score()

print(score)