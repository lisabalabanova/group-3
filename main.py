from Tasks import task13, Task14, task11
from libs import MakePicture


def main():
    """ Функция для Запуска программы построения графа.
        Выводит опредленный пукты, для правильного восприятия пользователя.
     """
    print("№ 1 : В заданном неориентированном графе найти все максимальные и все наибольшие внутренне устойчивые (независимые)множества вершин.\n"
          "№ 2 : В заданном неориентированном графе найти все минимальные и все наименьшие внешне устойчивые (доминирующие) множества вершин.\n"
          "№ 3 : В заданном ориентированном графе найти все минимальные и все наименьшие внешне устойчивые (доминирующие) множества вершин.")
    flag = "да"
    while flag.lower() == "да":
        NumberTask = input("Выберите номер задачи: ")
        if int(NumberTask) == 1:
            task11.Start()
            makePicture()
        elif int(NumberTask) == 2:
            task13.Start()
            makePicture()
        elif int(NumberTask) == 3:
            Task14.Start()
            makePicture()
        else:
            print("Выберите задание!")
        flag = input('Хотите продолжить? (Да или нет) ')
    return 0

def makePicture():
    print("Вывести вкартинку в консоль? 1: Да, 2:Нет")
    MakeImg = input()
    if int(MakeImg) == 1:
        MakePicture.Start()
    else:
        print("Ну ладно =(")
    return 0

main()

