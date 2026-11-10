import turtle as t
import time as ti
import random as r
t1=t.Turtle()
t2=t.Turtle()
t3=t.Turtle()
t4=t.Turtle()
t5=t.Turtle()
winnini=False
turtles={t1, t2, t3, t4, t5}

def colorasig(cy):
        numero=0
        for i in cy:
            i.shape("turtle")
            if numero==0:
                i.color("green")
            elif numero==1:
                i.color("red")
            elif numero==2:
                i.color("yellow")
            elif numero==3:
                i.color("blue")
            else:
                i.color("orange")
            numero+=1
colorasig(turtles)
t1.up()
t1.left(90)
t1.forward(150)
t1.down()
t1.right(90)
t2.up()
t2.left(90)
t2.forward(75)
t2.down()
t2.right(90)
t4.up()
t4.right(90)

t4.forward(75)
t4.down()
t4.left(90)
t5.up()
t5.right(90)
t5.forward(150)
t5.down()
t5.left(90)
while True:
     for i in turtles:
        moveval=r.randint(0,150)
        locat= i.xcor()
        if locat>500:
            t.done 
            break
        if locat<500:
            for i in turtles:
                i.forward(moveval)
     break
t.done()