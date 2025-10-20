import maze_utils as mu
from queue import PriorityQueue
import time

def astar(matriz, start, goal, heuristic):
    
    dRow = [-1, 0, 1, 0]
    dCol = [0, 1, 0, -1]

    nos_expandidos = 0
    fronteira = PriorityQueue()
    fronteira.put((heuristic(start, goal), 0, start, [start]))  # (f, g, estado, caminho)
    visitados = set()
    max_mem = 1

    while not fronteira.empty():
        
        max_mem = max(max_mem, fronteira.qsize() + len(visitados))
        f, g, cell, path = fronteira.get()
        nos_expandidos += 1

        if cell == goal:
            print("Caminho Encontrado!", cell[0], cell[1])
            mu.print_maze(matriz, visitados, path)
            return path, nos_expandidos, max_mem

        visitados.add(cell)

        x, y = cell
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]

            if mu.is_valid_move(visitados, adjx, adjy, matriz):
                g_novo = g + 1
                h_novo = heuristic((adjx, adjy), goal)
                f_novo = g_novo + h_novo
                fronteira.put((f_novo, g_novo, (adjx, adjy), path + [(adjx, adjy)]))

    print("Nenhum caminho encontrado.")
    return None, nos_expandidos, max_mem
