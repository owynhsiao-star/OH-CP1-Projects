#OH, period 1, Pasword strength

while True: #This while true loop is so you can enter a new password if you don't like yours
    capital=False
    notsocapital=False
    digidigi=False
    specialchar=False
    score=0
    password=list(input("What would you like as a password? (if you wanna end the program type \"end\") "))#From the while true loop to here is just for resetting all the variables
    if 8<=len(password):
        score += 1
    for i in password:
        if str.isupper(i):
            capital=True
    if capital==True:
        score+=1
    for i in password:
        if str.islower(i):
            notsocapital=True
    if  notsocapital==True:
        score+=1
    for i in password:
        if str.isdigit(i):
            digidigi=True
    if digidigi==True:
        score+=1
    for i in password:
        if i=="!" or i=="@" or i=="#" or i=="$" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")" or i=="_" or i=="+" or i=="-" or i=="=" or i=="[" or i=="]" or i=="{" or i=="}" or i=="|" or i==";" or i==":" or i=="." or i=="," or i=="<" or i==">" or i=="?":
            specialchar=True
    if specialchar==True:
        score+=1    #From the first if statement to here checks to see if all the requirements are met
    if password==["e", "n", "d"] or password==["E", "n", "d"]:
        print ("Bye")
        break
    if score==0:
        print("You didn't enter a password")
    if score==1 or score==2:
        print("Weak ", score)
    if score==3:
        print("Moderate ", score)
    if score==4:
        print("Strong ", score)
    if score==5:
        print('Very strong ', score)#From the if statement with lists to here is for printing the strength of the password or ending the program
    