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
def playturn(n):
    bdamage=r.randint(1,10)
    c=input("would you like you like to attack, defend, heal, or flee").title().strip()
    if c == "Attack":
        damage=
