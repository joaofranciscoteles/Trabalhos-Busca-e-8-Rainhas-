import maze_utils as mu
import time

def dfs(matriz, start, goal):
    
    if start == goal:
        print("Caminho Encontrado:", start)
        return [start], 0, 1

    nos_expandidos = 0
    
    
    dRow = [0, 0, 1, -1]
    dCol = [-1, 1, 0, 0]
   

    fronteir = [(start, [start])]
    visited = set()
    max_mem = 1

    while fronteir:
        
        max_mem = max(max_mem, len(fronteir) + len(visited))
        cell, path = fronteir.pop()   # Pilha → remove último
        nos_expandidos += 1
        
        visited.add((cell))
        
        # --- VISUALIZAÇÃO ---
        #mu.print_maze(matriz, visited, path)
        # ---------------------
       
        
        x, y = cell
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]

            if mu.is_valid_move(visited, adjx, adjy, matriz):
                
                novo_caminho = path + [(adjx, adjy)]
                if (adjx, adjy) == goal:
                    print("Caminho Encontrado!", adjx, adjy)
                    mu.print_maze(matriz, visited, novo_caminho)
                    return novo_caminho, nos_expandidos, max_mem

                fronteir.append(((adjx, adjy), novo_caminho))

    print("Nenhum caminho encontrado.")
    return None, nos_expandidos, max_mem
