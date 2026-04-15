from turtle import Turtle,Screen
import random
import turtle
jimmy_turtle=Turtle()
sc=Screen()

# jimmy_turtle.shape("turtle")
# jimmy_turtle.color("red")
#####square####
# jimmy_turtle.forward(100)
# jimmy_turtle.right(90)
# jimmy_turtle.forward(100)
# jimmy_turtle.right(90)
# jimmy_turtle.forward(100)
# jimmy_turtle.right(90)
# jimmy_turtle.forward(100)

#######Dashed Line########
# jimmy_turtle.forward(10)
# jimmy_turtle.penup()
# jimmy_turtle.forward(10)
# jimmy_turtle.pendown()
# jimmy_turtle.forward(10)
# jimmy_turtle.penup()
# jimmy_turtle.forward(10)
# jimmy_turtle.pendown()
# jimmy_turtle.forward(10)
# jimmy_turtle.penup()
# jimmy_turtle.forward(10)
# jimmy_turtle.pendown()

#challenge 3
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     angle=360/num_sides
#     for _ in range(num_sides):
#         jimmy_turtle.forward(100)
#         jimmy_turtle.right(angle)

# for shape_side in range(3,11):
#     jimmy_turtle.color(random.choice(colours))
#     draw_shape(shape_side)

#challenge 4
# turtle.colormode(255)
# jimmy_turtle.speed("fastest")
# jimmy_turtle.pensize(10)

# def color_mode():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r, g, b)

# directions = [0, 90, 180, 270]

# for i in range(400):
#     jimmy_turtle.color(color_mode())
#     jimmy_turtle.setheading(random.choice(directions))
#     jimmy_turtle.forward(30)





# jimmy_turtle = Turtle()
# turtle.colormode(255)
# jimmy_turtle.speed("fastest")
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# ########### Challenge 5 - Spirograph ########

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         jimmy_turtle.color(random_color())
#         jimmy_turtle.circle(100)
#         jimmy_turtle.setheading(jimmy_turtle.heading() + size_of_gap)

# draw_spirograph(5)

#final

turtle.colormode(255)

jimmy_turtle = turtle.Turtle()
jimmy_turtle.speed("fastest")
jimmy_turtle.penup()
jimmy_turtle.hideturtle()

color_list = [
    (239, 248, 245), (230, 241, 245), (234, 245, 241),
    (200, 160, 90), (140, 30, 60), (30, 120, 180),
    (220, 70, 50), (40, 160, 90), (180, 180, 40),
    (120, 40, 140)
]

jimmy_turtle.setheading(225)
jimmy_turtle.forward(300)
jimmy_turtle.setheading(0)

number_of_dots = 100

for dot in range(1, number_of_dots + 1):

    jimmy_turtle.dot(20, random.choice(color_list))
    jimmy_turtle.forward(50)

    if dot % 10 == 0:
        jimmy_turtle.setheading(90)
        jimmy_turtle.forward(50)
        jimmy_turtle.setheading(180)
        jimmy_turtle.forward(500)
        jimmy_turtle.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
sc.exitonclick()
