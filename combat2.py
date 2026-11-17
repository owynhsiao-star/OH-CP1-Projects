#OH, period 1, combat
import random as r
barbarian=[16, 14, 34]
rogue=[18, 12, 30]
fighter=[17, 16, 32]
count=0
endgame=False
lasturndef=False
player=str(input("What is your name? "))
dif=input("What would you like the difficulty to be? ").strip().title()
clas=input('What class would you like to be, barbarian, fighter, or rogue? ').title().strip()
if clas=="Barbarian":
    clas=barbarian
if clas=="Rogue":
    clas=rogue
if clas=='Fighter':
    clas=fighter
if dif == "Hard":
    enemy="Orc"
    enhel=60
    enda=15
    ende=16
elif dif == "Normal":
    enemy="Soldier"
    enhel=30
    enda=12
    ende=13
elif dif == "Easy":
    enemy="Rabbit"
    enhel=1
    enda=-1
    ende=19
else:
     print("Not an option")
health=clas[2]
defense=clas[1]
av=clas[0]
def playturn():
    global enda, enhel, c, clas, defense, health, ende, endgame, lasturndef
    if lasturndef == True:
        ende-=5
        lasturndef=False
    c=input("would you like you like to attack, defend, heal, or flee ").title().strip()
    if c == "Attack":
        av=r.randint(1,20)
        if av>ende:
            enhel-=clas[0]
    elif c == "Defend":
        defense+=5
    elif c == "Heal":
        health+=10
    elif c == "Flee":
        print("You ran away")
        endgame=True
    else:
        print ("I'm skipping your turn")
    if health<1:
        print("You lose", player)
        endgame=False
def enturn():
    global enhel, endgame, enda, ende
    print(enemy)
    ch=r.randint(1,5)
    if ch == 1:
        print(enemy, " attacked!")
        nuhealth=health-enda
    elif ch == 2:
        ende+=5
        print("Enemy defended")
        lasturndef=True
    elif ch == 2:
        enhel+=10
    else:
        print("It ran away")
        endgame=True
    if enhel<1:
        print("You win ", player)
        endgame=True
while endgame==False:
    playturn()
    enturn()
    count+=1
