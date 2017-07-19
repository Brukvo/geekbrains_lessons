# encoding: utf-8

import turtle
import random

turtle.circle(20)
answer = ''
while answer != 'N':
    answer = turtle.textinput("Python 3.x + Turtle", "Нарисовать ещё несколько разных окружностей? (Y/N/Д/Н)")
    if answer == 'Y':
        for iterate in range(20):
            turtle.circle(random.randrange(10,100,2))
    elif answer == 'N':
        pass
    else:
        print("Неправильный ввод!")
print("Спасибо за запуск демонстрации связки Python 3.x и Turtle!")
