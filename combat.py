#OH, combat, period 1
#function for player class
#function for player turn
#function for enemy turn
#generate enemy and player turn numbers
import random
def playclass(r):
    bdamage=random.randint(1, 26)
    wdamage=random.randint(1, 8)
    rdamage=random.randint(1, 22)
    rogue=[20, 14, 85, rdamage]
    barbarian=[20, 16, 114, (bdamage+5)]
    wizard=[20, 12, 78, wdamage]
    classes=[]
def playturn(e):