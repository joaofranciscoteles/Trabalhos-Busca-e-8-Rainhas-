import time
import random
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Any

# Importa a biblioteca 'statistics' para calcular média e desvio padrão
import statistics 

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
def _plot_and_save(x_data, y_data, title, y_label, filename: Path, y_error=None):
    
    plt.figure()  # Cria uma nova figura
    
    # Adiciona 'yerr' e 'capsize' se 'y_error' for fornecido
    plt.bar(x_data, y_data, yerr=y_error, capsize=5) 
    
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
    
    # (O código original desta função está 100% correto e não precisa
    # de alterações, pois a lógica de captura de 3 itens ainda funciona)
    
    random.seed(42)
    print("--- Execução Única (Seed 42) ---")
    board_inicial_demo = initial_board()
    print(f"Tabuleiro Inicial (Conflitos: {conflicts(board_inicial_demo)})")
    
    algoritmos = [
        ("Simples", hill_climbing_simple),
        ("Laterais", hill_climbing_sideways),
        ("Reinício", hill_climbing_random_restart),
    ]
    
    results = []

    for nome, func in algoritmos:
        start = time.time()
        
        # O 'board_inicial_demo.copy()' é importante aqui
        if nome == "Reinício":
            # O 'random_restart' não aceita um 'board' inicial,
            # pois sua lógica é justamente criar novos.
            # Para a demo, forçamos o primeiro 'run' a ser com o board.
            # (Assumindo que o primeiro 'simple_climb' usará o board)
            # Para simplificar e não alterar a lógica, vamos chamá-lo
            # da forma padrão (ele vai ignorar o board_inicial_demo).
             result = func() 
        else:
             result = func(board=board_inicial_demo.copy())
        
        end = time.time()

        # Desempacota a tupla de retorno
        # (board, conflitos, iterações)
        # Isso funciona pois intencionalmente ignora o 4º item (restarts)
        # que 'hill_climbing_random_restart' retorna.
        board_final, conflitos_finais, iteracoes = result[0], result[1], result[2]
        tempo = end - start

        print(f"\nAlgoritmo: {nome}")
        print(f"    Conflitos finais: {conflitos_finais}")
        print(f"    Iterações: {iteracoes}")
        print(f"    Tempo: {tempo:.4f}s")
        if board_final and conflitos_finais == 0:
            print_board(board_final)
            
        results.append((nome, conflitos_finais, iteracoes, tempo))

    return results

# ------------------------------------------------------------
# 12. EXECUÇÃO DE EXPERIMENTOS (MÚLTIPLAS RODADAS)
# ------------------------------------------------------------
def run_experiments(n_runs: int = 30) -> Dict[str, List[Tuple[int, int, float, int]]]:
    
    print(f"\n--- Rodando Experimentos ({n_runs} execuções) ---")
    
    results = {
        "Simples": [],
        "Laterais": [],
        "Reinício": [],
    }

    for i in range(n_runs):
        if (i + 1) % 5 == 0:
            print(f"    ...execução {i+1}/{n_runs}")
            
        random.seed() 

        # --- Simples ---
        start = time.time()
        _, conf, it = hill_climbing_simple() 
        #  Adiciona '0' para restarts
        results["Simples"].append((conf, it, time.time() - start, 0))

        # --- Laterais ---
        start = time.time()
        _, conf, it = hill_climbing_sideways()
        #  Adiciona '0' para restarts
        results["Laterais"].append((conf, it, time.time() - start, 0))

        # --- Reinício Aleatório ---
        start = time.time()
        
        #  Captura o 4º valor (restarts)
        _, conf, it, restarts = hill_climbing_random_restart() 
        
        #  Salva o valor 'restarts'
        results["Reinício"].append((conf, it, time.time() - start, restarts))

    print("Experimentos concluídos.")
    return results

# ------------------------------------------------------------
# 13. FUNÇÃO PRINCIPAL (ORQUESTRADOR)
# ------------------------------------------------------------
def main(n_runs: int):
    
    RESULTS_DIR.mkdir(exist_ok=True)

    # --- 1. Execução Única (Demo) ---
    
    demo_results = run_demo()
    
    # O zip vai criar 4 listas, mas só usamos as 3 primeiras
    # (nome, conflitos, iterações, tempo)
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

    #  Extrai listas de dados brutos para estatística
    # (v[0]=conflitos, v[1]=iterações, v[2]=tempo, v[3]=restarts)
    
    times_data = {k: [v[2] for v in exp_results[k]] for k in labels}
    iters_data = {k: [v[1] for v in exp_results[k]] for k in labels}
    
    # Apenas 'Reinício' terá valores > 0 aqui
    restarts_data = [v[3] for v in exp_results["Reinício"]] 

    #  Calcula médias E desvio padrão
    avg_times = [statistics.mean(times_data[k]) for k in labels]
    std_times = [statistics.stdev(times_data[k]) for k in labels]
    
    avg_iters = [statistics.mean(iters_data[k]) for k in labels]
    std_iters = [statistics.stdev(iters_data[k]) for k in labels]
    
    
    success_rate = [sum(1 for v in exp_results[k] if v[0] == 0) / n_runs * 100 for k in labels]

    #  Calcula estatísticas de reinício
    avg_restarts = statistics.mean(restarts_data)
    std_restarts = statistics.stdev(restarts_data)

    #  Imprime os resultados estatísticos no console
    print("\n--- Resultados Estatísticos (Média ± Desvio Padrão) ---")
    print(f"Baseado em {n_runs} execuções.\n")
    
    for i, k in enumerate(labels):
        print(f"Algoritmo: {k}")
        print(f"  Taxa de Sucesso: {success_rate[i]:.1f}%")
        print(f"  Tempo Médio:     {avg_times[i]:.4f} ± {std_times[i]:.4f} s")
        print(f"  Iterações Médias: {avg_iters[i]:.2f} ± {std_iters[i]:.2f}")
        if k == "Reinício":
            print(f"  Reinícios Médios: {avg_restarts:.2f} ± {std_restarts:.2f}")
        print("-" * 30)


    print("\nGerando gráficos dos experimentos...")
    
    
    _plot_and_save(labels, avg_times, f"Tempo Médio ({n_runs} execuções)", "Tempo (s)", 
                   RESULTS_DIR / "exp_tempo_medio.png", y_error=std_times)
                   
    
    _plot_and_save(labels, avg_iters, f"Iterações Médias ({n_runs} execuções)", "Iterações", 
                   RESULTS_DIR / "exp_iteracoes_medias.png", y_error=std_iters)
                   
    # (Gráfico de sucesso não precisa de barra de erro)
    _plot_and_save(labels, success_rate, f"Taxa de Sucesso ({n_runs} execuções)", "% Sucesso", 
                   RESULTS_DIR / "exp_taxa_sucesso.png")
                   
    # Gráfico específico para a média de reinícios
    _plot_and_save(
        ["Reinício Aleatório"],  # Lista com um único item
        [avg_restarts],          # Lista com um único item
        f"Média de Reinícios ({n_runs} execuções)", 
        "Nº de Reinícios", 
        RESULTS_DIR / "exp_restarts_medio.png",
        y_error=[std_restarts] # Lista com um único item
    )
    
    print(f"\nAnálise concluída. Todos os gráficos salvos em '{RESULTS_DIR.resolve()}'")


# ------------------------------------------------------------
# 14. PONTO DE ENTRADA DO SCRIPT
# ------------------------------------------------------------
if __name__ == "__main__":
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    except ValueError:
        print("Argumento inválido. Usando N=30.")
        n = 30
        
    main(n_runs=n)