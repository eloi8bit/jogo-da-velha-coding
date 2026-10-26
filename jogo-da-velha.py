# =====================================================================
# JOGO DA VELHA - CAMPEONATO "MELHOR DE N"
# Disciplina: Coding | UNINASSAU | Prof. M.Sc. Tiago Martins Ribeiro
# Integrantes: Maria Heloísa Mendes, Maria Clara Araújo, Maria Letícia Xavier
# Como executar: python jogo_da_velha.py
# =====================================================================

# [BLOCO 1A - Heloísa] MATRIZ DO TABULEIRO
# Declarada por extenso: 3 listas (linhas) com 3 posições (colunas).
# Acesso: tabuleiro[i][j] -> i = linha, j = coluna.
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print(tabuleiro) 

# [BLOCO 1B - MARIA CLARA] VARIÁVEIS DA  SESSÃO (PLACAR ACUMULADO E ESTATÍSTICAS).
vitorias_x = 0           #vitorias do jogador X.
vitorias_o = 0           #vitorias do jogador O.
empates = 0
total_partidas = 0
campeonatos_x = 0        #serie de campeonatos vencidos por X.
campeonatos_O = 0        #serie de campeonatos vencidos por O.
sequencia_x = 0          #vitorias consecutivas de X.
sequencia_o = 0          #vitorias consecutivas de O.
maior_sequencia_x = 0
maior_sequencia_o = 0
inicia_x = True          #indica que "X" começa.

