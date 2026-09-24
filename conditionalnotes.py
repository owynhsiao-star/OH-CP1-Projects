# VL Conditonal Notes
# Can I get ice cream = no, were about to have dinner
#Can I have ice cream = yes:
    #Can you drive me = no, go walk to the place
    #Can you drive me = Yes, lets go get ice cream
grade=int(input("What is your grade? "))
# Start every boolean statement with if
# end conditonal and boolean statements with a colon:
# when a line ends with a colon indent the next line
if grade >= 90:
    print ("Haha, ha, A")
elif grade>=70:
#Elif is literally just if the first if isnt true, check this if, if it's true, do this
    print("Do better, but you'll pass")
else:
    print("Ew")
#Very top line of a boolean should be the least possible answer
raining==False
if raining:
    print("bring me an umbrella")
else:
    print("Wear sunscreen")
#If a variable is guaranteed false, you don't need to write the boolean statement
#If it's an input you do 