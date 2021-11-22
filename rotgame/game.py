from networkx import DiGraph


class Game:
    def __init__(self, nodes, edges, n=2):
        self.data = DiGraph()
        self.n = n
        for v in nodes:
            self.data.add_node(v, val=nodes[v] % n)
        for x, y in edges:
            self.data.add_edge(x, y)

    def win(self):
        for n in self.data:
            if self.data.nodes[n]['val'] > 0:
                return False
        return True

    def action(self, node):
        self.single(node)
        for v in self.data.adj[node].keys():
            self.single(v)

    def single(self, node):
        self.data.nodes[node]['val'] += 1
        self.data.nodes[node]['val'] %= self.n
