# encoding: utf-8

import turtle
import random

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
            print("Поднимаем перо")
            turtle.penup()
            print("Передвигаемся в новую точку")
            turtle.goto(random.randrange(0, 200), random.randrange(0, 200))
            print("Опускаем перо")
            turtle.pendown()
            print("Устанавливаем цвет заливки")
            turtle.fillcolor(0, random.random(), 0)
            print("Устанавливаем цвет линии")
            turtle.pencolor(0, random.random(), 0)
            turtle.begin_fill()
            print("Рисуем окружность №" + str(iterate) + ", которая будет заполнена выбранным нами цветом")
            turtle.circle(random.randrange(10, 100, 10))
            print("Делаем заливку выбранным случайным образом цветом")
            turtle.end_fill()
        print("Закончили рисование")
    elif answer == 'N':
        pass
    else:
        print("Неправильный ввод!")
print("Спасибо за запуск демонстрации связки Python 3.x и Turtle!")
