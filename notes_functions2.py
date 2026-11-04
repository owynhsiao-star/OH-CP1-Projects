def birthday(): #def defines it as a function, what's in the parenthesis are the parameters, and birthday is the name of the new keyword
    print("happy birthday to you") #this is what the function does
birthday()
birthday() #Calling the function, by its name and requirements
print("Happy Birthday Dear Owyn")
birthday()

name=input("What's your name?")
def birthday(name): #name is now the parameter, when you call the variable you need to also state what the parameter is
    print("Happy birthday to you")
    print("Happy Birthday to you")
    print(f"Happy birthday dear {name}")
    print("Happy birthday to you")
birthday(name)

#Keywords and names and parameters and such
#Parameter: A variable that exists exclusively inside the function, the function cannot run without the parameters filled
#a local variable is only in the function, global is only outside the function
#Arguements are what go inside the parenthsis when you call it, in the below scenario the parameter is (name) and the arguement is (owyn)
def birthday(name):
    print("Happy birthday to you")
    print("Happy Birthday to you")
    print(f"Happy birthday dear {name}")
    print("Happy birthday to you")
birthday("owyn")

def birthday(name="dad"): #Now if I don't give an arguement it'll give dad
    print("Happy birthday to you")
    print("Happy Birthday to you")
    print(f"Happy birthday dear {name}")
    print("Happy birthday to you")
birthday()

def birthday(name, age): #you can have multiple parameters  and numbers but the numbers of them must match
    print("Happy birthday to you")
    print("Happy Birthday to you")
    print(f"Happy birthday dear {name}")
    print("Happy birthday to you")
    print(f"You're now {age} years old")
birthday("owyn", "15") #The position of the argument has to match the parameter, the first goes to the first and the second goes to the second

def birthday(name="Dad", age="50"): #You can have multiple defaults, but if you set one you need to have all the parameters after also have defaults, but before doesn't matter
    print("Happy birthday to you")
    print("Happy Birthday to you")
    print(f"Happy birthday dear {name}")
    print("Happy birthday to you")
    print(f"You're now {age} years old!")
birthday()

#A function in general is a block of named code to be used again, a named action
#A function is for organization and speed
#You write def, say the name with parameters, tab over on the next line and write what it does
#Keyword: Functions should have a keyword that tells them exactly what the code does, it also takes big problems and breaks them into smaller stuff, it makes code reusable, and can be used many a time, the last is abstraction, you should be able to use a function without knowing how to use the insides by wrapping it in a name
#Functions increase readability because they simplify large blocks of code

#RETURN returns a specific value, can return as many as you want if seperated by commas but generally returns one

def supidpoof(user_answer, correct_answererer):
    user_answer=user_answer.strip().title()
    if user_answer in correct_answererer:
        return user_answer
    else:
        return False
