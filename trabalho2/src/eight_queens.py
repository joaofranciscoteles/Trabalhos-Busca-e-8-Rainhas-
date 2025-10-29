import random
from typing import List, Iterable, Tuple

Board = List[int]          # lista com 8 posições: board[coluna] = linha
Move = Tuple[int, int]     # (coluna, nova_linha)
N = 8                      # tamanho do tabuleiro (8x8)

# ------------------------------------------------------------
# 1. GERAÇÃO DE UM TABULEIRO INICIAL
# ------------------------------------------------------------
def initial_board() -> Board:

    board = [random.randint(0, N - 1) for _ in range(N)]
    return board


# ------------------------------------------------------------
# 2. FUNÇÃO DE AVALIAÇÃO (CONFLITOS)
# ------------------------------------------------------------
def conflicts(board: Board) -> int:

    conflitos = 0
    for i in range(N):
        for j in range(i + 1, N):
            mesma_linha = board[i] == board[j]
            mesma_diagonal = abs(board[i] - board[j]) == abs(i - j)
            if mesma_linha or mesma_diagonal:
                conflitos += 1
    return conflitos


# ------------------------------------------------------------
# 3. GERAÇÃO DE VIZINHOS
# ------------------------------------------------------------
def neighbors(board: Board) -> Iterable[Move]:

    vizinhos = []
    for col in range(N):
        linha_atual = board[col]
        for nova_linha in range(N):
            if nova_linha != linha_atual:
                vizinhos.append((col, nova_linha))
    return vizinhos


# ------------------------------------------------------------
# 4. APLICA UM MOVIMENTO
# ------------------------------------------------------------
def apply(board: Board, move: Move) -> Board:

    col, nova_linha = move
    new_board = board.copy()
    new_board[col] = nova_linha
    return new_board

# ------------------------------------------------------------
# 5. IMPRESSÃO DO TABULEIRO
# ------------------------------------------------------------
def print_board(board: Board):

    print("\nTabuleiro final:")
    for row in range(N):
        linha = ""
        for col in range(N):
            linha += " Q " if board[col] == row else " . "
        print(linha)
    print()  



