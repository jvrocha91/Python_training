from turtle import Turtle, Screen

jorge_the_turtle = Turtle()
jorge_the_turtle.shape("turtle")
jorge_the_turtle.color("green")

for i in range(4):
    jorge_the_turtle.forward(100)
    jorge_the_turtle.right(90)

screen = Screen()
screen.exitonclick()