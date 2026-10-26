# =====================================================================
# JOGO DA VELHA - CAMPEONATO "MELHOR DE N"
# Disciplina: Coding | UNINASSAU | Prof. M.Sc. Tiago Martins Ribeiro
# Integrantes: Maria Heloísa Mendes, Maria Clara Araújo, Maria Letícia Xavier
# Como executar: python jogo_da_velha.py
# =====================================================================

# [HELOÍSA] MATRIZ DO TABULEIRO
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
] 

# [MARIA CLARA] VARIÁVEIS DA  SESSÃO (PLACAR ACUMULADO E ESTATÍSTICAS).
vitorias_x = 0
vitorias_o = 0
empates = 0
total_partidas = 0
campeonatos_x = 0
campeonatos_O = 0
sequencia_x = 0
sequencia_o = 0
maior_sequencia_x = 0
maior_sequencia_o = 0
inicia_x = True

# [HELOÍSA] EXIBIÇÃO DO TABULEIRO (for aninhado)
print()
print("      1   2   3")
for i in range(3):
    print(f"  {i + 1}  ", end="")
    for j in range(3):
        print(f" {tabuleiro[i][j]} ", end="")
        if j < 2:
            print("|", end="")
    print()
    if i < 2: 
        print("     ---+---+---")
print()