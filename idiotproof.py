#OH, idiotproof project

firstname=input("what is your first name ").strip().title()
lastname=input("what is your last name ").strip().title()
firstseperated=firstname.split()
firstfixed="".join(firstseperated)
lastseperated=lastname.split()
lastfixed="".join(lastseperated)
fullname=firstfixed.title() + " " +lastfixed.title()


while True:
    phone=(input("What is your phone number? "))
    if len(phone)==10:
        if phone.isdigit():
            break
    print("Only numbers, exactly ten letters, no spaces or dashes")
fixed = phone[:3] + " " + phone[3:6] + " " + phone[6:]


while True:
    gpa=(input("What is your gpa? "))
    if "." in gpa:
        parts=gpa.split(".")
        if len(parts)==2:
            if parts[0].isdigit()and parts [1].isdigit():
                num=float(gpa)
                break
    print("Must be a valid number with a decimal because it's a GPA, try again")

print("Name: " + fullname)
print("Phone: " +fixed)
print("GPA: ", num)
