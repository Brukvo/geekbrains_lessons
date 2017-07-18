# encoding: utf-8

import psutil
import shutil
import os
import sys


def dupfiles():
    itera = 0
    filelist = os.listdir(os.getcwd())
    print(delimit + 'После этой операции новые имена файлов приобретут следующие названия:\n')
    for fileitem in filelist:
        if os.path.isfile(fileitem):
            filenew = fileitem + ".dupl"
            print(fileitem + " => " + filenew)
    yn = input('Продолжить? (Y/N) ')
    if yn == ('Y' and 'y'):
        for fileitem in filelist:
            if os.path.isfile(fileitem):
                shutil.copy(fileitem, fileitem + ".dupl")
                itera += 1
        return itera
    else:
        print('Операция прервана.')

# TODO: добавить больше котят!
def deldupfiles():
    itera = 0
    filelist = os.listdir(os.getcwd())
    print(delimit + 'Список дубликатов:')
    for fileitem in filelist:
        if fileitem.endswith('.dupl'):
            print(fileitem)
    yn = input('Удалить дубликаты? (Y/N) ')
    if yn == ('Y' and 'y'):
        for fileitem in filelist:
            if os.path.isfile(fileitem):
                if fileitem.endswith('.dupl'):
                    os.remove(fileitem)
                    itera += 1
        return itera
    if yn == ('N' and 'n'):
        pass

# TODO: здесь котят надо меньше
def delseldups():
    itera = 0
    dirname = input("Для удаления дубликатов в папке укажите путь к ней: ")
    filelist = os.listdir(dirname)
    ilit = 0
    while ilit < len(filelist):
        fullname = os.path.join(dirname, filelist[ilit])
        if fullname.endswith(".dupl"):
            os.remove(fullname)
            itera += 1
        ilit += 1
    return itera


def selfiledup():
    which_file = input("Укажите файл для дублирования относительно текущего расположения (" + os.getcwd() + "): ")
    if os.path.isfile(which_file):
        shutil.copy(which_file, which_file + ".dupl")
    else:
        print("Либо Вы указали папку, либо такого файла нет!")


status = 0  # если всё хорошо, останется 0; если пользователь отказался от операции, то будет 1
work = ''  # заранее формируем переменную для успешного прохождения условия
i = 0
delimit = "\n________________\n"  # чтобы и код, и вывод были читабельными; символ \n - как Enter в текстовом редакторе
name = input("Как Вас зовут? ")
work = input('Отлично, ' + name + ', а не желаете ли поработать? (Y/N/Q) ')
while work != ('Q' and 'q'):
    if work == ('Y' and 'y'):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Выберите желаемое действие:")
        print("  [1] показать информацию о системе")
        # действие 2 доступно только пользователям Linux/UNIX-систем
        print("  [2] сделать дубликаты файлов текущей папки")
        print("  [3] удалить дубликаты файлов (.dupl)")
        print("  [4] сделать дубликат указанного файла")
        print("  [5] удалить дубликаты в указанной Вами папке")
        print('  [Q] выход')
        select = input("Ваш выбор: ")
        if select == '1':
            print(delimit + "Информация о системе:\n")
            print("Текущая папка: " + os.getcwd())
            print("Ваша домашняя папка: " + os.getenv('HOME'))
            print("Логин текущего пользователя: " + os.getenv('LOGNAME'))
            print('В Вашей системе установлено ' + str(psutil.cpu_count()) + " процессор(а).")
            print('Платформа: ' + sys.platform)
            print('Кодировка Вашей файловой системы: ' + sys.getfilesystemencoding())
        elif select == '2':
            duplicated = str(dupfiles())
            print("Файлов продублировано: " + duplicated)
        elif select == '3':
            dupsdeleted = str(deldupfiles())
            print("Удалено дубликатов: " + dupsdeleted)
        elif select == '4':
            selfiledup()
        elif select == '5':
            seldups = str(delseldups())
            print("Удалено дубликатов в выбранной Вами папке: " + seldups)
        elif select == ('Q' and 'q'):
            # чтобы прервать ветвление, пользуемся break
            break
        else:
            print('\n\nНе знаю, чего Вы хотите...\n\n')
    elif work == ('N' and 'n'):
        print("\n\nЛадно, отдыхайте.\n\n")
        break
    else:
        print("\n\nУпс... Не знаем такого ответа! Только Y, N или Q!\n\n");
        status = 1
        break
# та самая переменная status
if status == 1:
    print("Аварийное завершение работы.")
else:
    print('Спасибо за использование Помощника!\nДо свидания!')