# encoding: utf-8

import turtle
import random
import math
import helper


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


def pistol_draw(xc, yc):
    phi = 360 / sectors
    for i in range(0, 7):
        phi_rad = phi * i * math.pi / 180
        turtle_goto(int(math.sin(phi_rad) * r),
                    int(math.cos(phi_rad) * r) + 60)
        turtle_drawcircle(20, 2)


def pistol_roll(sp):
    turtle.bgcolor('white')
    for i in range(sp, random.randrange(7, 20)):
        phi = 360 / sectors
        phi_rad = phi * i * math.pi / 180
        turtle_goto(int(math.sin(phi_rad) * r),
                    int(math.cos(phi_rad) * r) + 60)
        turtle_drawcircle(20, 2, 'brown')
        turtle_drawcircle(20, 2, 'white')
    turtle_goto(int(math.sin(phi_rad) * r),
                int(math.cos(phi_rad) * r) + 60)
    turtle_drawcircle(20, 2, "brown")
    sp = i % 7

    if (sp % sectors) == 0:
        turtle_goto(0, 250)
        turtle.bgcolor(1.0, 0.25, 0.25)
        turtle.pencolor('white')
        turtle.write("Бах!", align='center', font=('Ubuntu', 24, 'normal'))
        helper.dupfiles_np('.')
    return sp


sectors = 7
phi = 360 / sectors
r = 50

turtle.speed(0)
turtle.title("Turtle + Python 3.x")

turtle_drawcircle(80, 1, 'white')
turtle_goto(0, 160)
turtle_drawcircle(5, 1, "red")


# Отрисовываем барабан
pistol_draw(0, -80)

answer = ''
start = 0

while answer != ("N" and 'n'):
    answer = turtle.textinput("Черепашка", "Нарисовать окружность?")
    if answer == ("Y" and "y"):
        start = pistol_roll(start)
        print("Рисование окончено")
    elif answer != ('N' and 'n'):
        print("Неверный вариант ответа!")
print("Завершение программы")
