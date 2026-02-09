
import colorgram
import turtle as t
import random
# color_list = []
# colors = colorgram.extract('hirst_img.jpg', 30)
# for color in range(1, 30):
#     color_position = colors[color].rgb
#     first_r = color_position[0]
#     first_g = color_position[1]
#     first_b = color_position[2]
#     color_tuple = (first_r, first_g, first_b)
#
#     color_list.append(color_tuple)
#
# print(color_list)

paint = t.Turtle()

paint.speed(0)
paint.penup()
paint.hideturtle()
t.colormode(255)

color_list = [(201, 158, 116), (65, 98, 127), (147, 85, 63), (141, 161, 186), (124, 185, 170), (195, 139, 155), (227, 202, 118), (156, 165, 55), (131, 78, 86), (64, 40, 33), (79, 112, 92), (62, 169, 117), (30, 48, 66), (175, 95, 107), (195, 97, 77), (142, 29, 43), (108, 40, 30), (56, 33, 44), (11, 62, 49), (46, 58, 95), (170, 188, 217), (87, 129, 183), (228, 203, 9), (157, 209, 193), (218, 180, 172), (53, 155, 162)]
color = random.choice(color_list)

def x_direction():
    paint.setheading(225)
    paint.forward(400)
    paint.setheading(0)

    for x_axis in range(10):
        color = random.choice(color_list)
        paint.dot(20, color)
        paint.forward(50)
y = 0
for y_axis in range(10):
    y += 50
    paint.teleport(-50, y)
    x_direction()

screen = t.Screen()
screen.exitonclick()