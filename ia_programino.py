from .game import Game
import math
class IAProgramino():
	pass
# 	def playRandom(game):
# 	return qualquer das peças jogaveis

# 	def playMax(game)
# 		# humano é player 0
# 		# máquina é player 1
# 		if Game.valid_moves = (): # se o jogo acabou: retorna +1, se maquina venceu; retorna -1 se humano venceu; retorna 0, se empate.
# 			if Game.turn == 0:
# 				return -1 # humano venceu
# 			elif Game.turn == 1:
# 				return 1 # máquina venceu
# 			else:
# 				return 0 # empate
# 		vmax = -math.inf
# 		pecaMax = null
# 		for domino in Game.valid_moves: # para cada peça X do conjunto JOGÁVEL (pela máquina)
# 			gcopy = copy.deepcopy(game) #cria uma cópia do jogo
# 			gcopy.jogarPeca(X, máquina)
# 			v = playMin(gcopy)
# 			if (v > vmax)
# 				vmax = v
# 				pecaMax = X
# 		return pecaMax

# 	def playMin(game)
# 		# humano é player 0
# 		# máquina é player 1
# 		if Game.valid_moves = (): # se o jogo acabou: retorna +1, se maquina venceu; retorna -1 se humano venceu; retorna 0, se empate.
# 			if Game.turn = 0:
# 				return -1 # humano venceu
# 			elif Game.turn = 1:
# 				return +1 # máquina venceu
# 			else:
# 				return 0 # empate 
# 		vmin = math.inf
# 		pecaMin = null
# 		for domino in Game.valid_moves: # para cada peça X do conjunto JOGÁVEL (pelo humano)
# 			gcopy = copy.deepcopy(game) #cria uma cópia do jogo
# 			gcopy.jogarPeca(X, humano)
# 			v = playMax(gcopy)
# 			if (v > vmin)
# 				vmin = v
# 				pecaMin = X
# 		return pecaMin 
# 			