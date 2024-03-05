import turtle
lentgh = int(input("please enter lentgh: "))
color = input("please enter color: ")
screen = turtle.Screen()
Dawn = turtle.Turtle("turtle")
turtle.bgcolor("hotpink")
Dawn.color(color)
for i in range(4):
    Dawn.forward(lentgh)
    Dawn.right(90)
screen.mainloop()
