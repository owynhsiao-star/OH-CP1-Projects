# OH, period 1 Crew shares assignment
while True:
    try:
        crewsize=int(input("How many crew members are there? "))
    except:
        print("Please input a number")
    else:
        break
import random
randnum=random.randint(0,5000)
numsubtract=crewsize*3
randnumnew=randnum-numsubtract
yonducut=randnumnew*.13
randnumnewer=randnumnew-yonducut
petercut=randnumnewer * .11
randnumnewest=randnumnewer-petercut
fullcrew=crewsize+2
crewshares=randnumnewest/fullcrew
yondushare=yonducut+crewshares
petershare=petercut+crewshares
print(f"Unit number: " + str(randnum))
print(f'Yondu\'s share: '+ str(round(yondushare, 2)))
print(f"peter\'s share: " + str(round(petershare, 2)))
print(f"crew member\'s shares: " + str(round(crewshares, 2)))

