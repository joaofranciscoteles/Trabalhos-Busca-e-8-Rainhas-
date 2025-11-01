# ♟️ Resolução do Problema das 8 Rainhas com Hill Climbing

[![Instituição][cefet-badge]][cefet-url]
[![IDE][vscode-badge]][vscode-url]
[![Linguagem][python-badge]][python-url]

Este repositório contém o código-fonte do **Trabalho 2 da disciplina de Inteligência Artificial**, ministrada pelo **prof. Tiago Alves de Oliveira** no **CEFET-MG – Campus V**.

O objetivo do projeto é **resolver o problema das 8 Rainhas** utilizando o algoritmo de **Subida de Encosta (Hill Climbing)**, comparando três variações principais:

- **Hill Climbing Simples**  
- **Hill Climbing com Movimentos Laterais (limitados)**  
- **Hill Climbing com Reinícios Aleatórios (Random-Restart)**  

---

## 🧠 Visão Geral do Funcionamento

O script principal do repositório é o arquivo `run_analysis.py` (localizado na pasta `src/`).  
Ao executá-lo, o programa:

1. Gera automaticamente um **tabuleiro inicial aleatório** representando a posição das 8 rainhas;  
2. Avalia o número de **conflitos (ataques entre rainhas)**;  
3. Executa as três variações do algoritmo Hill Climbing;  
4. Mede e coleta métricas estatísticas (baseado em N=30 execuções):
   - Taxa de sucesso (% de execuções que encontraram solução);
   - Tempo médio de execução (com desvio padrão);
   - Número médio de iterações (com desvio padrão);
   - Número médio de reinícios (para a variação Random-Restart).
5. Exibe os resultados estatísticos no terminal (formatado como Média ± Desvio Padrão);
6. Gera, salva e exibe **gráficos comparativos** das métricas, incluindo barras de erro para o desvio padrão.

---

## 📥 Clone do Projeto

Para começar, clone este repositório para sua máquina local:

```bash
# usando HTTPS
git clone https://github.com/joaofranciscoteles/Trabalhos-Busca-e-8-Rainhas-.git

# usando SSH
git clone git@github.com:joaofranciscoteles/Trabalhos-Busca-e-8-Rainhas-.git
```

---

## 🚀 Requisitos

- **Python 3.10** (ou superior)  
- **Matplotlib** (utilizada para gerar os gráficos)

---

## ⚙️ Instalação das Dependências

Instale manualmente com o `pip`:

```bash
pip install -r requirements.txt
```

---

## 📂 Detalhes do Projeto

### Estrutura de Pastas

```markdown
Trabalho2/
├── src/
│   ├── eight_queens.py     
│   ├── hill_climbing.py    
│   └── run_analysis.py      
│
├── resultados/
│   ├── demo_conflitos.png
│   ├── demo_iteracoes.png
│   ├── demo_tempo.png
│   ├── exp_iteracoes_medias.png
│   ├── exp_taxa_sucesso.png
│   ├── exp_tempo_medio.png
│   └── exp_restarts_medio.png      
│
├── .gitignore
├── README.md
├── trabalho2__BrunoPrado_JoãoFrancisco_.pdf
└── requirements.txt
```

### Representação do Tabuleiro

O estado é representado por uma lista de tamanho 8:  
`board[coluna] = linha`, onde cada elemento indica a posição da rainha em sua coluna.  

Exemplo:  
```python
board = [0, 4, 7, 5, 2, 6, 1, 3]
```
significa que a rainha da coluna 0 está na linha 0, a da coluna 1 na linha 4 e assim por diante.

---

## ▶️ Execução

Com as dependências instaladas, execute o script principal a partir da pasta `src/`:

```bash
# Linux/macOS
python3 run_analysis.py

# Windows
python run_analysis.py
# ou
py run_analysis.py
```

Durante a execução, o programa:
- Mostra os resultados da execução única (Demo com seed=42);
- Executa os 30 experimentos (com barra de progresso);
- Exibe uma tabela de **Resultados Estatísticos** no console, contendo (Média ± Desvio Padrão) para Tempo, Iterações e Reinícios.
- Gera, salva e exibe os gráficos de barra com os resultados estatísticos.

---

## 📈 Métricas e Gráficos

Ao final da execução, são exibidos os gráficos das métricas (separados entre Demo e Experimentos):

- **Resultados da Demo (N=1, seed=42)**:
    - Conflitos finais por variação
    - Iterações por variação
    - Tempo de execução
- **Resultados Estatísticos (N=30)**:
    - **Taxa de Sucesso (%)**: Compara a eficácia (quantas vezes achou a solução).
    - **Tempo Médio de Execução (s)**: Compara o custo computacional (inclui barras de erro para o desvio padrão).
    - **Iterações Médias**: Compara o número de passos da busca (inclui barras de erro para o desvio padrão).
    - **Média de Reinícios**: Mostra o custo médio (com desvio padrão) pago pela variação "Reinício Aleatório" para atingir 100% de sucesso.
---

## 💻 Máquinas de Teste

Para testagem do projeto, foram utilizadas 2 máquinas que rodaram o cógido em sistema operacional Linux (Ubuntu).

| Máquina | Processador            | Memória RAM | Sistema Operacional |
|------------------|------------------------|-------------|---------------------|
| ACER NITRO 5 |Intel(R) Core(TM) i5-12450H    | 16 GB       | Windows 10     |
| Acer Aspire A515-54    | Intel(R) Core(TM) i5-10210U    | 8 GB        | Windows 11       |

---

## 👨‍💻 Autores

Trabalho desenvolvido em dupla pelos seguintes alunos:

<div align="center">
    
**Bruno Prado Dos Santos**  
*Estudante de Engenharia de Computação @ CEFET-MG*  
<br><br>
[![Gmail][gmail-badge]][gmail-bruno]

<br><br>

**João Francisco Teles da Silva**  
*Estudante de Engenharia de Computação @ CEFET-MG*  
<br><br>
[![Gmail][gmail-badge]][gmail-joao]

</div>

---


[gmail-badge]: https://img.shields.io/badge/-Gmail-D14836?style=for-the-badge&logo=Gmail&logoColor=white  
[gmail-bruno]: mailto:bruno.santos@aluno.cefetmg.br  
[gmail-joao]: mailto:joaoteles0505@gmail.com  
[cefet-badge]: https://img.shields.io/badge/CEFET--MG-Campus%20V-blue?logo=academia  
[cefet-url]: https://www.cefetmg.br/  
[vscode-badge]: https://img.shields.io/badge/VSCode-1.86-blue?logo=visualstudiocode  
[vscode-url]: https://code.visualstudio.com/  
[python-badge]: https://img.shields.io/badge/Python-3.10-yellow?logo=python  
[python-url]: https://www.python.org/
