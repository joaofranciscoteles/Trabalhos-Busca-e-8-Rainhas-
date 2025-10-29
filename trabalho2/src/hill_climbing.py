import random
from eight_queens import initial_board, conflicts, neighbors, apply

def hill_climbing_simple(board=None, max_iter=1000):

    if board is None:
        board = initial_board()

    atual = board
    atual_conflitos = conflicts(atual)
    iteracoes = 0

    while iteracoes < max_iter:
        iteracoes += 1

        vizinhos = neighbors(atual)

        melhor_vizinho = None
        melhor_conflitos = float("inf")

        for mv in vizinhos:
            novo_board = apply(atual, mv)
            c = conflicts(novo_board)
            if c < melhor_conflitos:
                melhor_conflitos = c
                melhor_vizinho = novo_board

        if melhor_conflitos < atual_conflitos:
            atual = melhor_vizinho
            atual_conflitos = melhor_conflitos
        else:

            break

        if atual_conflitos == 0:
            break

    return atual, atual_conflitos, iteracoes

def hill_climbing_sideways(board=None, max_iter=1000, max_sideways=100):
    if board is None:
        board = initial_board()

    atual = board
    atual_conflitos = conflicts(atual)
    iteracoes = 0
    movimentos_laterais = 0

    while iteracoes < max_iter:
        iteracoes += 1
        vizinhos = neighbors(atual)
        melhor_vizinho = None
        melhor_conflitos = float("inf")

        for mv in vizinhos:
            novo_board = apply(atual, mv)
            c = conflicts(novo_board)
            if c < melhor_conflitos:
                melhor_conflitos = c
                melhor_vizinho = novo_board

        if melhor_conflitos < atual_conflitos:
            atual = melhor_vizinho
            atual_conflitos = melhor_conflitos
            movimentos_laterais = 0
        elif melhor_conflitos == atual_conflitos:
           
            if movimentos_laterais < max_sideways:
                atual = melhor_vizinho
                movimentos_laterais += 1
            else:
                break 
        else:
            break  

        if atual_conflitos == 0:
            break

    return atual, atual_conflitos, iteracoes

def hill_climbing_random_restart(max_restarts=100, max_iter=1000):
    total_iter = 0
    for restart in range(max_restarts):
        board = initial_board()
        result, conf, it = hill_climbing_simple(board, max_iter)
        total_iter += it
        if conf == 0:
            return result, conf, total_iter, restart
    return None, None, total_iter, max_restarts

