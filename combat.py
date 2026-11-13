#OH, combat, period 1
#function for player class
#function for player turn
#function for enemy turn
#generate enemy and player turn numbers
import random
fist=random.randint(1, 15)
bdamage=random.randint(1, 30)
wdamage=random.randint(1, 18)
rdamage=random.randint(1, 22)
rogue=[14, 85, rdamage, fist]
barbarian=[(random.randint(9, 20)),16, 114, (bdamage+5), fist+5]
wizard=[12, 78, wdamage, fist-5]
classess=str(input('Would you like to bea wizard, a rogue, or a barbarian')).title().strip()
dif=str(input("Hard, normal, or easy enemy"))
if dif == "Hard":
    enemy="Orc"
    enhel=random.randint(100, 190)
    enda=random.randint(30, 60)
    ende=random.randint(15, 18)
if dif == "normal":
    enemy="Soldier"
    enhel=random.randint(75, 140)
    enda=random.randint(20,40)
    ende=random.randint(10, 15)
if dif == "Easy":
    enemy="Rabbit"
    enhel=1
    enda=-1
    ende=19
classes=[rogue, wizard, barbarian]
one=[random.randint(1,8) * 4]
two=[random.randint(1,6) *8]
three=[random.randint(1, 6) *5 +random.randint[1,4]*3]
def playturn(e):
    if classess=="Barbarian":
        classess=barbarian
    elif classess=="Wizard":
        classess=wizard
    elif classess=="Rogue":
        classess=rogue
    else:
        print("Choose a class")
    if not classess == wizard:
        choice=str(input("Would you like to attack, defend, or heal? ")).strip().title()
    elif classess == wizard:
        choice=str(input("Would you like to attack, cast a spell, or heal? "))
    if choice=="Attack":
        choiceattack=str(input("Weapon or fist")).strip().title()
        if choiceattack=="Weapon":
            attackroll=classess[0]
            if attackroll>ende:
                attackdamage=classess[3]
        if choiceattack=="Fist":
                attackdamage=classess[4]
    elif choice=="Defend":
            defense=classess[1]+5
    elif choice=="Heal":
            classess[2]+=5
    else:
         print("Choose one of the presented options")



