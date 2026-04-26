import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(G, clusters=None):
    pos = nx.spring_layout(G)

    if clusters:
        color_map = {}
        for c, nodes in clusters.items():
            for n in nodes:
                color_map[n] = c
        colors = [color_map.get(node, 0) for node in G.nodes()]
    else:
        colors = 'blue'

    nx.draw(G, pos, node_color=colors, node_size=30, with_labels=False)
    plt.show()
