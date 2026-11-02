import random
number=random.randint(1, 1000000)
print(f"Your random number is: {number}")
#The first number in parenthesis is the lowest arguement, and the last is the highest arguement
#If you didn't use import the program wouuldn't know what "random" is, as it's not a regular function like print or input
#There is no real randomness in computer science, as they follow algorithms that have a set patters.
#Random calls on a library/module, "import random" pulls a bunch of prebuilt code from somewhere else to use the function
#The return of a function is the info it gives back to you
#random.choice does the same but with strings

baseballs = random.randrange(33,1000000000000000000000009,52)
print(f"I have {baseballs} baseballs")
#first number is a starting point, second is ending point which is not included, hence why it's different from randint, third number is what you are counting by
forkliftcertifications=random.random()
print(f"You have {forkliftcertifications:.2} at home")
#random.random gives a random decimal (float) between 0 and 1
