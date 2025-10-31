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

# ------------------------------------------------------------
# 9. CONFIGURAÇÃO DE DIRETÓRIOS E PASTAS
# ------------------------------------------------------------

# __file__ é o caminho deste script
SCRIPT_DIR = Path(__file__).resolve().parent

# Assume que este script está em uma pasta 'src' ou 'analise'
PROJECT_ROOT = SCRIPT_DIR.parent

# Define o local para salvar os gráficos
RESULTS_DIR = PROJECT_ROOT / "resultados"


# ------------------------------------------------------------
# 10. FUNÇÃO AUXILIAR DE PLOTAGEM
# ------------------------------------------------------------
def _plot_and_save(x_data, y_data, title, y_label, filename: Path):
    """Função helper interna para gerar e salvar gráficos de barra."""
    plt.figure()  # Cria uma nova figura
    plt.bar(x_data, y_data)
    plt.ylabel(y_label)
    plt.title(title)
    
    # Salva o gráfico como imagem na pasta de resultados
    plt.savefig(filename)
    
    plt.show()  # Exibe o gráfico para o usuário
    
    # Fecha a figura para liberar memória
    plt.close()


# ------------------------------------------------------------
# 11. EXECUÇÃO DE DEMONSTRAÇÃO (SEED FIXA)
# ------------------------------------------------------------
def run_demo() -> List[Tuple[str, int, int, float]]:
    """
    Executa cada algoritmo uma vez com seed fixa (42) para
    demonstração e comparação direta.
    """
    # Define uma 'seed' (semente) fixa para garantir que os resultados
    # desta função sejam sempre os mesmos (reprodutibilidade)
    random.seed(42)
    
    print("--- Execução Única (Seed 42) ---")
    
    # Gera um tabuleiro inicial fixo para todos os algoritmos
    board_inicial_demo = initial_board()
    print(f"Tabuleiro Inicial (Conflitos: {conflicts(board_inicial_demo)})")
    
    # Lista de tuplas contendo (Nome do Algoritmo, Função a ser chamada)
    algoritmos = [
        ("Simples", hill_climbing_simple),
        ("Laterais", hill_climbing_sideways),
        ("Reinício", hill_climbing_random_restart),
    ]
    
    results = []

    for nome, func in algoritmos:
        start = time.time()
        
        # Chama a função do algoritmo (ex: hill_climbing_simple())
        # Passa o 'board_inicial_demo' para garantir que todos comecem igual
        result = func(board=board_inicial_demo.copy()) 
        
        end = time.time()

        # Desempacota a tupla de retorno padrão: (board, conflitos, iterações, ...)
        # O [0], [1], [2] garante que pegamos os 3 primeiros itens,
        # ignorando o 4º item (restarts) do 'random_restart'
        board_final, conflitos_finais, iteracoes = result[0], result[1], result[2]
        tempo = end - start

        print(f"\nAlgoritmo: {nome}")
        print(f"   Conflitos finais: {conflitos_finais}")
        print(f"   Iterações: {iteracoes}")
        print(f"   Tempo: {tempo:.4f}s")
        if board_final:
            print_board(board_final)
            
        # Armazena os dados para os gráficos da demo
        results.append((nome, conflitos_finais, iteracoes, tempo))

    return results

# ------------------------------------------------------------
# 12. EXECUÇÃO DE EXPERIMENTOS (MÚLTIPLAS RODADAS)
# ------------------------------------------------------------
def run_experiments(n_runs: int = 30) -> Dict[str, List[Tuple[int, int, float]]]:
    """
    Executa os algoritmos 'n_runs' vezes com seeds aleatórias
    para coletar estatísticas de desempenho.
    """
    print(f"\n--- Rodando Experimentos ({n_runs} execuções) ---")
    
    # Dicionário para agrupar resultados por algoritmo
    # Cada lista armazenará tuplas de (conflitos, iteracoes, tempo)
    results = {
        "Simples": [],
        "Laterais": [],
        "Reinício": [],
    }

    for i in range(n_runs):
        # Imprime uma mensagem de progresso a cada 5 execuções
        if (i + 1) % 5 == 0:
            print(f"   ...execução {i+1}/{n_runs}")
            
        # Reseta a seed (para None), fazendo com que o 'random'
        # use uma seed nova (baseada no tempo) a cada iteração.
        # Isso garante que cada 'run' seja diferente.
        random.seed() 

        # --- Simples ---
        start = time.time()
        # Não passamos 'board', então ele gera um aleatório
        _, conf, it = hill_climbing_simple() 
        results["Simples"].append((conf, it, time.time() - start))

        # --- Laterais ---
        start = time.time()
        _, conf, it = hill_climbing_sideways()
        results["Laterais"].append((conf, it, time.time() - start))

        # --- Reinício Aleatório ---
        start = time.time()
        # O retorno é (board, conf, it, restarts) - pegamos os 3 primeiros
        _, conf, it, _ = hill_climbing_random_restart() 
        results["Reinício"].append((conf, it, time.time() - start))

    print("Experimentos concluídos.")
    return results

