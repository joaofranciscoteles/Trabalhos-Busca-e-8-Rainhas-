import time
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def read_matrix(nome_arquivo):
    
    with open(nome_arquivo, "r") as f:
        linhas = [linha.strip() for linha in f]
    return linhas

def tratar_matriz(linhas):
   
    matriz = []
    start = None
    goal = None
    
    for i, linha in enumerate(linhas):
        linha_convertida = []
        for j, ch in enumerate(linha):
            if ch == '#':
                linha_convertida.append(1)
            else:
                linha_convertida.append(0)
            
            if ch == 'S':
                start = (i, j)
            elif ch == 'G':
                goal = (i, j)
                
        matriz.append(linha_convertida)
    
    return matriz, start, goal

def is_valid_move(visited,row,col,matriz):

    if(row<0 or col<0 or row>=len(matriz) or col>=len(matriz[0])):
        return False
    
    if(matriz[row][col]==1):
        return False
    
    if((row,col) in visited):
        return False
    
    return True

def medir_desempenho(nome, func, *args):
    print(f"\n=== {nome} ===")
    inicio = time.time()
    path, nos_expandidos = func(*args)
    fim = time.time()
    tempo = fim - inicio

    if path:
            print("Caminho Encontrado")
    else:
            print("Nenhum caminho encontrado.")
    
    print(f"Nós expandidos: {nos_expandidos}")
    print(f"Tempo de execução: {tempo:.4f} segundos")
    print("=========================")


def print_maze(matriz, visited=set(), path=[]):
    for i, row in enumerate(matriz):
        linha = ""
        for j, val in enumerate(row):
            if (i, j) in path:
                linha += "*"
            elif (i, j) in visited:
                linha += "*"
            elif val == 1:
                linha += "#"
            else:
                linha += "."
        print(linha)
    print("\n")

    
