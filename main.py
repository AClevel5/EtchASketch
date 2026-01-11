from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)

screen.listen()
screen.onkey(move_forwards, "space")
screen.exitonclick()