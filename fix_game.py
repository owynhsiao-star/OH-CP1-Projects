#OH, period 1, fix the game assignment
import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        while True:
            try:
                guess = int(input("Guess a number between 1 and 20: "))
            except:
                print("Number please")
            else:
                break
        guesses = guesses + 1

        if guess == secret_number: #There was no colon, so the computer didn't know everything after was inside the if statement, also, and if always ends with a colon, it was a sytax error
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number and guess>-1:
            print("Too low!")
        elif guess > secret_number and guess<21:
            print("Too high!")
        elif guess>20:
            print("Below 21")
        elif guess<0:
            print("Above -1") 
    scores.append(guesses)

print("\n--- Game Over ---")
print("Your guesses per round: " , scores) #You cannot concatonate an integer with a string with a +, you need to use a ,

total = 0
for score in scores:
    total = total + score#There was a "total=0" inside the for loop so the program was resetting the score back to 0 every time the for loop ran, which prevented it from getting the actual average, this is a logic error.

average = total / rounds
print("Your average guesses per round was " + str(round(average,2)))

best_round = scores[0] 
for i in range(1, rounds): #There was a -1, this was a logic error, if the range is from 1 to rounds-1 then it excludes a number that it needs, you don't need anything after rounds
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")
