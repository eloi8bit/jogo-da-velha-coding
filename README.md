# Jogo da Velha - Campeonato "Melhor de N"

## Como executar

1. **Instalar o Python:**  
   Para executar o jogo, é necessário ter o Python instalado no computador. Caso ainda não tenha, baixe-o no site oficial: https://www.python.org/downloads/

2. **Abrir a pasta do jogo:**  
   Abra o Visual Studio Code e selecione a pasta onde está salvo o projeto.

3. **Executar o jogo:**  
   Abra o terminal do Visual Studio Code, acessando Terminal e, em seguida, Novo Terminal.

   No terminal, execute o comando:

   ```bash
   python jogo-da-velha.py
   ```

   Pressione Enter para iniciar o programa.

4. **Utilizar o menu:**  
   Após iniciar o programa, siga as instruções exibidas no terminal para escolher uma opção do menu e interagir com o jogo.

## Regras do jogo

1. O tabuleiro tem 3 linhas e 3 colunas.
2. Dois jogadores se alternam: X e O.
3. Na sua vez, informe a LINHA e a COLUNA de uma casa vazia (1 a 3).
4. Vence a partida quem completar uma linha, uma coluna ou uma diagonal com o seu símbolo.
5. Se o tabuleiro encher sem vencedor, é empate (não conta na série).
6. No campeonato "melhor de N", vence quem garantir a maioria das vitórias primeiro (2 na melhor de 3 | 3 na melhor de 5).
7. A cada partida, quem começa é alternado.

### Verificação de vitória e empate

O programa verifica se algum jogador venceu utilizando laços `for` e condições `if`. Os laços percorrem as linhas e colunas do tabuleiro para identificar três símbolos iguais na mesma linha ou coluna. Também são utilizados contadores para verificar as diagonais principal e secundária. Para identificar um empate, outros laços percorrem todas as casas do tabuleiro e contam quantas estão vazias. Se houver um vencedor, a partida termina com uma mensagem de vitória. Se não houver vencedor e nenhuma casa estiver vazia, a partida termina em empate.

## Desafio escolhido

Em construção.

## Divisão de tarefas

**Maria Letícia**

- Adiciona verificação de vitória em linhas e colunas com `for`.
- Adiciona verificação das diagonais com contadores.
- Adiciona detecção de empate com `for` aninhado e mensagens de resultado.
- Comenta os Blocos 7, 8 e 9 e adiciona teste de mesa dos laços de vitória.
- Documenta a verificação de vitória e empate no README.

## Testes

Os casos de teste de validação (entradas inválidas, casa ocupada, vitórias, empate e série completa) estão documentados em [docs/tabela_de_testes.md](docs/tabela_de_testes.md), com a entrada, o resultado esperado e o resultado obtido de cada caso.