from collections import defaultdict


class Graph:
    def __init__(self):
        self.neighbors = defaultdict(set)

    def add_edge(self, u, v):
        self.neighbors[u].add(v)
        self.neighbors[v].add(u)

    def get_neighbors(self, v):
        return self.neighbors[v]


def process_post(graph, post):
    if post.author is None:
        return None

    news_id = f"news_{post.id}"
    author_id = f"author_{post.author}"
    topic_id = f"topic_{post.subreddit}"

    graph.add_edge(news_id, author_id)
    graph.add_edge(news_id, topic_id)

    return news_id