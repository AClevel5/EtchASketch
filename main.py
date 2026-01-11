from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def reset():
    t.clear()
    t.goto(0,0)

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(reset, "c")
screen.exitonclick()