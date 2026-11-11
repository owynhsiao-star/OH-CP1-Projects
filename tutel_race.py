import turtle as t
import random as r
t1=t.Turtle()
t2=t.Turtle()
t3=t.Turtle()
t4=t.Turtle()
t5=t.Turtle()
finishline=t.Turtle()
winnini=False
turtles={t1, t2, t3, t4, t5}
pen_color, fill_color=t.color()
pen_color, fill_color.hideturtle()
def setup(cy):
        numero=0
        for i in cy:
            i.shape("turtle")
            if numero==0:
                i.color("green")
                i.up()
                i.left(90)
                i.forward(150)
                i.down()
                i.right(90)
            elif numero==1:
                i.color("red")
                i.up()
                i.left(90)
                i.forward(75)
                i.down()
                i.right(90)
            elif numero==2:
                i.color("yellow")
                i.up()
                i.right(90)
                i.forward(75)
                i.down()
                i.left(90)
            elif numero==3:
                i.color("blue")
                i.up()
                i.right(90)
                i.forward(150)
                i.down()
                i.left(90)
            else:
                i.color("orange")
            numero+=1

        


        finishline.up()
        finishline.goto(500, 500)
        finishline.down()
        finishline.right(90)
        finishline.forward(900)
        finishline.hideturtle()
def move(m):    
        for i in m:
            i.forward(r.randint(0,200))
def win(e):
     for i in e:
        locat=i.xcor()
        if locat>500:
            print(f"YOU WIN {i.pencolor()}") 
            t.done()
        else:
            break
   
setup(turtles)
while True:
    move(turtles)
    win(turtles)
