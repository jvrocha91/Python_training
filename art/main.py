from turtle import Turtle, Screen
from random import choice
# Para simplificar poderia ser import turtle as t e depois ao declarar objeto, artist = t.Turtle()

jorge_the_turtle = Turtle()
jorge_the_turtle.shape("turtle")
jorge_the_turtle.color("green")
jorge_the_turtle.speed(3)
jorge_the_turtle.pensize(8)

cores = ["red","blue","green","yellow","purple","orange"]
numero_lados = 3

while numero_lados <=15:
    jorge_the_turtle.color(choice(cores))
    for i in range(numero_lados):
        angulo = 360 / numero_lados
        jorge_the_turtle.forward(100)
        jorge_the_turtle.right(angulo)
    numero_lados += 1

screen = Screen()
screen.exitonclick()
