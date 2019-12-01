from .game import Game
from .head import Head
from .domino import Domino
from .ia_programino import IAProgramino

# teste players com random
for x in range(0, 3):
    d = Domino(Head(float), Head(float))
    g = Game.new(starting_domino=d)

    while g.valid_moves:
        g.make_random_move()

    print(g)

# teste player 0 com random e player 1 com minimax
for x in range(0, 3):
    d = Domino(Head(float), Head(float))
    g = Game.new(starting_domino=d)

    while g.valid_moves:
        if g.turn == 0:  # se for o jogador 0
            g.make_random_move()
        else:
            move = IAProgramino().chose_better_move(g)
            g.make_move(*move)

    print(g)
