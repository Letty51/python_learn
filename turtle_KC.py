import turtle

def turtle_KO():
    Tt = turtle.Turtle()
    Tt.shape("turtle")
    Tt.pencolor("blue")
    Tt.right(90)
    Tt.forward(50)
    Tt.left(135)
    Tt.forward(50)
    Tt.right(180)
    Tt.forward(50)
    Tt.left(45)
    Tt.forward(50)
    Tt.left(180)
    Tt.forward(50)
    Tt.right(135)
    Tt.forward(50)

    Tt.penup()
    Tt.goto(50,0)
    Tt.pendown()

    Tt.left(45)
    Tt.forward(50)
    Tt.right(180)
    Tt.forward(50)
    Tt.left(90)
    Tt.forward(100)
    Tt.left(90)
    Tt.forward(50)

    window = turtle.Screen()
    window.exitonclick()

turtle_KO()