import networkx as nx
from networkx.algorithms.community.quality import modularity


def compute_modularity(G, clusters):
    communities = list(clusters.values())
    return modularity(G, communities)

