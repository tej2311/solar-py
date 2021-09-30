# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 12:08:40 2021

@author: Tej Gandhi
"""


# importing libraries
import turtle
import random
  
wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1500,height=1000)
wn.title("Solar System")


pen=turtle.Turtle()
pen.hideturtle()
pen.penup()




sun=turtle.Turtle()
sun.shape("circle")
sun.shapesize(stretch_len=8,stretch_wid=8)
sun.color("yellow")
sun.penup()
sun.goto(300,0)




mercury=turtle.Turtle()
mercury.shape("circle")
mercury.shapesize(stretch_len=1.2,stretch_wid=1.2)
mercury.color("dark gray")
mercury.penup()
mercury.goto(300,-105)
mercury.pensize(5)
mercury.pendown()



venus=turtle.Turtle()
venus.shape("circle")
venus.shapesize(stretch_len=1.5,stretch_wid=1.5)
venus.color("white")
venus.penup()
venus.goto(420,-95)
venus.pensize(5)
venus.pendown()




earth=turtle.Turtle()
earth.shape("circle")
earth.shapesize(stretch_len=2,stretch_wid=2)
earth.color("turquoise")
earth.penup()
earth.goto(500,20)
earth.pensize(5)
earth.pendown()



moon=turtle.Turtle()
moon.shape("circle")
moon.shapesize(stretch_len=1,stretch_wid=1)
moon.color("light gray")
moon.penup()
moon.goto(earth.xcor(),earth.ycor())
moon.fd(35)




mars=turtle.Turtle()
mars.shape("circle")
mars.shapesize(stretch_len=1.5,stretch_wid=1.5)
mars.color("#FF0000")
mars.penup()
mars.goto(480,175)
mars.pensize(5)
mars.pendown()


moonm=turtle.Turtle()
moonm.shape("circle")
moonm.shapesize(stretch_len=0.4,stretch_wid=0.4)
moonm.color("navy")
moonm.penup()
moonm.goto(mars.xcor(),mars.ycor())
moonm.fd(35)

moonm1=turtle.Turtle()
moonm1.shape("circle")
moonm1.shapesize(stretch_len=0.9,stretch_wid=0.9)
moonm1.color("gold")
moonm1.penup()
moonm1.goto(mars.xcor(),mars.ycor())
moonm1.fd(35)



jupiter=turtle.Turtle()
jupiter.shape("circle")
jupiter.shapesize(stretch_len=3.5,stretch_wid=3.5)
jupiter.color("#8B4513")
jupiter.penup()
jupiter.goto(300,305)
jupiter.pensize(5)
jupiter.pendown()

moonj=turtle.Turtle()
moonj.shape("circle")
moonj.shapesize(stretch_len=1.5,stretch_wid=1.5)
moonj.color("light gray")
moonj.penup()
moonj.goto(jupiter.xcor(),jupiter.ycor())
moonj.fd(35)


moonj1=turtle.Turtle()
moonj1.shape("circle")
moonj1.shapesize(stretch_len=0.7,stretch_wid=0.7)
moonj1.color("#924900")
moonj1.penup()
moonj1.goto(jupiter.xcor(),jupiter.ycor())
moonj1.fd(40)


moonj2=turtle.Turtle()
moonj2.shape("circle")
moonj2.shapesize(stretch_len=0.8,stretch_wid=0.8)
moonj2.color("navy")
moonj2.penup()
moonj2.goto(jupiter.xcor(),jupiter.ycor())
moonj2.fd(32)

moonj3=turtle.Turtle()
moonj3.shape("circle")
moonj3.shapesize(stretch_len=0.9,stretch_wid=0.9)
moonj3.color("light green")
moonj3.penup()
moonj3.goto(jupiter.xcor(),jupiter.ycor())
moonj3.fd(34)

jupiter_spot=turtle.Turtle()
jupiter_spot.shape("circle")
jupiter_spot.shapesize(stretch_len=0.8,stretch_wid=0.8)
jupiter_spot.color("dark red")
jupiter_spot.penup()
jupiter_spot.goto(285,300)





saturn=turtle.Turtle()
saturn.shape("circle")
saturn.shapesize(stretch_len=3,stretch_wid=3)
saturn.color("light yellow")
saturn.penup()
saturn.goto(45,255)
saturn.pensize(5)
saturn.pendown()

moons1=turtle.Turtle()
moons1.shape("circle")
moons1.shapesize(stretch_len=0.9,stretch_wid=0.9)
moons1.color("cyan")
moons1.penup()
moons1.goto(saturn.xcor(),saturn.ycor())
moons1.fd(38)

moons2=turtle.Turtle()
moons2.shape("circle")
moons2.shapesize(stretch_len=0.7,stretch_wid=0.7)
moons2.color("magenta")
moons2.penup()
moons2.goto(saturn.xcor(),saturn.ycor())
moons2.fd(36)



saturn_ring=turtle.Turtle()
saturn_ring.hideturtle()
saturn_ring.color("#ab604a")
saturn_ring.penup()
saturn_ring.goto(45,213)
saturn_ring.pensize(4)
saturn_ring.pendown()
saturn_ring.circle(42)







uranus=turtle.Turtle()
uranus.shape("circle")
uranus.shapesize(stretch_len=2.6,stretch_wid=2.6)
uranus.color("light blue")
uranus.penup()
uranus.goto(-150,0)
uranus.pensize(5)
uranus.pendown()


moonu=turtle.Turtle()
moonu.shape("circle")
moonu.shapesize(stretch_len=0.7,stretch_wid=0.7)
moonu.color("gold")
moonu.penup()
moonu.goto(uranus.xcor(),uranus.ycor())
moonu.fd(35)


moonu1=turtle.Turtle()
moonu1.shape("circle")
moonu1.shapesize(stretch_len=0.5,stretch_wid=0.5)
moonu1.color("violet")
moonu1.penup()
moonu1.goto(uranus.xcor(),uranus.ycor())
moonu1.fd(33)







neptune=turtle.Turtle()
neptune.shape("circle")
neptune.shapesize(stretch_len=2.4,stretch_wid=2.4)
neptune.color("blue")
neptune.penup()
neptune.goto(-50,-325)
neptune.pensize(5)
neptune.pendown()

moonn=turtle.Turtle()
moonn.shape("circle")
moonn.shapesize(stretch_len=0.7,stretch_wid=0.7)
moonn.color("magenta")
moonn.penup()
moonn.goto(neptune.xcor(),neptune.ycor())
moonn.fd(35)


moonn1=turtle.Turtle()
moonn1.shape("circle")
moonn1.shapesize(stretch_len=0.7,stretch_wid=0.7)
moonn1.color("red")
moonn1.penup()
moonn1.goto(neptune.xcor(),neptune.ycor())
moonn1.fd(37)


#directions

mercury.setheading(0)
venus.setheading(45)
earth.setheading(90)
mars.setheading(135)
jupiter.setheading(180)
jupiter_spot.setheading(180)
saturn.setheading(225)
uranus.setheading(270)
neptune.setheading(315)


wn.tracer(60)


#functions

def orbits():
    mercury.fd(5)
    mercury.lt(2.4)
    venus.fd(5)
    venus.lt(1.8)
    earth.fd(5)
    earth.lt(1.4)
    moon.goto(earth.xcor(),earth.ycor())
    moon.fd(35)
    moon.rt(5)
    mars.fd(5)
    mars.lt(1.1)
    moonm.goto(mars.xcor(),mars.ycor())
    moonm.fd(35)
    moonm.rt(4)
    moonm1.goto(mars.xcor(),mars.ycor())
    moonm1.fd(35)
    moonm1.rt(6)
    jupiter.fd(5)
    jupiter.lt(0.9)
    moonj.goto(jupiter.xcor(),jupiter.ycor())
    moonj.fd(35)
    moonj.rt(5)
    moonj1.goto(jupiter.xcor(),jupiter.ycor())
    moonj1.fd(40)
    moonj1.rt(4)
    moonj2.goto(jupiter.xcor(),jupiter.ycor())
    moonj2.fd(32)
    moonj2.rt(3)
    moonj3.goto(jupiter.xcor(),jupiter.ycor())
    moonj3.fd(36)
    moonj3.rt(7)
    jupiter_spot.fd(5)
    jupiter_spot.lt(0.9)
    moons1.goto(saturn.xcor(),saturn.ycor())
    moons1.fd(36)
    moons1.rt(6)
    moons2.goto(saturn.xcor(),saturn.ycor())
    moons2.fd(38)
    moons2.rt(4)
    saturn.fd(5)
    saturn.lt(0.76)
    uranus.fd(5)
    uranus.lt(0.67)
    moonu.goto(uranus.xcor(),uranus.ycor())
    moonu.fd(35)
    moonu.rt(6)
    moonu1.goto(uranus.xcor(),uranus.ycor())
    moonu1.fd(33)
    moonu1.rt(7)
    neptune.fd(5)
    neptune.lt(0.61)
    moonn.goto(neptune.xcor(),neptune.ycor())
    moonn.fd(35)
    moonn.rt(4)
    moonn1.goto(neptune.xcor(),neptune.ycor())
    moonn1.fd(37)
    moonn1.rt(5)
    
    
    
def show_names_and_locations():
    mercury_x=str(mercury.xcor())
    mercury_y=str(mercury.ycor())
    venus_x=str(venus.xcor())
    venus_y=str(venus.ycor())
    earth_x=str(earth.xcor())
    earth_y=str(earth.ycor())
    moon_x=str(moon.xcor())
    moon_y=str(moon.ycor())
    mars_x=str(mars.xcor())
    mars_y=str(mars.ycor())
    jupiter_x=str(jupiter.xcor())
    jupiter_y=str(jupiter.ycor())
    saturn_x=str(saturn.xcor())
    saturn_y=str(saturn.ycor())
    uranus_x=str(uranus.xcor())
    uranus_y=str(uranus.ycor())
    neptune_x=str(neptune.xcor())
    neptune_y=str(neptune.ycor())
    pen.goto(-850,450)
    pen.color("yellow")
    pen.write("THE SUN",font=(15,"bold"),align="left")
    pen.goto(-700,450)
    pen.color("dark red")
    pen.write("JUPITER'S SPOT",font=(15,"bold"),align="left")
    pen.goto(-850,350)
    pen.color("dary gray")
    pen.write("MERCURY: "+"("+mercury_x+", "+mercury_y+")",font=(15,"bold"),align="left")
    pen.goto(-850,250)
    pen.color("white")
    pen.write("VENUS: "+"("+venus_x+", "+venus_y+")",font=(15,"bold"),align="left")
    pen.goto(-850,150)
    pen.color("turquoise")
    pen.write("EARTH: "+"("+earth_x+", "+earth_y+")",font=(15,"bold"),align="left")
    pen.goto(-850,50)
    pen.color("light gray")
    pen.write("THE MOON: "+"("+moon_x+", "+moon_y+")",font=(15,"bold"),align="left")
    pen.goto(-850,-50)
    pen.color("#FF0000")
    pen.write("MARS: "+"("+mars_x+", "+mars_y+")",font=(15,"bold"),align="left")
    pen.goto(-850,-150)
    pen.color("#8B4513")
    pen.write("JUPITER: "+"("+jupiter_x+", "+jupiter_y+")",font=(15,"bold"),align="left")
    pen.goto(-850,-250)
    pen.color("light yellow")
    pen.write("SATURN: "+"("+saturn_x+", "+saturn_y+")",font=(15,"bold"),align="left")
    pen.goto(-850,-350)
    pen.color("light blue")
    pen.write("Uranus: "+"("+uranus_x+", "+uranus_y+")",font=(15,"bold"),align="left")
    pen.goto(-850,-450)
    pen.color("blue")
    pen.write("NEPTUNE: "+"("+neptune_x+", "+neptune_y+")",font=(15,"bold"),align="left")
    
    
t = turtle.Turtle()
  
# to activate turtle graphics Screen
w = turtle.Screen()
  
# setting speed of turtle
t.speed(50)
  
# giving the background color of turtle
# graphics screen
w.bgcolor("black")
  
# giving the color of pen to our turtle
# for drawing
t.color("white")
  
# giving title to our turtle graphics window
w.title("Starry Sky")
  
# making function to draw the stars
def stars():
    for i in range(5):
        t.fd(10)
        t.right(144)
  
  
# loop for making number of stars
for i in range(500):
    
    # generating random integer values for x and y
    x = random.randint(-730, 730)
    y = random.randint(-420, 420)
      
    # calling the function stars to draw the 
    # stars at random x,y value
    stars()
      
    # took up the turtle's pen
    t.up()
      
    # go at the x,y coordinate generated above
    t.goto(x, y)
      
    # took down the pen to draw
    t.down()
    

  
# 
# going at the specific coordinated

  
# start filling the color



t.hideturtle()
    
    
    
#main loop

while True:
    orbits()
    show_names_and_locations
    saturn_ring.clear()
    saturn_ring.goto(saturn.xcor()-1,saturn.ycor()-45)
    saturn_ring.circle(42)
    stars()
    wn.update
    
    
    
    

  
# creating turtle object

  
# after drawing hidding the turtle from
# the window


wn.mainloop()
  


t.hideturtle()