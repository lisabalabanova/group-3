# This is a sample Python script.
import task11
import task13
import Task14
import MakePicture
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def Main():
    """Функция для Запуска программы построения графа

           Parameters
           ----------
           Входных параметров не имеет

           Example
           -------
             Ожидает значения от пользователя от 1 до 3, в
             зависимости какую задачу хочет решить пользователь.

           Returns
           -------
           str
               Выводит Опреленный пункиты, для правильного восприятия пользователя
           """
    print("№ 1 : В заданном неориентированном графе найти все максимальные и все наибольшие внутренне устойчивые (независимые)множества вершин.\n"
          "№ 2 : В заданном неориентированном графе найти все минимальные и все наименьшие внешне устойчивые (доминирующие) множества вершин.\n"
          "№ 3 : В заданном ориентированном графе найти все минимальные и все наименьшие внешне устойчивые (доминирующие) множества вершин.")
    NumberTask = input("Выберите номер задачи: ")
    if int(NumberTask) == 1:
        task11.Start()
    elif int(NumberTask) == 2:
        task13.Start()
    elif int(NumberTask) == 3:
        Task14.Start()
    else:
        print("Выберите задание!")
    print("Вывести вкартинку в консоль? 1: Да, 2:Нет")
    MakeImg = input()
    if int(MakeImg) == 1:
        MakePicture.Start()
    else:
        print("Ну ладно =(")
    return 0
Main()