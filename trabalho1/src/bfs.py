import maze_utils as mu
import time
from collections import deque

def bfs(matriz,start,goal):

    if start == goal:
         print("Caminho Encontrado:", start)
         return [start], 0, 1

    nos_expandidos=0

    dRow = [ -1, 0, 1, 0]
    dCol = [ 0, 1, 0, -1]

    fronteir = deque([(start, [start])])
    visited=set()
    
    max_mem = 1

    while (len(fronteir)>0):
        
        
        max_mem = max(max_mem, len(fronteir) + len(visited))

        cell, path = fronteir.popleft()
        nos_expandidos += 1
        visited.add(cell)
       
        x=cell[0]
        y=cell[1]

        for i in range(4):
            adjx=x+dRow[i]
            adjy=y+dCol[i]
            if(mu.is_valid_move(visited,adjx,adjy,matriz)):
                if (adjx, adjy) == goal:
                    path_final=path + [(adjx, adjy)]
                    print("Caminho Encontrado!"," Posições:",adjx,adjy)
                    mu.print_maze(matriz, visited, path_final)
                    return path_final,nos_expandidos, max_mem
                    
                fronteir.append(((adjx, adjy), path + [(adjx, adjy)]))


    print("Nenhum caminho encontrado.")
    return None,nos_expandidos, max_mem





