import matplotlib.pyplot as plt
import networkx as nx


# from colorit import background, init_colorit


def New_graph(V, E):
    """Функция создания неориентированного графа.

             Parameters
             ----------
             V : str
               Список вершин.
             E : str
               Список ребер

             Returns
             -------
             int
                Построенный граф и картинку графа в формате jpg.

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
            tmp = []    # print(res)
    graph.add_nodes_from(V)
    graph.add_edges_from(res)
    nx.draw_circular(graph, node_color='red', node_size=1000, with_labels=True)
    plt.savefig("Graf.jpg")
    plt.show()
    resE = []
    for i in range(0, len(E), 2):
        resE.append((int(E[i]), int(E[i + 1])))
    # print(resE)
    Dfs(V, resE)
    return 0


def Dfs(V, E):
    """Функция вычисления всех наименьшие внутренне устойчивых множеств вершин графа G = (V, Е)

          Parameters
               ----------
               V : list
                 Список вершин.
               E : list
                 Список ребер

             Example
             -------
                 >>> (V={1,2,3,4,5,6,7}, E={(1,2),(1,4),(1,6),(1,7),(2,4),(2,6),(3,4),(3,5),(3,6),(3,7),(4,5),(5,6),(6,7)})
                Минимальные внешне устойчивые множества вершин:
                {2,6,7}, {1,7}, {3,5,7}, {2,5,7}, {2,4,7}, {2,4,6},
                {1,4}, {3,4}, {2,4,5}, {2,5,6},{3,6}, {1,5,6}.
                Наименьшие внешне устойчивые множества вершин:
                {1,7}, {1,4}, {3,4}, {3,6}.

             Returns
             -------
             int
                 Все минимальные внешние устойчивые множеста, а также наименьшие из них.
          """
    temp = dict()
    for i in V:
        for j in E:
            if i in j:
                if i in temp:
                    for t in list(set(j) - {i}):
                        temp[i].append(t)
                else:
                    temp[i] = [t for t in list(set(j) - {i})]

    tmp_res = []
    for i in temp.items():
        tmp = []
        tmp.append(i[0])
        for j in i[1]:
            tmp.append(j)
        tmp_res.append(tmp)

    res = tmp_res[0]
    for i in range(1, len(tmp_res)):
        tmp = []
        Absorber = []
        for first_elem in res:
            for second_elem in tmp_res[i]:
                if str(first_elem) in str(second_elem):
                    tmp.append(second_elem)
                    Absorber.append(second_elem)
                elif str(second_elem) in str(first_elem):
                    tmp.append(first_elem)
                    Absorber.append(first_elem)
                else:
                    new_elem = ''.join(sorted(list(set(char for char in str(first_elem) + str(second_elem)))))
                    tmp.append(int(new_elem))
        res = list(set(tmp))
        Absorber = list(set(Absorber))
        for pop in Absorber:
            res = Absorb_test(res, pop)

    final_stage = []
    for i in res:
        final_stage.append(list(map(int, [char for char in str(i)])))

    final_stage_lengths = dict()

    for i in final_stage:
        if len(i) in final_stage_lengths:
            final_stage_lengths[len(i)].append(i)
        else:
            final_stage_lengths[len(i)] = [i]

    print("Все минимальные внешне устойчивые множества вершин: ", final_stage)
    print("Наименьшие по мощности: ", final_stage_lengths[min(final_stage_lengths.keys())])
    return 0


def Absorb(absorber, res):
    """Функция определения поглатителя

               Parameters
               ----------
               absorber : str
                   Значение которое при умножении поглощает другое значение с которым умножается.
               res : str
                   Результат умножения и поглошения(одного шага).

               Returns
               -------
               bool
                   Выводит значение True или False
          """
    abs = [i for i in absorber]
    r = [i for i in res]
    flag = True
    for p in abs:
        if p not in r:
            flag = False
    return flag


def Absorb_test(res, absorber):
    """Функция поглощения

              Parameters
              ----------
              absorber : str
                  Значение которое при умножении поглощает другое значение с которым умножается.
              res : str
                  Результат умножения.

              Returns
              -------
              list
                  Выводит финальный результат шага(результат поглащения)
         """
    final_res = []
    for r in res:
        if absorber == r or not Absorb(str(absorber), str(r)):
            final_res.append(r)
    return list(set(final_res))

def Start():
    """Функция запуска программы
        Выводит финальный результат шага(результат поглащения).
              Example
              -------
              Вводим параметры V вершины и E ребра.

          """
        # print("Введите вершины графа: ")
    try:
        V = input("Введите вершины графа: ")
        # V = "{1,2,3,4,5,6,7}"
        # print("Введите ребра графа: ")
        E = input("Введите ребра графа: ")
        # E = "(1,2) (1,3) (1,5) (1,6) (2,3) (3,4) (3,6) (4,5) (4,7) (5,6) (6,7)"
        New_graph(V, E)
    except Exception as e:
        print(e)

# (V={1,2,3,4,5,6,7}, E={(1,2),(1,4),(1,6),(1,7),(2,4),(2,6),(3,4),(3,5),(3,6),(3,7),(4,5),(5,6),(6,7)})
# (V={1,2,3,4,5,6,7}, E={(1,2),(1,3),(1,4),(1,6),(2,3),(2,6),(3,4),(3,6),(3,7),(4,5),(4,7),(5,6),((6,7)}).
