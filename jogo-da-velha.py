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

# [HELOÍSA] LIMPEZA DA MATRIZ
tabuleiro[1][1] = "X"
print(tabuleiro)

for i in range(3):
    for j in range(3):
        tabuleiro[i][j] = " "

print(tabuleiro)

# [HELOÍSA] LEITURA DA JOGADA COM VALIDAÇÃO
linha_valida = False
while linha_valida == False:
    entrada = input("Escolha a LINHA (1 a 3): ")
    for n in range(1, 4):
        if entrada == str(n):
            linha_valida = True
            linha = n - 1 
    if linha_valida == False:
        print("Entrada inválida! Digite um número de 1 a 3.")

print(f"Linha escolhida (índice): {linha}")

# [MARIA CLARA] MENU PRINCIPAL
print("==============================================")
print("     JOGO DA VELHA - CAMPEONATO MELHOR DE N")
print("==============================================")



menu_ativo = True
while menu_ativo == True:
    print()
    print("----------------- MENU -----------------")
    print("1 - Jogar campeonato (melhor de 3 ou melhor de 5)")
    print("2 - Ver regras")
    print("3 - Ver placar")
    print("4 - Sair")

    opcao_valida = False
    while opcao_valida == False:
        entrada = input("Escolha uma opção (1 a 4): ")

        for n in range(1, 5):
            if entrada == str(n):
                opcao_valida = True
                opcao = n

        if opcao_valida == False:
            print("Entrada inválida! Digite um número de 1 a 4.")
        

