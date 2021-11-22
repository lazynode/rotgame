from rotgame.game import Game
from random import randrange


if __name__ == '__main__':
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

    game = Game(nodes, edges, N)

    print('''INITIAL STATE''')
    print('''''')
    print('''==== nodes ====''')
    print(game.data.nodes.data())
    print('''==== edges ====''')
    print(game.data.edges)
    print('''''')

    while game.win() == False:
        print('''>>> type your action''')
        action = input('enter your action (e.g: `(1,1)`):')
        data = eval(action, {}, {})
        game.action(data)
        print('''==== nodes ====''')
        print(game.data.nodes.data())
