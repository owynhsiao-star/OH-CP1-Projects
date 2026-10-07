#OH, period 1, Multiplication table project
for num in range(1,13):
    for num2 in range(1,13,12):
        print(num*num2, " ", end="")
print("\n")
for num in range(1,13):   
    for num2 in range(2,13,12):
        print(num*num2, " ", end="")
print("\n")
for num in range(1,13):
    for num2 in range(3,13,12):
        print(num*num2, " ", end="")
print("\n")
for num in range(1,13):   
    for num2 in range(4,13,12):
        print(num*num2, " ", end="")
print("\n")
for num in range(1,13):
    for num2 in range(5,13,12):
        print(num*num2, " ", end="")
print("\n")
for num in range(1,13):   
    for num2 in range(6,13,12):
        print(num*num2, " ", end="")
print("\n")
for num in range(1,13):
    for num2 in range(7,13,12):
        print(num*num2, " ", end="")
print("\n")
for num in range(1,13):   
    for num2 in range(8,13,12):
        print(num*num2, " ", end="")
print("\n")
for num in range(1,13):
    for num2 in range(9,13,12):
        print(num*num2, " ", end="")
print("\n")
for num in range(1,13):   
    for num2 in range(10,13,12):
        print(num*num2, " ", end="")
print("\n")
for num in range(1,13):
    for num2 in range(11,13,12):
        print(num*num2, " ", end="")
print("\n")
for num in range(1,13):   
    for num2 in range(12,13,12):
        print(num*num2, " ", end="")
print("\n")

xval=int(input("What number is being multiplied?"))
if xval<1 or xval>12:
    print("Between one and twelve please")
    xval=int(input("What number is being multiplied?"))
yval=int(input("What number is doing the multiplying?"))
if yval<1 or yval>12:
    print('Between one and twelve please')
    yval=int(input("What number is doing the multiplying?"))
print(yval*xval)