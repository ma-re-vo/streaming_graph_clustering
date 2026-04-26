class FennelClustering:
    def __init__(self, k=5, alpha=1.5):
        self.k = k
        self.alpha = alpha
        self.clusters = {i: set() for i in range(k)}

    def assign(self, node, G):
        best_cluster = None
        best_score = float('-inf')

        for c in range(self.k):
            internal_edges = sum(
                1 for neighbor in G.neighbors(node)
                if neighbor in self.clusters[c]
            )

            size_penalty = self.alpha * len(self.clusters[c])
            score = internal_edges - size_penalty

            if score > best_score:
                best_score = score
                best_cluster = c

        self.clusters[best_cluster].add(node)
        return best_cluster

    def run(self, G):
        for node in G.nodes():
            if not any(node in c for c in self.clusters.values()):
                self.assign(node, G)
        return self.clusters
