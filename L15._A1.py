import turtle
turtle.Screen().bgcolor("darkgreen")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
polygon.pensize(5)
num_sides=6
side_lenth=70
angle=360/num_sides
for i in range(num_sides):
    polygon.forward(side_lenth)
    polygon.right(angle)
turtle.done()
