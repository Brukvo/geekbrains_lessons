# encoding: utf-8

import turtle
import random


def tur_goto(xcoord, ycoord):
    print("Поднимаем перо")
    turtle.penup()
    print("Передвигаемся в новую точку")
    turtle.goto(xcoord, ycoord)
    print("Опускаем перо")
    turtle.pendown()


def tur_drcir(radius, pen_size, cir_color, line_color = "black"):
    print("Устанавливаем размер кисти")
    turtle.pensize(pen_size)
    print("Устанавливаем цвет заливки")
    turtle.fillcolor(cir_color)
    print("Устанавливаем цвет линии")
    turtle.pencolor(line_color)
    turtle.begin_fill()
    print("Рисуем окружность, которая будет заполнена выбранным нами цветом")
    turtle.circle(radius)
    print("Делаем заливку выбранным случайным образом цветом")
    turtle.end_fill()

print("Устанавливаем скорость рисования")
turtle.speed(1)
print("Рисуем окружность радиусом 20 точек")
turtle.circle(20)
answer = ''
while answer != 'N':
    answer = turtle.textinput("Python 3.x + Turtle", "Нарисовать ещё несколько разных окружностей? (Y/N/Д/Н)")
    if answer == 'Y':
        print("Выбираем случайное число для цвета")
        brt = random.random()
        for iterate in range(20):
            tur_goto(random.randrange(0, 200), random.randrange(0, 200))
            tur_drcir(random.randrange(10, 100), random.randrange(1, 10), "brown", "green")
        print("Закончили рисование")
    elif answer == 'N':
        pass
    else:
        print("Неправильный ввод!")
print("Спасибо за запуск демонстрации связки Python 3.x и Turtle!")
