#OH, period 1, Pasword strength

score=0
while True:
    try:
        password=str(input("What would you like as a password?"))
    except:
        print("A password with letters please")
    else:
        break
if 8<=len(password):
    score += 1
    print(score)
