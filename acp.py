import turtle

s = turtle.Screen()
s.bgcolor('black')

t = turtle.Turtle()
t.speed('fastest')
t.hideturtle()

colors = ['red', 'green', 'blue']

t.penup()
t.goto(-200, 100)
t.pendown()
t.fillcolor(colors[0])
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.goto(50, 100)
t.pendown()
t.fillcolor(colors[1])
t.begin_fill()
for _ in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-70, -150)
t.pendown()
t.fillcolor(colors[2])
t.begin_fill()
for _ in range(6):
    t.forward(80)
    t.left(60)
t.end_fill()