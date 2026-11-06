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
    t.showturtle()
    for x in range(0,100):
        t.tilt(x)
    t.shearfactor(30)
    t.shapetransform(10,5,3,2)
