from turtle import Turtle, Screen
from random import random
# Para simplificar poderia ser import turtle as t e depois ao declarar objeto, artist = t.Turtle()

jorge_the_turtle = Turtle()
jorge_the_turtle.shape("turtle")
jorge_the_turtle.color("green")
jorge_the_turtle.speed(1)
#will_the_turtle = Turtle()
#will_the_turtle.shape("turtle")
#will_the_turtle.color("red")
#will_the_turtle.speed(1)

for i in range(15):
    jorge_the_turtle.forward(10)
    jorge_the_turtle.penup()
    jorge_the_turtle.forward(10)
    jorge_the_turtle.pendown()

screen = Screen()
screen.exitonclick()
