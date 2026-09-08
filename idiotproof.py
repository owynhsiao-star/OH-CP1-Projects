#OH, idiotproof project

firstname=input("what is your first name ").strip().title()
lastname=input("what is your last name ").strip().title()
firstseperated=firstname.split()
firstfixed="".join(firstseperated)
lastseperated=lastname.split()
lastfixed="".join(lastseperated)
fullname=firstfixed.title() + " " +lastfixed.title()
print("Name: " + fullname)

while True:
    try:
        phone=int(input("What is your phone number? "))
    except:
        print("Phone NUMBER without dashes")
    else:
        break
    space=" "
phone=phone[3]+
print(f"phone number: " +phone)


