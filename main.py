from turtle import Turtle, Screen

husni = Turtle()
husni.shape("turtle")
husni.color("green4")

# def draw_dashed_line():
#     husni.penup()
#     husni.setpos(-100, 0)
#     for i in range(0, 20):
#         husni.pendown()
#         husni.forward(10)
#         husni.penup()
#         husni.forward(10)
#
#
# draw_dashed_line()




# def draw_triangle():
#     lines = 0
#     while lines < 3:
#         husni.forward(100)
#         husni.right(120)
#         lines += 1
#
#
# def draw_square():
#     lines = 0
#     while lines < 4:
#         husni.forward(100)
#         husni.right(90)
#         lines += 1
#
#
# def draw_pentagon():
#     lines = 0
#     while lines < 5:
#         husni.forward(100)
#         husni.right(72)
#         lines += 1
#
#
# def draw_hexagon():
#     lines = 0
#     while lines < 6:
#         husni.forward(100)
#         husni.right(60)
#         lines += 1
#
#
# def draw_heptagon():
#     lines = 0
#     while lines < 7:
#         husni.forward(100)
#         husni.right(51.4)
#         lines += 1
#
#
# def draw_octagon():
#     lines = 0
#     while lines < 8:
#         husni.forward(100)
#         husni.right(45)
#         lines += 1
#
#
# def draw_nonagon():
#     lines = 0
#     while lines < 9:
#         husni.forward(100)
#         husni.right(40)
#         lines += 1
#
#
# def draw_decagon():
#     lines = 0
#     while lines < 10:
#         husni.forward(100)
#         husni.right(36)
#         lines += 1
#
#
# draw_triangle()
# draw_square()
# draw_pentagon()
# draw_hexagon()
# draw_heptagon()
# draw_octagon()
# draw_nonagon()
# draw_decagon()




# def draw_form():
#     lines = 0
#     while lines < 52:
#         if lines < 3:
#             degrees = 120
#             husni.color("red")
#         elif lines < 7:
#             degrees = 90
#             husni.color("blue")
#         elif lines < 12:
#             degrees = 72
#             husni.color("green")
#         elif lines < 18:
#             degrees = 60
#             husni.color("pink")
#         elif lines < 25:
#             degrees = 51.4
#             husni.color("yellow")
#         elif lines < 33:
#             degrees = 45
#             husni.color("black")
#         elif lines < 42:
#             degrees = 40
#             husni.color("silver")
#         elif lines < 52:
#             degrees = 36
#             husni.color("skyblue")
#
#         husni.forward(100)
#         husni.right(degrees)
#         lines += 1
#
#
# draw_form()





# import random
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         husni.forward(100)
#         husni.right(angle)
#
#
# for shape_side_n in range(3, 10):
#     husni.color(random.choice(colours))
#     draw_shape(shape_side_n)




# import random
# def random_walk():
#     husni.speed(speed=10)
#     for i in range(50):
#         steps = int(random.random() * 50)
#         angle = [0, 90, 180, 270]
#         husni.color(random.random(), random.random(), random.random())  # (r, g, b)
#         husni.pensize(width=5 + i*0.2)
#         husni.right(random.choice(angle))
#         husni.fd(steps)
#
#
# random_walk()


# screen = Screen()
# from random import random
# def draw_spirograph():
#     screen.tracer(5)
#     husni.hideturtle()
#     for n in range(0, 360, 10):
#         for i in range(360):
#             steps = 1
#             angle = 1
#             husni.left(angle)
#             husni.fd(steps)
#         husni.color(random(), random(), random())
#         husni.seth(n)
#
#
# draw_spirograph()




# screen = Screen()
# from random import random
# def draw_spirograph():
#     husni.hideturtle()
#     screen.tracer(5)
#     for n in range(0, 360, 10):
#         husni.color(random(), random(), random())
#         husni.setheading(n)
#         husni.circle(100)
#
#
# draw_spirograph()




screen = Screen()
screen.exitonclick()