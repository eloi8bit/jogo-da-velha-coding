# Tabela de testes de validação

Como testar: `python jogo_da_velha.py`. Nas jogadas, o par `L,C` significa LINHA e COLUNA digitadas (ex.: `1,1`).

> A coluna "Resultado obtido" deve ser preenchida **depois de rodar cada caso** no programa.

## Testes de validação de entrada

| Nº | Caso | Entrada | Resultado esperado | Resultado obtido |
|----|------|---------|--------------------|------------------|
| 1 | Letra no menu | `a` | Mostra "Entrada inválida! Digite um número de 1 a 4." e pede a opção de novo | Entrada inválida! Digite um número de 1 a 4. |
| 2 | Campo vazio no menu | (apenas Enter) | Mostra "Entrada inválida! Digite um número de 1 a 4." e pede a opção de novo | Entrada inválida! Digite um número de 1 a 4. |
| 3 | Opção de menu inválida | `5` | Mostra "Entrada inválida! Digite um número de 1 a 4." e pede a opção de novo | Entrada inválida! Digite um número de 1 a 4. |
| 4 | Série inválida | opção `1`, depois `4` | Mostra "Entrada inválida! Digite 3 ou 5." e pede a série de novo | Entrada inválida! Digite 3 ou 5. |
| 5 | Número fora do intervalo (zero) | opção `1`, série `3`, linha `0` | Mostra "Entrada inválida! Digite um número de 1 a 3." e pede a linha de novo | Entrada inválida! Digite um número de 1 a 3. |
| 6 | Número fora do intervalo (quatro) | opção `1`, série `3`, linha `4` | Mostra "Entrada inválida! Digite um número de 1 a 3." e pede a linha de novo | Entrada inválida! Digite um número de 1 a 3. |
| 7 | Símbolo inválido | opção `1`, série `3`, linha `1`, coluna `@` | Mostra "Entrada inválida! Digite um número de 1 a 3." e pede a coluna de novo | Entrada inválida! Digite um número de 1 a 3. |
| 8 | Casa ocupada | opção `1`, série `3`; X joga `1,1`; O tenta `1,1` | Mostra "Casa já ocupada! Escolha outra casa." e O joga de novo | Casa já ocupada! Escolha outra casa. |

## Testes de fim de partida e de série

| Nº | Caso | Entrada (jogadas em ordem) | Resultado esperado | Resultado obtido |
|----|------|----------------------------|--------------------|------------------|
| 9 | Vitória por linha | X `1,1` · O `2,1` · X `1,2` · O `2,2` · X `1,3` | "Jogador X venceu!" na rodada 5 | Jogador X venceu! |
| 10 | Vitória por diagonal | X `1,1` · O `1,2` · X `2,2` · O `1,3` · X `3,3` | "Jogador X venceu!" na rodada 5 | Jogador X venceu! |
| 11 | Empate | X `1,1` · O `1,2` · X `1,3` · O `2,2` · X `2,1` · O `2,3` · X `3,2` · O `3,1` · X `3,3` | Tabuleiro cheio sem vencedor: "Deu empate! Ninguém pontua na série." | Deu empate! Ninguém pontua na série. |
| 12 | Série melhor de 3 completa | opção `1`, série `3`; X vence duas partidas seguidas (jogadas do caso 9, duas vezes) | A série termina quando X chega a 2 vitórias e o jogo pergunta se quer jogar novamente a mesma série; no menu, opção `3` mostra X com 2 vitórias | O jogador X é o CAMPEÃO da série (2 x 0)! E menu mostra X com duas vitórias |