import time
import random
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Any

import matplotlib.pyplot as plt

# Importa dos seus módulos base
from eight_queens import initial_board, conflicts, print_board
from hill_climbing import (
    hill_climbing_simple,
    hill_climbing_sideways,
    hill_climbing_random_restart,
)


SCRIPT_DIR = Path(__file__).resolve().parent

PROJECT_ROOT = SCRIPT_DIR.parent

RESULTS_DIR = PROJECT_ROOT / "resultados"


def _plot_and_save(x_data, y_data, title, y_label, filename: Path):
    """Função helper interna para gerar e salvar gráficos de barra."""
    plt.figure()
    plt.bar(x_data, y_data)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(filename)
    plt.show()
    plt.close()


def run_demo() -> List[Tuple[str, int, int, float]]:
    """
    Executa cada algoritmo uma vez com seed fixa (42) para
    demonstração e comparação direta.
    """
    random.seed(42)
    print("--- Execução Única (Seed 42) ---")
    print(f"Tabuleiro Inicial (Conflitos: {conflicts(initial_board())})")
    
    algoritmos = [
        ("Simples", hill_climbing_simple),
        ("Laterais", hill_climbing_sideways),
        ("Reinício", hill_climbing_random_restart),
    ]
    
    results = []

    for nome, func in algoritmos:
        start = time.time()
        result = func()  # Retorna (board, conflitos, iterações, ...)
        end = time.time()

        board_final, conflitos_finais, iteracoes = result[0], result[1], result[2]
        tempo = end - start

        print(f"\nAlgoritmo: {nome}")
        print(f"  Conflitos finais: {conflitos_finais}")
        print(f"  Iterações: {iteracoes}")
        print(f"  Tempo: {tempo:.4f}s")
        if board_final:
            print_board(board_final)
            
        results.append((nome, conflitos_finais, iteracoes, tempo))

    return results


def run_experiments(n_runs: int = 30) -> Dict[str, List[Tuple[int, int, float]]]:
    """
    Executa os algoritmos 'n_runs' vezes com seeds aleatórias
    para coletar estatísticas de desempenho.
    """
    print(f"\n--- Rodando Experimentos ({n_runs} execuções) ---")
    
    # Estrutura para armazenar os resultados (conflitos, iteracoes, tempo)
    results = {
        "Simples": [],
        "Laterais": [],
        "Reinício": [],
    }

    for i in range(n_runs):
        if (i + 1) % 5 == 0:
            print(f"  ...execução {i+1}/{n_runs}")
            
        random.seed() # Nova seed

        # Simples
        start = time.time()
        _, conf, it = hill_climbing_simple()
        results["Simples"].append((conf, it, time.time() - start))

        # Laterais
        start = time.time()
        _, conf, it = hill_climbing_sideways()
        results["Laterais"].append((conf, it, time.time() - start))

        # Reinício Aleatório
        start = time.time()
        _, conf, it, _ = hill_climbing_random_restart()
        results["Reinício"].append((conf, it, time.time() - start))

    print("Experimentos concluídos.")
    return results


def main(n_runs: int):
    
    # Garante que o diretório de resultados exista
    RESULTS_DIR.mkdir(exist_ok=True)

    # 1. Execução Única (Demo)
    demo_results = run_demo()
    
    # Desempacota os resultados da demo usando zip
    # (nome, conflitos, iterações, tempo)
    names, conflicts_list, iters_list, times_list = zip(*demo_results)
    
    print("\nGerando gráficos da execução única...")
    _plot_and_save(names, conflicts_list, "Conflitos Finais (Demo)", "Conflitos", 
                   RESULTS_DIR / "demo_conflitos.png")
                   
    _plot_and_save(names, iters_list, "Iterações (Demo)", "Iterações", 
                   RESULTS_DIR / "demo_iteracoes.png")
                   
    _plot_and_save(names, times_list, "Tempo (Demo)", "Tempo (s)", 
                   RESULTS_DIR / "demo_tempo.png")

    # 2. Experimentos (Múltiplas Execuções)
    exp_results = run_experiments(n_runs)
    labels = list(exp_results.keys())

    # Calcula as métricas usando list comprehensions
    avg_times = [sum(v[2] for v in exp_results[k]) / n_runs for k in labels]
    avg_iters = [sum(v[1] for v in exp_results[k]) / n_runs for k in labels]
    success_rate = [sum(1 for v in exp_results[k] if v[0] == 0) / n_runs * 100 for k in labels]

    print("\nGerando gráficos dos experimentos...")
    _plot_and_save(labels, avg_times, f"Tempo Médio ({n_runs} execuções)", "Tempo (s)", 
                   RESULTS_DIR / "exp_tempo_medio.png")
                   
    _plot_and_save(labels, avg_iters, f"Iterações Médias ({n_runs} execuções)", "Iterações", 
                   RESULTS_DIR / "exp_iteracoes_medias.png")
                   
    _plot_and_save(labels, success_rate, f"Taxa de Sucesso ({n_runs} execuções)", "% Sucesso", 
                   RESULTS_DIR / "exp_taxa_sucesso.png")
                   
    print(f"\nAnálise concluída. Todos os gráficos salvos em '{RESULTS_DIR.resolve()}'")


if __name__ == "__main__":
    # Permite customizar o N de execuções via CLI (ex: python run_analysis.py 50)
    # Senão, usa 30 como padrão.
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    except ValueError:
        print("Argumento inválido. Usando N=30.")
        n = 30
        
    main(n_runs=n)