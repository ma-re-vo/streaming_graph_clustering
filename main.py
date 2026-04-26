from src.ingestion.reddit_stream import create_stream
from src.graph.graph_builder import Graph, process_post
from src.algorithms.fennel import FennelPartitioner
from config import NUM_PARTITIONS, ALPHA, MAX_POSTS
from src.visualization import draw_graph
from src.algorithms.cluster_quality import compute_modularity, dummy_oslom_genperm
from src.modular_decomp import modular_decomposition
import networkx as nx

def main():
    graph = Graph()
    fennel = FennelPartitioner(graph, NUM_PARTITIONS, ALPHA)

    stream = create_stream()

    for i, post in enumerate(stream):
        if i >= MAX_POSTS:
            break

        news_node = process_post(graph, post)
        if news_node is None:
            continue

        fennel.assign(news_node)

    # --- кластеризация проверка OSLOM / GenPerm ---
    partitions = dummy_oslom_genperm(graph, fennel.partitions)

    # --- модульная декомпозиция ---
    modular_clusters = modular_decomposition(graph)

    # --- визуализация ---
    draw_graph(graph, partitions=partitions)

    # --- метрика качества ---
    G_nx = nx.Graph()
    for node, neighbors in graph.neighbors.items():
        for n in neighbors:
            G_nx.add_edge(node, n)
    mod_score = compute_modularity(G_nx, partitions)
    print("Modularity of Fennel clusters:", mod_score)

if __name__ == "__main__":
    main()