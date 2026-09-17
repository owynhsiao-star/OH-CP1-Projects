#OH, period 1 Debugging with the debugger
# Ravager Snack Bar
import random
while True:
    try:
        pirate_name = str(input("What's your name, pirate? "))
        snack_name = str(input("What snack do you want? "))
        if:
        pirate_name==int
        else:
        print("Please input a word")
        break

price = random.randint(2, 8)  # random price in credits
while True: #You have to add a while True loop to make sure they give you a number
    try:
        quantity = (input("How many would you like? "))
    except:
        print("Please input a number")
    else:
        break
total = quantity * price
discounted_total = total - total * 0.10 #change 2 to total
tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)
print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) #snack_name needs to be the same here as in the variable 
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(discounted_total)+" credits")#you need to put total here not price
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") # Fixed syntax error: They forgot to add a )