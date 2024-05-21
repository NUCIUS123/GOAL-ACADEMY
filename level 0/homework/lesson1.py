from turtle import*

width(7)
#we want to paint house
speed(15)
#step 1:draw a square

forward(200)
left(90)
forward(200) 
left(90)
forward(200)
left(90)
forward(200)
#begin making door
left(90)
forward(65)
color("green")
begin_fill()
left(90)
forward(80)

right(90)
forward(70)

right(90)
forward(80)
end_fill()
#end making door
#start making roof
penup()
goto(200,200)
color("blue")
begin_fill()
pendown()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("orange")
begin_fill()
#start first window
penup()
goto(20,125)
pendown()
right(150)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
begin_fill()
#start second window
penup()
goto(180,125)
pendown()

forward(50)
right(90)

forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
#end drawing
        





exitonclick()
