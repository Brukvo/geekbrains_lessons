# encoding: utf-8

import turtle
import random

turtle.circle(20)
answer = ''
while answer != 'N':
    answer = turtle.textinput("Python 3.x + Turtle", "Нарисовать ещё одну окружность? (Y/N/Д/Н)")
    if answer == 'Y':
        turtle.circle(random.randrange(10,200,2))
    else:
        print("Неправильный ввод!")
print("Спасибо за запуск демонстрации связки Python 3.x и Turtle!")
