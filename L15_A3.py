import turtle
turtle.Screen().bgcolor("White")
turtle.Screen().setup(300,400)
turtle.Screen().title(turtle)
pencil=turtle.Turtle()
size=0
while True:
    for i in range(4):
        pencil.fd(size+1)
        pencil.left(90)
        size=size-5
    size=size+1
    

