import turtle as t #This is aliasing
t.showturtle()
'''t.color("orange")
t.width(3)
t.forward(300)
t.left(120)
t.forward(300)
t.left(120)
t.forward(300)
t.speed(10)
t.up()
t.forward(300)
t.down()
t.left(20)
t.forward(400)
t.home()
t.pos(0,100)
t.clearscreen()
t.pos(300, 400)
t.home()'''

colors=["orange","blue","green"]
loop_helper=0
for num in range(360):
    t.color(colors[loop_helper])
    t.fd(5)
    t.left(1)
    loop_helper+=1
    if loop_helper==6:
        loop_helper=0
t.shape("square")
t.shapesize(300)
t.hideturtle()
t.forward(200)
for x in range(0,100):
    t.tilt(x)
t.shearfactor(30)
t.shapetransform(10,5,3,2)
t.goto(200,400)

t.exitonclick()
beebus=t.Turtle()
geebus=t.Turtle()