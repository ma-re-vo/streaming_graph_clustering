import networkx as nx

def modular_decomposition(graph_obj):
    G = nx.Graph()
    for node, neighbors in graph_obj.neighbors.items():
        for n in neighbors:
            G.add_edge(node, n)

    # используем Louvain как пример modular decomposition
    import community as community_louvain
    partition = community_louvain.best_partition(G)
    # возвращаем списки узлов по сообществам
    clusters = {}
    for node, com_id in partition.items():
        clusters.setdefault(com_id, []).append(node)
    return list(clusters.values())