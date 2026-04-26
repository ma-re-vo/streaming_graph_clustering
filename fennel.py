class FennelPartitioner:
    def __init__(self, graph, num_partitions, alpha):
        self.graph = graph
        self.partitions = [set() for _ in range(num_partitions)]
        self.alpha = alpha

    def connections(self, v, partition):
        return len(self.graph.get_neighbors(v).intersection(partition))

    def score(self, v, partition):
        return self.connections(v, partition) - self.alpha * len(partition)

    def choose_partition(self, v):
        scores = [self.score(v, p) for p in self.partitions]
        return scores.index(max(scores))

    def assign(self, v):
        p_idx = self.choose_partition(v)
        self.partitions[p_idx].add(v)
        return p_idx