# encoding: utf-8

import turtle
import random
import math


def turtle_goto(xcoord=0, ycoord=0):
    turtle.penup()
    turtle.goto(xcoord, ycoord)
    turtle.pendown()


def turtle_drawcircle(r, p_size, c_color='', p_color="black"):
    turtle.pensize(p_size)
    turtle.fillcolor(c_color)
    turtle.pencolor(p_color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


sectors = 7
r = 50

turtle.speed(0)
turtle.title("Turtle + Python 3.x")

turtle_drawcircle(80, 1, 'white')
turtle_goto(0, 160)
turtle_drawcircle(5, 1, "red")

phi = 360 / sectors

# Отрисовываем барабан
for i in range(0, 7):
    phi_rad = phi * i * math.pi / 180
    turtle_goto(int(math.sin(phi_rad) * r), int(math.cos(phi_rad) * r) + 60)
    turtle_drawcircle(20, 2)

answer = ''

while answer != ("N" and 'n'):
    answer = turtle.textinput("Черепашка", "Нарисовать окружность?")
    if answer == ("Y" and "y"):
        for i in range(0, random.randrange(7, 20)):
            phi_rad = phi * i * math.pi / 180
            turtle_goto(int(math.sin(phi_rad) * r),
                        int(math.cos(phi_rad) * r) + 60)
            turtle_drawcircle(20, 2, 'brown')
            turtle_drawcircle(20, 2, 'white')
        turtle_goto(int(math.sin(phi_rad) * r),
                    int(math.cos(phi_rad) * r) + 60)
        turtle_drawcircle(20, 2, "brown")
        if (i % sectors) == 0:
            turtle_goto(0, 250)
            turtle.bgcolor(1.0, 0.25, 0.25)
            turtle.pencolor('white')
            turtle.write("Бах!", align='center', font=('Ubuntu', 24, 'normal'))
        print("Рисование окончено")
    elif answer != ('N' and 'n'):
        print("Неверный вариант ответа!")
print("Завершение программы")
