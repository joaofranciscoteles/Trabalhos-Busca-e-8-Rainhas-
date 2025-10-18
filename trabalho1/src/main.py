import maze_utils as mu
import bfs
import gbfs

linhas=mu.read_matrix("../data/labirinto1.txt")
matriz,start,goal=mu.tratar_matriz(linhas)

mu.medir_desempenho("BFS", bfs.bfs, matriz, start, goal)
mu.medir_desempenho("GBFS", gbfs.gbfs, matriz, start, goal, mu.manhattan)
