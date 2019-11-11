from .game import Game
import math
import copy


class IAProgramino:

    def __init__(self): 
        self.run = 0 # qtd de iterações do algoritmo

    def chose_better_move(self, game):
        move = self.play_max(game, True)
        print(self.run)
        return move

    def play_max(self, game, is_root=False):
        # humano é player 0
        # máquina é player 1
        # se o jogo acabou: retorna +1, se maquina venceu; retorna -1 se humano venceu; retorna 0, se empate.
        self.run += 1
        game = copy.deepcopy(game)
        if not game.valid_moves:
            if game.turn == 0:
                # print("Humano venceu!\n")
                return -1  # humano venceu
            elif game.turn == 1:
                # print("Máquina venceu!\n")
                return 1  # máquina venceu
            else:
                # print("Empate!\n")
                return 0  # empate
        vmax = -math.inf
        max_move = None

        # para cada peça X do conjunto JOGÁVEL (pela máquina)
        for move in game.valid_moves:
            gcopy = copy.deepcopy(game)  # cria uma cópia do jogo
            gcopy.make_move(*move)  # faz jogada para a máquina
            v = self.play_min(gcopy)  # chama o play_min para o humano
            if v > vmax:
                vmax = v
                max_move = move

        return max_move if is_root else vmax

    def play_min(self, game):
        # humano é player 0
        # máquina é player 1
        # se o jogo acabou: retorna +1, se maquina venceu; retorna -1 se humano venceu; retorna 0, se empate.
        self.run += 1
        game = copy.deepcopy(game)
        if not game.valid_moves:
            if game.turn == 0:
                # print("Humano venceu!\n")
                return -1  # humano venceu
            elif game.turn == 1:
                # print("Máquina venceu!\n")
                return 1  # máquina venceu
            else:
                # print("Empate!\n")
                return 0  # empate
        vmin = math.inf
        min_move = None

        # para cada peça X do conjunto JOGÁVEL (pelo humano)
        for move in game.valid_moves:
            gcopy = copy.deepcopy(game)  # cria uma cópia do jogo
            gcopy.make_move(*move)  # faz jogada para o humano
            v = self.play_max(gcopy)  # chama o play_max para a máquina
            if v < vmin:
                vmin = v
                min_move = move
        return vmin
