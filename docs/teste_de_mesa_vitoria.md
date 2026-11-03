# TESTE DE MESA — VERIFICAÇÃO DE VITÓRIA

**Projeto:** Jogo da Velha — Campeonato Melhor de N  
**Responsável:** Maria Letícia  

## 1. Objetivo

Verificar como o programa identifica uma vitória quando o jogador X completa a primeira coluna do tabuleiro.

## 2. Situação do teste

O jogador X ocupa as três casas da primeira coluna:

- `tabuleiro[0][0]`
- `tabuleiro[1][0]`
- `tabuleiro[2][0]`

## 3. Tabela do teste de mesa

| Iteração | i | j | Casa testada | Símbolo |
|---|---:|---:|---|---|
| 1 | 0 | 0 | tabuleiro[0][0] | X |
| 2 | 1 | 0 | tabuleiro[1][0] | X |
| 3 | 2 | 0 | tabuleiro[2][0] | X |

## 4. Verificação da vitória

O programa verifica se as três posições da primeira coluna possuem o símbolo do jogador atual.

Como todas as posições possuem X, a condição é verdadeira.

Assim:
- `venceu = True`
- `partida_terminou = True`

## 5. Resultado esperado

**Jogador X venceu!**

A partida é encerrada após a identificação da vitória.