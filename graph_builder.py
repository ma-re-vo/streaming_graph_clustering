import networkx as nx
from collections import defaultdict

class GraphBuilder:
    def __init__(self):
        self.G = nx.Graph()
        self.post_users = defaultdict(set)

    def process(self, data):
        user = data.get("author")
        post = data.get("link_id")

        if not user or user == "[deleted]":
            return self.G

        self.post_users[post].add(user)
        users = list(self.post_users[post])

        for i in range(len(users)):
            for j in range(i + 1, len(users)):
                u1, u2 = users[i], users[j]

                if self.G.has_edge(u1, u2):
                    self.G[u1][u2]['weight'] += 1
                else:
                    self.G.add_edge(u1, u2, weight=1)

        return self.G
