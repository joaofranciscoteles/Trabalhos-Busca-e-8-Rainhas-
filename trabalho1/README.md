# 🔍 Comparador de Algoritmos de Busca em Labirintos

[![Instituição][cefet-badge]][cefet-url]
[![IDE][vscode-badge]][vscode-url]
[![Linguagem][python-badge]][python-url]

Este repositório contém o código-fonte do **Trabalho 1 da disciplina de Inteligência Artificial**, ministrada pelo **prof. Tiago Alves de Oliveira** no **CEFET-MG – Campus V**.

O objetivo do projeto é **implementar e comparar o desempenho** de diferentes **algoritmos de busca** aplicados à resolução de **labirintos**:

- **Busca em Profundidade (DFS)**  
- **Busca em Largura (BFS)**  
- **Busca Gulosa (GBFS)**  
- **Busca A\*** (*A-star*)

O projeto suporta duas heurísticas para as buscas informadas: **Manhattan** e **Euclidiana**.

---

## 🧠 Visão geral do funcionamento

O script principal do repositório é o arquivo `main.py` (localizado na pasta `src/`). Ao executar `main.py` ele:

1. Lê **um arquivo de labirinto por vez** (arquivo `.txt`) a partir da pasta `data/`;
2. Converte o labirinto lido para uma representação interna (`matriz`) e identifica `start` e `goal`;
3. Executa os quatro algoritmos de busca (BFS, DFS, GBFS e A*) sobre esse labirinto;
4. Mede e coleta métricas para cada execução:
   - Tempo de execução;
   - Número de nós expandidos;
   - Pico de memória (definido como `len(fronteira) + len(visitados)` em seu ponto máximo);
   - Custo do caminho encontrado (número de passos);
5. Gera um sumário no terminal e salva **gráficos comparativos** no diretório `resultados/` (subpastas como `geral/` e `comparativo_heuristicas/`).

> Observação: por design, `main.py` roda sobre um arquivo de labirinto por execução — se você quiser processar múltiplos labirintos em lote, basta chamar `main.py` várias vezes em um script externo ou adicionar um loop que itere sobre `data/`.

---

## 📥 Clone do Projeto

Para começar, clone este repositório para a sua máquina local usando o seguinte comando no seu terminal:

```bash
#usando HTTPS
git clone https://github.com/joaofranciscoteles/Trabalhos-Busca-e-8-Rainhas-.git

#usando SSH
git clone git@github.com:joaofranciscoteles/Trabalhos-Busca-e-8-Rainhas-.git
```

---

## 🚀 Requisitos

* **Python 3.10** (ou superior)
* **Matplotlib** (única dependência externa, usada para gerar os gráficos)

---

## ⚙️ Instalação das Dependências

###  Instalação Manual (via Pip)

Você deve instalar a biblioteca manualmente usando o `pip` (gerenciador de pacotes do Python):

```bash
pip install -r requirements.txt
```

---

## 📂 Detalhes do Projeto

### Estrutura de Pastas

Seus arquivos de labirinto devem estar dentro de uma pasta chamada `data/`. O script principal `run_search.py` foi programado para procurar automaticamente por qualquer arquivo que comece com `labirinto` (ex: `labirinto.txt`, `labirinto_grande.txt`, etc.) dentro dessa pasta.

``` Markdown
Trabalho1/
├── data/
│   ├── labirinto.txt
│   ├── labirinto1.txt
|   └── labirinto3.txt
│
├── src/
│   ├── main.py
│   ├── astar.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── gbfs.py
│   └── maze_utils.py
│
├── resultados/
│   ├── comparativo_heuristicas/
|   |    ├── custo_caminho.png
|   |    ├── memoria_maxima.png
|   |    ├── nos_expandidos.png
|   |    ├── tempo_execucao.png
│   ├── geral/
|   |    ├── custo_caminho.png
|   |    ├── memoria_maxima.png
|   |    ├── nos_expandidos.png
|   |    ├── tempo_execucao.png
|
├── .gitignore
├── trabalho1_<BrunoPrado,JoãoFrancisco>.pdf
├── README.md 
└── requirements.txt


```

### Formato do labirinto

Os arquivos `.txt` devem seguir este formato: 

- `#`: Parede
- `.`: Caminho livre
- `S`: Ponto de partida (Start)
- `G`: Ponto de chegada (Goal)

## ▶️ Execução

Com as dependências instaladas e os labirintos na pasta `data/`, basta executar o script principal a partir da pasta `src/`.

```Bash

# Em Linux/macOS
python3 main.py

# Em Windows
python main.py
# ou
py main.py
```

## 💻 Máquinas de Teste

Para testagem do projeto, foram utilizadas 2 máquinas que rodaram o cógido em sistema operacional Linux (Ubuntu).

| Máquina | Processador            | Memória RAM | Sistema Operacional |
|------------------|------------------------|-------------|---------------------|
| ACER NITRO 5 |Intel(R) Core(TM) i5-12450H    | 16 GB       | Windows 10     |
| Acer Aspire A515-54    | Intel64 Family 6 Model 142 Stepping 12 GenuineIntel ~1609 MHz       | 8 GB        | Windows 11       |


---

## 👨‍💻 Autores

Trabalho desenvolvido em dupla pelos seguintes alunos:

<div align="center">
    
**Bruno Prado Dos Santos**
<br>
*Estudante de Engenharia de Computação @ CEFET-MG*
<br><br>
[![Gmail][gmail-badge]][gmail-bruno]


<br><br>

**João Francisco Teles da Silva**
<br>
*Estudante de Engenharia de Computação @ CEFET-MG*
<br><br>
[![Gmail][gmail-badge]][gmail-joao]


</div>

[gmail-badge]: https://img.shields.io/badge/-Gmail-D14836?style=for-the-badge&logo=Gmail&logoColor=white


[gmail-bruno]: mailto:bruno.santos@aluno.cefetmg.br


[gmail-joao]: mailto:joaoteles0505@gmail.com


[cefet-badge]: https://img.shields.io/badge/CEFET--MG-Campus%20V-blue?logo=academia
[cefet-url]: https://www.cefetmg.br/

[vscode-badge]: https://img.shields.io/badge/VSCode-1.86-blue?logo=visualstudiocode
[vscode-url]: https://code.visualstudio.com/

[python-badge]: https://img.shields.io/badge/Python-3.10-yellow?logo=python
[python-url]: https://www.python.org/
