# encoding: utf-8

import turtle

turtle.circle(20)
answer = ''
while answer != ('N' and 'n' and 'Н' and 'н'):
    answer = turtle.textinput("Python 3.x + Turtle", "Нарисовать ещё одну окружность? (Y/N/Д/Н)")
    if answer == ('Y' and 'y' and 'Д' and 'д'):
        turtle.circle(30)
    if answer == ('N' and 'n' and 'Н' and 'н'):
        print("Спасибо за запуск демонстрации связки Python 3.x и Turtle!")
    else:
        print("Аварийное завершение - пользователь ввёл неверное значение.")
        