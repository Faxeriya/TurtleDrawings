from turtle import *
speed(6)
setup(height=800, width=1400)
bgcolor("red")
color("white")
left(90)
begin_fill()
circle(200)
end_fill()
color("red")
right(90)
forward(50)
left(90)
begin_fill()
circle(170)
end_fill()
color("white")
penup()
goto(60,50)
pendown()
begin_fill()
round = 0
while round < 5:
    left(144)
    forward(150)
    round +=1
end_fill()
hideturtle()
done()