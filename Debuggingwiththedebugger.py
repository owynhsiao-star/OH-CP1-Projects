#OH, period 1 Debugging with the debugger
# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
pirate_name: int
print("Please input a word")

snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
while True: #there needs to be a while true loop to make sure they input a number
    try:
        quantity = int(input("How many would you like? "))
    except:
        print("please input a number")
    else:
        break

total = price * quantity

discounted_total = total - total * 0.10 #2 needs to be changed to total

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) #this needs to have the variable snack_name not snackName
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(discounted_total))#This should be discounted_total not price
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") #There needs to be a ) here