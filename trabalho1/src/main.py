import maze_utils as mu
import matplotlib.pyplot as plt
import bfs
import gbfs
import dfs
import astar

linhas = mu.read_matrix("../data/labirinto1.txt")
matriz, start, goal = mu.tratar_matriz(linhas)

resultados = []
resultados.append(mu.medir_desempenho("BFS", bfs.bfs, matriz, start, goal))
resultados.append(mu.medir_desempenho("DFS", dfs.dfs, matriz, start, goal))
resultados.append(mu.medir_desempenho("GBFS", gbfs.gbfs, matriz, start, goal, mu.manhattan))
resultados.append(mu.medir_desempenho("A*", astar.astar, matriz, start, goal, mu.manhattan))

# Exemplo simples de tabela de resumo
print("\n--- Resumo Comparativo ---")
for r in resultados:
    print(f"{r['algoritmo']:<6} | "
          f"Tempo: {r['tempo']:.4f}s | "
          f"Expandidos: {r['nos_expandidos']} | "
          f"Memória: {r['memoria_max']} | "
          f"Custo: {r['custo']}")

# --- Geração de gráficos comparativos ---
def gerar_graficos(resultados):
    nomes = [r['algoritmo'] for r in resultados]
    tempos = [r['tempo'] for r in resultados]
    expandidos = [r['nos_expandidos'] for r in resultados]
    memoria = [r['memoria_max'] for r in resultados]
    custo = [r['custo'] for r in resultados]

    # Gráfico 1: Tempo de execução
    plt.figure()
    plt.bar(nomes, tempos)
    plt.title("Tempo de Execução por Algoritmo")
    plt.ylabel("Tempo (s)")
    plt.xlabel("Algoritmo")
    plt.savefig("../resultados/tempo_execucao.png", dpi=300)
    plt.close()

    # Gráfico 2: Nós expandidos
    plt.figure()
    plt.bar(nomes, expandidos)
    plt.title("Nós Expandidos por Algoritmo")
    plt.ylabel("Nós Expandidos")
    plt.xlabel("Algoritmo")
    plt.savefig("../resultados/nos_expandidos.png", dpi=300)
    plt.close()

    # Gráfico 3: Memória máxima
    plt.figure()
    plt.bar(nomes, memoria)
    plt.title("Memória Máxima (Fronteira + Visitados)")
    plt.ylabel("Tamanho Máximo")
    plt.xlabel("Algoritmo")
    plt.savefig("../resultados/memoria_maxima.png", dpi=300)
    plt.close()

    # Gráfico 4: Custo do Caminho
    plt.figure()
    plt.bar(nomes, custo)
    plt.title("Custo do Caminho (passos até o objetivo)")
    plt.ylabel("Custo")
    plt.xlabel("Algoritmo")
    plt.savefig("../resultados/custo_caminho.png", dpi=300)
    plt.close()

    print("✅ Gráficos salvos na pasta 'resultados/'.")

# Criar pasta de saída (se não existir)
import os
os.makedirs("../resultados", exist_ok=True)

# Gera os gráficos com base nos resultados medidos
gerar_graficos(resultados)