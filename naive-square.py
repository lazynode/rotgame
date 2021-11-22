from rotgame.game import Game
from random import randrange


class G(Game):
    def __init__(self):
        N = 2
        nodes = {
            (0, 0): randrange(N),
            (0, 1): randrange(N),
            (1, 0): randrange(N),
            (1, 1): randrange(N),
        }
        edges = [
            v
            for x, y in nodes
            for v in [
                ((x, y), (1-x, y)),
                ((x, y), (x, 1-y)),
            ]
        ]
        super().__init__(nodes, edges, n=N)

    def list_nodes(self):
        '''
        `list_nodes()`: list all nodes of the graph;
        '''
        print()
        for v in self.data.nodes:
            print(v, '=>', self.data.nodes[v]['val'])
        print()

    def list_edges(self):
        '''
        `list_edges()`: list all edges of the graph;
        '''
        print()
        for x, y in self.data.edges.keys():
            print(x, '=>', y)
        print()

    def list_neighbours(self, node):
        '''
        `list_neighbours(NODE)`: list neighbours of a node;
        where `NODE` is the node you want to show neighbours;
        '''
        print()
        for v in self.data.adj[node].keys():
            print(v)
        print()

    def rotate_node(self, node):
        '''
        `rotate_node(NODE)`: perform an action of the game;
        where `NODE` is the node you want to rotate;
        '''
        self.action(node)
        self.list_nodes()

    def get_help(self, cmd=None):
        '''
        `get_help()`: show help message and list cmds;
        `get_help(CMD)`: show help message of a cmd;
        '''
        if cmd is None:
            print()
            print('type `get_help(CMD)` to see help for `CMD`;')
            print('`CMD` is one of available cmds below:')
            print()
            for v in self.cmd:
                print(v)
            print()
            return
        print()
        print(cmd.__doc__)
        print()

    @ property
    def cmd(self):
        return {
            'list_nodes': self.list_nodes,
            'list_edges': self.list_edges,
            'list_neighbours': self.list_neighbours,
            'rotate_node': self.rotate_node,
            'get_help': self.get_help,
        }


if __name__ == '__main__':
    game = G()
    print('''GAME START''')

    game.list_nodes()

    while game.win() == False:
        action = input('cmd (type `get_help()` to see all) >>> ')
        try:
            node = eval(action, {}, game.cmd)
            if node is not None:
                game.action(node)
        except:
            print()
            print('ERROR!!!')
            print()
            if action in game.cmd:
                print('''maybe you should type `{}(...)`'''.format(action))
                print('''`...` is the args''')
                print()

    print('''YOU WIN!!!''')
