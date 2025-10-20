import maze_utils as mu
import time

def dfs(matriz, start, goal):
    
    if start == goal:
        print("Caminho Encontrado:", start)
        return [start], 0, 1

    nos_expandidos = 0
    dRow = [-1, 0, 1, 0]
    dCol = [0, 1, 0, -1]

    fronteira = [(start, [start])]
    visitados = set()
    max_mem = 1

    while fronteira:
        
        max_mem = max(max_mem, len(fronteira) + len(visitados))
        cell, path = fronteira.pop()   # Pilha → remove último
        nos_expandidos += 1
        visitados.add(cell)

        x, y = cell
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]

            if mu.is_valid_move(visitados, adjx, adjy, matriz):
                novo_caminho = path + [(adjx, adjy)]
                if (adjx, adjy) == goal:
                    print("Caminho Encontrado!", adjx, adjy)
                    mu.print_maze(matriz, visitados, novo_caminho)
                    return novo_caminho, nos_expandidos, max_mem

                fronteira.append(((adjx, adjy), novo_caminho))

    print("Nenhum caminho encontrado.")
    return None, nos_expandidos, max_mem
