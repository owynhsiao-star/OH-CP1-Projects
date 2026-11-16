#OH, period 1, combat
import random as r
barbarian=[16, 14, 34]
rogue=[18, 12, 30]
fighter=[17, 16, 32]
clas=input('What class would you like to be, barbarian, fighter, or rogue?').title().strip()
if clas=="Barbarian":
    clas=barbarian
if clas=="Rogue":
    clas=rogue
if clas=='Fighter':
    clas=fighter
dif=input("What would you like the difficulty to be? ").strip().title()
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
def playturn(n):
    bdamage=r.randint(1,10)
    if c == "Defend":
        dv-=5
    c=input("would you like you like to attack, defend, heal, or flee").title().strip()
    if c == "Attack":
        av=r.randint(1,(clas[0]))
        if av>ende:
            enhel-=bdamage
    elif c == "Defend":
        dv=clas[1]
        dv+=5
    elif c == "Heal":
        hv=clas[2]
        clas+=10
    elif c == "Flee":
        print("You ran away")
        break
    else:
        print ("I'm skipping your turn")
def enturn(h):
    print(enemy)
    ch=r.randint=(1,5)
    if ch == 1:
        at=random.randint
