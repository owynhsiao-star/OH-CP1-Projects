try:
    bio = int(input ("What is your biology grade?"))
    math =int(input ("what is your math grade?"))
    geo=int(input ("what is your geography grade?"))
    eng=int(input("what is yoou english grade?"))
    prog=int(input("what is your programming grade?"))
    draw=int(input("what is your drawing grade?"))
except:
    print("please input a number")
else:
    print((bio+math+geo+eng+prog+draw)/6)