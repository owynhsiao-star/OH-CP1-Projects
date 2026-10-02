#OH, period 1 multiplication table assignment


multlist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for numericalator in multlist:
    print("1 2 3 5 6 7 8 9 10 11 12")
xval=int(input("What X value would you like? (between 1 and 12)"))
if xval>12:
    print("Lower")
    xval=input("What X value would you like? (between 1 and 12)")
if xval<1:
    print("Higher")
    xval=input("What X value would you like? (between 1 and 12)")
if xval>1 and xval<12:
    yval=input("What y value would you like? (Between 1 and 12)")
if yval>12:
    print("Lower")
    yval=input("What y value would you like? (Between 1 and 12)")
if yval<1:
    print("Higher")
    yval=input("What y value would you like? (Between 1 and 12)")
if yval>1 and yval<12:
    answer=(xval*yval)