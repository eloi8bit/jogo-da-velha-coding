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

for i in range(3):
    for j in range(3):
        tabuleiro[i][j] = " "

# [HELOÍSA] LEITURA DA JOGADA COM VALIDAÇÃO
simbolo = "X"
tabuleiro[1][1] = "O"

jogada_valida = False
while jogada_valida == False:
    
    linha_valida = False
    while linha_valida == False:
        entrada = input("Escolha a LINHA (1 a 3): ")
        for n in range(1, 4):
            if entrada == str(n):
                linha_valida = True
                linha = n - 1 
        if linha_valida == False:
            print("Entrada inválida! Digite um número de 1 a 3.")

    coluna_valida = False
    while coluna_valida == False:
        entrada = input("Escolha a COLUNA (1 a 3): ")
        for n in range(1, 4):
            if entrada == str(n):
                coluna_valida = True
                coluna = n - 1
        if coluna_valida == False:
            print("Entrada inválida! Digite um número de 1 a 3.")

    if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2 and tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = simbolo
        jogada_valida = True
    else:
        print("Casa já ocupada! Escolha outra casa.")
        
print(tabuleiro)     
           
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
        


    if opcao == 1:
        # [MARIA CLARA] - ESCOLHA DA SÉRIE
        serie_valida = False

        while serie_valida == False:
            entrada = input("Escolha a série (3 = melhor de 3 | 5 = melhor de 5): ")

            if entrada == "3" or entrada == "5":
                melhor_de = int(entrada)
                serie_valida = True
            else:
                print("Entrada inválida! Digite 3 ou 5.")

        vitorias_necessarias = int(melhor_de / 2) + 1

        print(f"Série melhor de {melhor_de}: vence quem fizer {vitorias_necessarias} vitórias primeiro.")

        # [MARIA LETÍCIA] - LAÇO DA PARTIDA
        # Controle de turno e contador de rodadas

        for i in range(3):
            for j in range(3):
                tabuleiro[i][j] = " "

        rodadas = 0
        partida_terminou = False
        venceu = False
        vez_de_x = True

        while partida_terminou == False:

            # [MARIA LETÍCIA] EXIBIÇÃO DO TABULEIRO
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

            # [MARIA LETÍCIA] INDICADOR DO JOGADOR
            if vez_de_x == True:
                simbolo = "X"
            else:
                simbolo = "O"

            print(f"Rodada {rodadas + 1} - Vez do jogador {simbolo}")

            # [MARIA LETÍCIA] LEITURA E VALIDAÇÃO DA JOGADA
            jogada_valida = False

            while jogada_valida == False:
                linha_valida = False

                while linha_valida == False:
                    entrada = input("Escolha a LINHA (1 a 3): ")

                    for n in range(1, 4):
                        if entrada == str(n):
                            linha = n - 1
                            linha_valida = True

                    if linha_valida == False:
                        print("Entrada inválida! Digite um número de 1 a 3.")

                coluna_valida = False

                while coluna_valida == False:
                    entrada = input("Escolha a COLUNA (1 a 3): ")

                    for n in range(1, 4):
                        if entrada == str(n):
                            coluna = n - 1
                            coluna_valida = True

                    if coluna_valida == False:
                        print("Entrada inválida! Digite um número de 1 a 3.")

                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = simbolo
                    jogada_valida = True
                else:
                    print("Casa já ocupada! Escolha outra casa.")

            # [MARIA LETÍCIA] CONTADOR E ALTERNÂNCIA
            rodadas += 1
            vez_de_x = not vez_de_x

            # Parada temporária após 9 rodadas
            if rodadas == 9:
                partida_terminou = True

        print("Partida encerrada após 9 rodadas.")


    elif opcao == 2:
        # [MARIA CLARA] - REGRAS DO JOGO
        print()
        print("-------------------- REGRAS --------------------")
        print("1. O tabuleiro tem 3 linhas e 3 colunas.")
        print("2. Dois jogadores se alternam: X e O.")
        print("3. Informe a linha e a coluna de uma casa vazia.")
        print("4. Vence quem completar uma linha, coluna ou diagonal.")
        print("5. Se o tabuleiro encher sem vencedor, ocorre empate.")
        print("6. Melhor de 3: vence quem ganhar 2 partidas.")
        print("7. Melhor de 5: vence quem ganhar 3 partidas.")
        print("------------------------------------------------")

    elif opcao == 3:
        # [MARIA CLARA] EXIBIÇÃO DO PLACAR
        print(f"Partidas jogadas: {total_partidas}")
        print(f"Vitórias de X: {vitorias_x}")
        print(f"Vitórias de O: {vitorias_o}")
        print(f"Empates: {empates}")

    elif opcao == 4:
        print("Obrigado por jogar!")
        menu_ativo = False
