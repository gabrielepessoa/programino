import csv
import os
import sys
import time
import copy
from datetime import datetime
from .game import Game
from .head import Head
from .domino import Domino
from .ia_programino import IAProgramino, Worst


# Recebendo parâmetros pela linha de comando
# ex: >> python -m programino 10 10
random_test_number = int(sys.argv[1])
ai_test_number = int(sys.argv[2])

# Definindo o nome dos arquivos a serem salvos
# com os resultados das simulações
now = datetime.now()
base_path = os.path.dirname(os.path.abspath(__file__))
base_file_name = base_path + '/experiments/{:%Y%m%d_%H%M%S}'.format(now)
random_file_name = base_file_name + '_random.csv'
ai_file_name = base_file_name + '_ai.csv'
wai_file_name = base_file_name + '_wai.csv'
worst_file_name = base_file_name + '_worst.csv'

# Iniciando o experimento
# print("\nO experimento será executado da seguinte forma:")
# print("({}) jogos de jogadas aleatórias x jogadas aleatórias".format(random_test_number))
print("({}) jogos de jogadas aleatórias x jogadas com minimax\n".format(ai_test_number))
# time.sleep(2)  # REMOVER AO EXECUTAR GRANDES EXPERIMENTOS


# Iniciando a simulação de (Aleatório x Aleatório)
# random_test_results = []
# total_random_test_result = [0, 0, 0]
# for count in range(0, random_test_number):
#     print("(Aleatório x Aleatório) Jogo {}:".format(count+1))

#     d = Domino(Head(float), Head(float))
#     game = Game.new(starting_domino=d)
#     while game.valid_moves:
#         game.make_random_move()

#     result = game.get_result()
#     random_test_results.append(result)
#     total_random_test_result[result.index(1)] += 1

#     print(result, end='\n\n')
#     # time.sleep(1)  # REMOVER AO EXECUTAR GRANDES EXPERIMENTOS

# print("Resultado da experiência: ", random_test_results, end='\n\n')

# # Salvando o resultado do experimento (Aleatório x Aleatório)
# with open(random_file_name, 'w') as random_experiment:
#     writer = csv.writer(random_experiment, delimiter=';')
#     writer.writerow(["player0", "player1", "stuck"])
#     writer.writerows(random_test_results)
#     writer.writerow(total_random_test_result)


# # Iniciando a simulação de (Aleatório x Minimax)
ai_test_results = []
total_ai_test_result = [0, 0, 0]
for count in range(0, ai_test_number):
    print("(Aleatório x Minimax) Jogo {}:".format(count + 1))

    d = Domino(Head(float), Head(float))
    game = Game.new(starting_domino=d)
    while game.valid_moves:
        if game.turn == 0:  # se for o jogador 0
            game.make_random_move()
        else:
            # move = IAProgramino().chose_better_move(game)
            game_copy = copy.deepcopy(game)
            game_copy.skinny_board()
            move = IAProgramino().chose_better_move(game_copy)
            game.make_move(*move)

    result = game.get_result()
    ai_test_results.append(result)
    total_ai_test_result[result.index(1)] += 1

    print(result, end='\n\n')

print("Resultado da experiência: ", ai_test_results, end='\n\n')

# Salvando o resultado do experimento (Aleatório x Minimax)
with open(ai_file_name, 'w') as ai_experiment:
    writer = csv.writer(ai_experiment, delimiter=';')
    writer.writerow(["player0", "player1", "stuck"])
    writer.writerows(ai_test_results)
    writer.writerow(total_ai_test_result)


# Iniciando a simulação de (Aleatório x Worst)
# worst_test_results = []
# total_worst_test_result = [0, 0, 0]
# for count in range(0, ai_test_number):
#     #print("(Aleatório x Minimax) Jogo {}:".format(count + 1))
#     d = Domino(Head(float), Head(float))
#     game = Game.new(starting_domino=d)
#     while game.valid_moves:
#         if game.turn == 0:  # se for o jogador 0
#             game.make_random_move()
#         else:
#             game_copy = copy.deepcopy(game)
#             game_copy.skinny_board()
#             move = Worst().chose_worst_move(game_copy)
#             game.make_move(*move)
#     result = game.get_result()
#     worst_test_results.append(result)
#     total_worst_test_result[result.index(1)] += 1
#     print(result, end='\n\n')
# print("Resultado da experiência: ", worst_test_results, end='\n\n')
# # Salvando o resultado do experimento (Aleatório x Minimax)
# with open(worst_file_name, 'w') as worst_experiment:
#     writer = csv.writer(worst_experiment, delimiter=';')
#     writer.writerow(["player0", "player1", "stuck"])
#     writer.writerows(worst_test_results)
#     writer.writerow(total_worst_test_result)

# print("DONE!")

# Iniciando a simulação de (Worst x Minimax)
ai_test_results = []
total_ai_test_result = [0, 0, 0]
for count in range(0, ai_test_number):
    print("(Worst x Minimax) Jogo {}:".format(count+1))

    d = Domino(Head(float), Head(float))
    game = Game.new(starting_domino=d)
    while game.valid_moves:
        if game.turn == 0:  # se for o jogador 0
            game_copy = copy.deepcopy(game)
            game_copy.skinny_board()
            move = Worst().chose_worst_move(game_copy)
            game.make_move(*move)
        else:
            game_copy = copy.deepcopy(game)
            game_copy.skinny_board()
            move = IAProgramino().chose_better_move(game_copy)
            game.make_move(*move)

    result = game.get_result()
    ai_test_results.append(result)
    total_ai_test_result[result.index(1)] += 1

    print(result, end='\n\n')
    # time.sleep(1)  # REMOVER AO EXECUTAR GRANDES EXPERIMENTOS

print("Resultado da experiência: ", total_ai_test_result, end='\n\n')

# Salvando o resultado do experimento (Worst x Minimax)
with open(wai_file_name, 'w') as ai_experiment:
    writer = csv.writer(ai_experiment, delimiter=';')
    writer.writerow(["player0", "player1", "stuck"])
    writer.writerows(ai_test_results)
    writer.writerow(total_ai_test_result)

print("DONE!")