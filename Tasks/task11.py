import matplotlib.pyplot as plt
import networkx as nx


# from colorit import background, init_colorit


def MakeGraphGreatAgain(V, E):
    """Функция создания неориентированного графа

        Parameters
        ----------
            V : str
            Список вершин.
            E : str
            Список ребер

        Returns
        -------
            tuple
            Построенный граф и картинку графа в формате jpg

     """
    graph = nx.Graph()
    V = list(map(int, V.replace('{', '').replace('}', '').replace(',', ' ').split()))
    E = list(map(int, E.replace('{', '').replace('}', '').replace('(', '').replace(')', '').replace(',', ' ').split()))
    res = []
    temp = 0
    tmp = []
    for i in E:
        tmp.append(i)
        temp += 1
        if temp % 2 == 0:
            res.append(tmp)
            tmp = []
    # print(res)
    graph.add_nodes_from(V)
    graph.add_edges_from(res)
    nx.draw_circular(graph, node_color='red', node_size=1000, with_labels=True)
    plt.savefig("Graf.jpg")
    plt.show()
    resE = []
    for i in range(0, len(E), 2):
        resE.append((int(E[i]), int(E[i + 1])))
    # print(resE)
    lis(V, resE)
    return 0



def lis(V, E):
    """Функция вычисления всех наибольших внутренне устойчивых множеств вершин графа G = (V, Е)

      Parameters
           ----------
           V : list
             Список вершин.
           E : list
             Список ребер

         Example
         -------
             >>> (V={1,2,3,4,5,6,7}, E={(1,2),(1,4),(1,6),(1,7),(2,4),(2,6),(3,4),(3,5),(3,6),(3,7),(4,5),(5,6),(6,7)})
            Максимальные внутренние устойчивые множества:
            V - {1,3,5,7} = {2,4,6}; V - {2,3,4,5,6} = {1,7}; V - {2,3,5,6,7} = {1,4};
            V - {1,2,4,6} = {3,5,7}; V - {1,3,4,6} = {2,5,7}.
            Наибольшие внутренне устойчивые множества:
            {2,4,6}; {3,5,7}; {2,5,7}

         Returns
         -------
         tuple
             Все максимальные устойчивые множеста, а также наибольшие из них.
      """
    res = E[0]
    for i in range(1, len(E)):
        tmp = []
        poglotitels = []
        for first_elem in res:
            for second_elem in E[i]:
                if str(first_elem) in str(second_elem):
                    tmp.append(second_elem)
                    poglotitels.append(second_elem)
                elif str(second_elem) in str(first_elem):
                    tmp.append(first_elem)
                    poglotitels.append(first_elem)
                else:
                    new_elem = ''.join(sorted(list(set(char for char in str(first_elem) + str(second_elem)))))
                    tmp.append(int(new_elem))
        res = list(set(tmp))
        poglotitels = list(set(poglotitels))
        for pop in poglotitels:
            res = test_pogloshenie(res, pop)

    final_stage = []
    for i in res:
        final_stage.append(list(map(int, [char for char in str(i)])))

    for i in range(len(final_stage)):
        final_stage[i] = tuple(set(V) - set(final_stage[i]))

    final_stage_lengths = dict()

    for i in final_stage:
        if len(i) in final_stage_lengths:
            final_stage_lengths[len(i)].append(i)
        else:
            final_stage_lengths[len(i)] = [i]
    print(final_stage, 'Максимальные внутренние устойчивые множества')
    print(final_stage_lengths[max(final_stage_lengths.keys())],'Наибольшие внутренне устойчивые множества')

    return 0


def pogloshenie(poglotitel, res):
    """Функция определения поглатителя

            Parameters
            ----------
            poglotitel : str
                Значение которое при умножении поглощает другое значение с которым умножается.
            res : str
                Результат умножения и поглошения(одного шага).

            Returns
            -------
            tuple
                Выводит значение True или False
       """
    pogl = [i for i in poglotitel]
    r = [i for i in res]
    flag = True
    for p in pogl:
        if p not in r:
            flag = False
    return flag


def test_pogloshenie(res, poglotitel):
    """Функция поглощения

              Parameters
              ----------
              poglotitel : str
                  Значение которое при умножении поглощает другое значение с которым умножается.
              res : str
                  Результат умножения.

              Returns
              -------
              tuple
                  Выводит финальный результат шага(результат поглащения)
         """
    final_res = []
    for r in res:
        if poglotitel == r or not pogloshenie(str(poglotitel), str(r)):
            final_res.append(r)
    return list(set(final_res))

def Start():
    """Функция запуска программы

            Example
            -------
            Вводим параметры V вершины и E ребра

            Returns
            -------
            tuple
                Выводит финальный результат шага(результат поглащения)
        """
    try:
        V = input("Введите вершины: ")
        # V = "{1,2,3,4,5,6,7}"
        E = input("Введите ребра: ")
        # E = "(1,2) (1,3) (1,5) (1,6) (2,3) (3,4) (3,6) (4,5) (4,7) (5,6) (6,7)"
        MakeGraphGreatAgain(V, E)
    except Exception as e:
        print(e)


# (V={1,2,3,4,5,6,7}, E={(1,2),(1,4),(1,6),(1,7),(2,4),(2,6),(3,4),(3,5),(3,6),(3,7),(4,5),(5,6),(6,7)})
# (V={1,2,3,4,5,6,7}, E={(1,2),(1,3),(1,4),(1,6),(2,3),(2,6),(3,4),(3,6),(3,7),(4,5),(4,7),(5,6),((6,7)}).
