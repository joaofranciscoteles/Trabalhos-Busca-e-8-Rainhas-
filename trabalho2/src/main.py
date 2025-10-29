from eight_queens import initial_board, conflicts, print_board
from hill_climbing import (
    hill_climbing_simple,
    hill_climbing_sideways,
    hill_climbing_random_restart,
)
import time
import random
import matplotlib.pyplot as plt

def run_once():
    random.seed(42)
    board = initial_board()
    print("Tabuleiro inicial:", board)
    print("Conflitos iniciais:", conflicts(board))

    resultados = []

    for nome, func in [
        ("Simples", hill_climbing_simple),
        ("Movimentos Laterais", hill_climbing_sideways),
        ("Reinício Aleatório", hill_climbing_random_restart),
    ]:
        start = time.time()
        result = func()
        end = time.time()

        print(f"\n{nome}:")
        print("Resultado:", result[0] if result[0] else "Sem solução")
        print("Conflitos finais:", result[1])
        print("Iterações:", result[2])
        print("Tempo:", round(end - start, 4), "s")

        if result[0]:
            print_board(result[0])

        resultados.append((nome, result[1], result[2], end - start))

    # --- GERAR GRÁFICOS DA EXECUÇÃO ÚNICA ---
    nomes = [r[0] for r in resultados]
    conflitos = [r[1] for r in resultados]
    iteracoes = [r[2] for r in resultados]
    tempos = [r[3] for r in resultados]

    plt.figure()
    plt.bar(nomes, conflitos)
    plt.ylabel("Conflitos finais")
    plt.title("Conflitos finais - Execução única - Seed(42)")
    plt.show()

    plt.figure()
    plt.bar(nomes, iteracoes)
    plt.ylabel("Iterações")
    plt.title("Iterações - Execução única - Seed(42)")
    plt.show()

    plt.figure()
    plt.bar(nomes, tempos)
    plt.ylabel("Tempo (s)")
    plt.title("Tempo - Execução única - Seed(42)")
    plt.show()

    return resultados


# ------------------------------------------------------------
#  GERAR GRÁFICOS 
# ------------------------------------------------------------
def run_experiments(n_exec=30):
    resultados = {
        "Simples": [],
        "Laterais": [],
        "Reinício Aleatório": [],
    }

    for _ in range(n_exec):
        random.seed()
        # Hill Climbing simples
        start = time.time()
        _, conf, it = hill_climbing_simple()
        resultados["Simples"].append((conf, it, time.time() - start))

        # Hill Climbing com movimentos laterais
        start = time.time()
        _, conf, it = hill_climbing_sideways()
        resultados["Laterais"].append((conf, it, time.time() - start))

        # Hill Climbing com reinício aleatório
        start = time.time()
        _, conf, it, _ = hill_climbing_random_restart()
        resultados["Reinício Aleatório"].append((conf, it, time.time() - start))

    return resultados


def plot_metrics(resultados):
    labels = list(resultados.keys())
    tempos = [sum(v[2] for v in resultados[k]) / len(resultados[k]) for k in labels]
    iteracoes = [sum(v[1] for v in resultados[k]) / len(resultados[k]) for k in labels]
    sucesso = [sum(1 for v in resultados[k] if v[0] == 0) / len(resultados[k]) * 100 for k in labels]

    # --- Tempo médio ---
    plt.figure()
    plt.bar(labels, tempos)
    plt.ylabel("Tempo médio (s)")
    plt.title("Tempo médio por variação")
    plt.show()

    # --- Iterações médias ---
    plt.figure()
    plt.bar(labels, iteracoes)
    plt.ylabel("Iterações médias")
    plt.title("Iterações por variação")
    plt.show()

    # --- Taxa de sucesso ---
    plt.figure()
    plt.bar(labels, sucesso)
    plt.ylabel("Taxa de sucesso (%)")
    plt.title("Taxa de sucesso (solução encontrada)")
    plt.show()


if __name__ == "__main__":
    print("=== Execução Única ===")
    run_once()

    print("\n=== Rodando Experimentos (30 execuções) ===")
    resultados = run_experiments(30)
    plot_metrics(resultados)
