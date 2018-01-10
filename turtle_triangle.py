import turtle

def turtle_triangle(Tt, level, dist):
    if level == 0:
        Tt.pendown()
        Tt.begin_fill()
        for _ in range(3):
            Tt.forward(dist)
            Tt.left(120)
        Tt.end_fill()
        Tt.penup()
    else:
        for _ in range(3):
            turtle_triangle(Tt, level-1, dist/2)
            Tt.forward(dist)
            Tt.left(120)

window = turtle.Screen()

Tt = turtle.Turtle()
#Tt.speed(10)
Tt.shape("turtle")
Tt.color("green")

turtle_triangle(Tt, 1, 300)

window.exitonclick()