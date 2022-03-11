import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image
# from colorit import background, init_colorit


def MakeGraphGreatAgain(V, E):
    graph = nx.Graph()
    V = list(map(int, V.split()))
    E = list(map(int, E.split()))
    # print(V)
    # print(E)
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
    plt.savefig("Graf.png")
    plt.show()
    # MakePicture()
    print(dfs(res))
    return 0

# def MakePicture():
#     init_colorit()
#     depth = 100
#     image = Image.open("Graf.png")
#     image = image.resize((depth, depth))
#     for y in range(image.size[1]):
#         for x in range(image.size[0]):
#             print(background(" ", image.getpixel((x, y))), end='')
#         print()


def dfs(res):
    print("Все работатет")
    return 0

# V = input()
V = "{1,2,3,4,5,6,7}"
V = V.replace('{','' ).replace('}','').replace(',',' ')
# E = input()
E = "{(1,2),(1,3),(1,5),(1,6),(2,3),(3,4),(3,6),(4,5),(4,7),(5, 6),(6,7)}"
E = E.replace('{','' ).replace('}','').replace('(','' ).replace(')','').replace(',',' ')
MakeGraphGreatAgain(V, E)

# {1,2,3,4,5,6,7}
# {(1,2),(1,3),(1,4),(2,3)