import turtle

def turtle_square_circle():
    Tt = turtle.Turtle()
    Tt.shape("turtle")
    Tt.color("blue")
    Tt.speed(10)
    
    Tt.left(45)

    for i in range(1,75):
        Tt.forward(50)
        Tt.right(45)
        Tt.forward(50)
        Tt.right(135)
        Tt.forward(50)
        Tt.right(45)
        Tt.forward(50)
        Tt.left(10)

    Tt.right(60)
    Tt.forward(200)

    window = turtle.Screen()
    window.exitonclick()

turtle_square_circle()