import maze_utils as mu
import time
from queue import PriorityQueue 

def gbfs(maze,start, goal, heuristic):

    dRow = [ -1, 0, 1, 0]
    dCol = [ 0, 1, 0, -1]

    nos_expandidos=0
    fronteir = PriorityQueue()
    fronteir.put((heuristic(start,goal),start,[start]))

    visited = set()

    while not fronteir.empty():
        
        cost, cell, path = fronteir.get()

        nos_expandidos+=1

        if cell == goal:
            print("Caminho Encontrado!",cell[0],cell[1])
            mu.print_maze(maze, visited, path)
            return path,nos_expandidos
        
        visited.add(cell)
        
        x=cell[0]
        y=cell[1]

        for d in range(4):
            adjx = x+ dRow[d]
            adjy = y+ dCol[d]
            if mu.is_valid_move(visited,adjx,adjy,maze):
                new_cost = heuristic((adjx,adjy), goal)
                fronteir.put((new_cost, (adjx,adjy), path + [(adjx,adjy)]))
                
    print("Nenhum caminho encontrado.")
    return None,nos_expandidos

    