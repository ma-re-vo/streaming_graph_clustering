import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def draw_graph(graph_obj, partitions=None):
    G = nx.Graph()
    for node, neighbors in graph_obj.neighbors.items():
        for n in neighbors:
            G.add_edge(node, n)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12, 8))

    if partitions:
        colors = cm.rainbow(np.linspace(0, 1, len(partitions)))
        for color, part in zip(colors, partitions):
            nx.draw_networkx_nodes(G, pos, nodelist=list(part), node_color=[color]*len(part), alpha=0.7)
    else:
        nx.draw_networkx_nodes(G, pos, node_size=50, alpha=0.7)

    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.title("Reddit Graph Clusters")
    plt.axis("off")
    plt.show()