# Teste de mesa - Exibição do tabuleiro

Trecho analisado (laço aninhado da exibição, em `jogo_da_velha.py`):

```python
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
```

## Estado do tabuleiro usado no teste

Para o teste, considera-se o tabuleiro abaixo (`_` representa a casa vazia `" "`):

|       | col 0 | col 1 | col 2 |
|-------|-------|-------|-------|
| lin 0 | X     | O     | X     |
| lin 1 | _     | X     | O     |
| lin 2 | O     | _     | X     |

## Como o laço funciona

- O `for i` (externo) percorre as **linhas** do tabuleiro: `i = 0, 1, 2`.
- O `for j` (interno) percorre as **colunas** de cada linha: `j = 0, 1, 2`.
- Para cada valor de `i`, o laço interno executa **3 vezes**, totalizando **3 x 3 = 9 passos**.
- O `print()` sem argumentos, após o laço interno, pula para a próxima linha.
- O separador `---+---+---` só é impresso se `i < 2`, ou seja, não aparece depois da última linha.
- O `|` só é impresso se `j < 2`, ou seja, não aparece depois da última coluna.

## Tabela do teste de mesa

| Passo | i | j | Casa consultada   | Símbolo exibido | Observação                                      |
|-------|---|---|-------------------|-----------------|-------------------------------------------------|
| 1     | 0 | 0 | `tabuleiro[0][0]` | `X`             | `j < 2`, imprime `\|`                           |
| 2     | 0 | 1 | `tabuleiro[0][1]` | `O`             | `j < 2`, imprime `\|`                           |
| 3     | 0 | 2 | `tabuleiro[0][2]` | `X`             | `j = 2`, sem `\|`; fim da linha (`print()`); `i < 2`, imprime separador |
| 4     | 1 | 0 | `tabuleiro[1][0]` | (vazio)         | `j < 2`, imprime `\|`                           |
| 5     | 1 | 1 | `tabuleiro[1][1]` | `X`             | `j < 2`, imprime `\|`                           |
| 6     | 1 | 2 | `tabuleiro[1][2]` | `O`             | `j = 2`, sem `\|`; fim da linha (`print()`); `i < 2`, imprime separador |
| 7     | 2 | 0 | `tabuleiro[2][0]` | `O`             | `j < 2`, imprime `\|`                           |
| 8     | 2 | 1 | `tabuleiro[2][1]` | (vazio)         | `j < 2`, imprime `\|`                           |
| 9     | 2 | 2 | `tabuleiro[2][2]` | `X`             | `j = 2`, sem `\|`; fim da linha (`print()`); `i = 2`, sem separador |

## Saída final na tela

```
      1   2   3
  1   X | O | X
     ---+---+---
  2     | X | O
     ---+---+---
  3   O |   | X
```