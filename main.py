from src.ingestion.pushshift_stream import PushshiftStream
from src.graph.graph_builder import GraphBuilder
from src.algorithms.fennel import FennelClustering
from src.algorithms.cluster_quality import compute_modularity


def main():
    stream = PushshiftStream("data/comments.jsonl", delay=0.0005)
    graph_builder = GraphBuilder()
    fennel = FennelClustering(k=5)

    step = 0

    for data in stream.stream():
        G = graph_builder.process(data)
        clusters = fennel.run(G)

        step += 1

        if step % 2000 == 0:
            mod = compute_modularity(G, clusters)
            print(f"Step {step} | Nodes: {len(G.nodes())} | Modularity: {mod:.4f}")


if __name__ == "__main__":
    main()