# ------------------------------------------------------------
# 13. FUNÇÃO PRINCIPAL (ORQUESTRADOR)
# ------------------------------------------------------------
def main(n_runs: int):
    
    # Garante que a pasta 'resultados' exista antes de salvar
    RESULTS_DIR.mkdir(exist_ok=True)

    # --- 1. Execução Única (Demo) ---
    demo_results = run_demo()
    
    # 'zip(*...)' é um truque para "desempacotar" a lista de tuplas.
    # Transforma: [('A', 1, 0.1), ('B', 0, 0.2)]
    # Em:         [('A', 'B'), (1, 0), (0.1, 0.2)]
    names, conflicts_list, iters_list, times_list = zip(*demo_results)
    
    print("\nGerando gráficos da execução única...")
    _plot_and_save(names, conflicts_list, "Conflitos Finais (Demo)", "Conflitos", 
                   RESULTS_DIR / "demo_conflitos.png")
                   
    _plot_and_save(names, iters_list, "Iterações (Demo)", "Iterações", 
                   RESULTS_DIR / "demo_iteracoes.png")
                   
    _plot_and_save(names, times_list, "Tempo (Demo)", "Tempo (s)", 
                   RESULTS_DIR / "demo_tempo.png")

    # --- 2. Experimentos (Múltiplas Execuções) ---
    exp_results = run_experiments(n_runs)
    labels = list(exp_results.keys()) # ['Simples', 'Laterais', 'Reinício']

    # Calcula as métricas usando 'list comprehensions'
    
    # Para cada algoritmo 'k' em 'labels', calcula a média do tempo
    # v[2] é o tempo (conflitos=0, iterações=1, tempo=2)
    avg_times = [sum(v[2] for v in exp_results[k]) / n_runs for k in labels]
    
    # v[1] são as iterações
    avg_iters = [sum(v[1] for v in exp_results[k]) / n_runs for k in labels]
    
    # v[0] são os conflitos. 'sum(1 ... if v[0] == 0)' conta quantos sucessos
    success_rate = [sum(1 for v in exp_results[k] if v[0] == 0) / n_runs * 100 for k in labels]

    print("\nGerando gráficos dos experimentos...")
    _plot_and_save(labels, avg_times, f"Tempo Médio ({n_runs} execuções)", "Tempo (s)", 
                   RESULTS_DIR / "exp_tempo_medio.png")
                   
    _plot_and_save(labels, avg_iters, f"Iterações Médias ({n_runs} execuções)", "Iterações", 
                   RESULTS_DIR / "exp_iteracoes_medias.png")
                   
    _plot_and_save(labels, success_rate, f"Taxa de Sucesso ({n_runs} execuções)", "% Sucesso", 
                   RESULTS_DIR / "exp_taxa_sucesso.png")
                   
    print(f"\nAnálise concluída. Todos os gráficos salvos em '{RESULTS_DIR.resolve()}'")


# ------------------------------------------------------------
# 14. PONTO DE ENTRADA DO SCRIPT
# ------------------------------------------------------------
if __name__ == "__main__":
    # Esta parte só executa se o script for chamado diretamente
    # (ex: python run_analysis.py)
    
    # Permite customizar o N de execuções via CLI (ex: python run_analysis.py 50)
    # Senão, usa 30 como padrão.
    try:
        # Pega o primeiro argumento da linha de comando (sys.argv[0] é o nome do script)
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    except ValueError:
        # Se o usuário digitar algo que não é um número (ex: python run_analysis.py "abc")
        print("Argumento inválido. Usando N=30.")
        n = 30
        
    # Inicia o programa principal
    main(n_runs=n)