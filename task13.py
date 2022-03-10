import networkx as nx
import matplotlib.pyplot as plt


def MakeGraphGreatAgain(V, E):
    graph = nx.Graph()
    V = list(map(int, V.split()))
    E = list(map(int, E.split()))
    res = []
    temp = 0
    tmp = []
    for i in E:
        tmp.append(i)
        temp += 1
        if temp % 2 == 0:
            res.append(tmp)
            tmp = []
    graph.add_nodes_from(V)
    graph.add_edges_from(res)
    nx.draw_circular(graph, node_color='red', node_size=1000, with_labels=True)
    plt.show()
    return 0

V = input()
V = V.replace('{','' ).replace('}','').replace(',',' ')
E = input()
E = E.replace('{','' ).replace('}','').replace('(','' ).replace(')','').replace(',',' ')
MakeGraphGreatAgain(V, E)

