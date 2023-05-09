import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#DEFE28")
drawing_board.title("🐢🐢")

turtle_instance = turtle.Turtle()
turtle_instance.pensize(6)
turtle_instance.pencolor("DeepPink")

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading() - 10)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading() + 10)

def clear_screen():
    turtle_instance.clear()

def home_position():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=rotate_angle_right, key="Right")
drawing_board.onkey(fun=rotate_angle_left, key="Left")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=home_position, key="h")
drawing_board.onkey(fun=turtle_pen_down, key="w")
drawing_board.onkey(fun=turtle_pen_up, key="q")

turtle.done()