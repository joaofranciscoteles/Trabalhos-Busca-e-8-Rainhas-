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

    resultado = func(*args)
    fim = time.time()
    tempo = fim - inicio

    # Tratamento flexível (compatível com funções antigas)
    if len(resultado) == 3:
        path, nos_expandidos, max_mem = resultado
    else:
        path, nos_expandidos = resultado
        max_mem = None

    # Métricas básicas
    if path:
        custo = len(path) - 1
        print("✅ Caminho encontrado!")
        print(f"Custo da solução: {custo}")
    else:
        custo = None
        print(" Nenhum caminho encontrado.")

    # Exibição das métricas
    print(f"Nós expandidos: {nos_expandidos}")
    if max_mem is not None:
        print(f"Memória máxima (fronteira + visitados): {max_mem}")
    print(f"Tempo de execução: {tempo:.4f} segundos")
    print("=========================\n")

    return {
        "algoritmo": nome,
        "tempo": tempo,
        "nos_expandidos": nos_expandidos,
        "memoria_max": max_mem,
        "custo": custo
    }


def print_maze(matriz, visited=set(), path=[]):
    for i, row in enumerate(matriz):
        linha = ""
        for j, val in enumerate(row):
            if (i, j) in path:
                linha += "🟩"  # caminho solução
            elif (i, j) in visited:
                linha += "🟦"  # caminho explorado
            elif val == 1:
                linha += "⬛"  # parede
            else:
                linha += "⬜"  # espaço livre
        print(linha)
    print("\n")


