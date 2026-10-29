#OH, period 1, Pasword strength
capital=False
notsocapital=False
digidigi=False
specialchar=False
while True:
    score=0
    while True:
        try:
            password=list(input("What would you like as a password? "))
        except:
            print("A password with letters please")
        else:
            break
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
        score+=1
    if score==0:
        print("You didn't enter a password")
    if score==1 or score==2:
        print("Weak ", score)
    if score==3:
        print("Moderate ", score)
    if score==4:
        print("Strong ", score)
    if score==5:
        print('Very strong ', score)