import os
import matplotlib.pyplot as plt
import maze_utils as mu
import bfs, dfs, gbfs, astar

# =================== LEITURA E PREPARO DA MATRIZ ===================

linhas = mu.read_matrix("../data/labirinto3.txt")
matriz, start, goal = mu.tratar_matriz(linhas)

# =================== EXECUÇÃO DOS ALGORITMOS ===================

resultados = []

# Algoritmos sem heurística
resultados.append(mu.medir_desempenho("BFS", bfs.bfs, matriz, start, goal))
resultados.append(mu.medir_desempenho("DFS", dfs.dfs, matriz, start, goal))

# --- Heurística Manhattan ---
resultados.append(mu.medir_desempenho("GBFS-Manhattan", gbfs.gbfs, matriz, start, goal, mu.manhattan))
resultados.append(mu.medir_desempenho("A*-Manhattan", astar.astar, matriz, start, goal, mu.manhattan))

# --- Heurística Euclidiana ---
resultados.append(mu.medir_desempenho("GBFS-Euclidiana", gbfs.gbfs, matriz, start, goal, mu.euclidiana))
resultados.append(mu.medir_desempenho("A*-Euclidiana", astar.astar, matriz, start, goal, mu.euclidiana))

# =================== TERMINAL: HUB DE RESULTADOS ===================

print("\n" + "="*70)
print("COMPARATIVO GERAL DE ALGORITMOS DE BUSCA".center(70))
print("="*70)

print(f"{'Algoritmo':<18} | {'Heurística':<12} | {'Tempo (s)':<10} | {'Nós Exp.':<10} | {'Memória':<10} | {'Custo':<6}")
print("-"*70)

for r in resultados:
    if "-" in r["algoritmo"]:
        nome, heur = r["algoritmo"].split("-")
    else:
        nome, heur = r["algoritmo"], "-"
    print(f"{nome:<18} | {heur:<12} | {r['tempo']:<10.4f} | {r['nos_expandidos']:<10} | {r['memoria_max']:<10} | {r['custo']:<6}")

print("="*70)

# =================== ORGANIZAÇÃO DOS RESULTADOS (MODIFICADO) ===================

# (1) Todos os 6 resultados
resultados_geral = resultados

# (2) Apenas os 4 algoritmos com heurísticas para comparar entre si
resultados_heuristicas = [r for r in resultados if "Manhattan" in r["algoritmo"] or "Euclidiana" in r["algoritmo"]]


# Criação das pastas (MODIFICADO)
os.makedirs("../resultados/geral", exist_ok=True)
os.makedirs("../resultados/comparativo_heuristicas", exist_ok=True)


# =================== FUNÇÃO DE GERAÇÃO DE GRÁFICOS (MODIFICADO) ===================

def gerar_graficos(resultados, pasta_saida, titulo_extra=""):
    nomes = [r['algoritmo'] for r in resultados]
    tempos = [r['tempo'] for r in resultados]
    expandidos = [r['nos_expandidos'] for r in resultados]
    memoria = [r['memoria_max'] for r in resultados]
    custo = [r['custo'] for r in resultados]

    # Paleta de cores (diferente para cada algoritmo)
    cores = plt.cm.tab10.colors   # 10 cores distintas

    def plot_bar(y, titulo, ylabel, nome_arquivo):
        plt.figure(figsize=(9, 5))
        plt.bar(nomes, y, color=cores[:len(nomes)])
        plt.title(f"{titulo} {titulo_extra}", fontsize=13, fontweight='bold')
        plt.ylabel(ylabel)
        plt.xlabel("Algoritmo")
        plt.xticks(rotation=30, ha="right")
        plt.grid(axis="y", linestyle="--", alpha=0.6)
        plt.tight_layout()
        plt.savefig(f"{pasta_saida}/{nome_arquivo}.png", dpi=300)
        plt.close()

    # --- Títulos sem caracteres especiais ---
    plot_bar(tempos, "Tempo de Execução", "Tempo (s)", "tempo_execucao")
    plot_bar(expandidos, "Nós Expandidos", "Quantidade", "nos_expandidos")
    plot_bar(memoria, "Memória Máxima", "Nós armazenados", "memoria_maxima")
    plot_bar(custo, "Custo do Caminho", "Passos até o objetivo", "custo_caminho")

    print(f"✅ Gráficos salvos em: {pasta_saida}/")

# =================== GRÁFICOS SEPARADOS (MODIFICADO) ===================

# (1) Comparativo geral (todos os 6 algoritmos)
gerar_graficos(resultados_geral, "../resultados/geral", "(Comparativo Geral)")

# (2) Comparativo focado nas Heurísticas (GBFS vs A* | Manhattan vs Euclidiana)
gerar_graficos(resultados_heuristicas, "../resultados/comparativo_heuristicas", "(Comparativo de Heurísticas)")