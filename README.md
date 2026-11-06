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

Campeonato "melhor de N":

O jogador escolhe uma série "melhor de 3" ou "melhor de 5". A escolha é validada: só são aceitos os valores 3 e 5, e qualquer outra entrada mostra uma mensagem de erro e pede de novo, sem o programa fechar.

O número de vitórias necessárias é calculado por `vitorias_necessarias = int(melhor_de / 2) + 1` (2 vitórias na melhor de 3 e 3 vitórias na melhor de 5).

A série continua enquanto `serie_x < vitorias_necessarias and serie_o < vitorias_necessarias`. Usamos `and` porque a série só acaba quando um dos dois jogadores atinge a maioria. Empates não contam para a série: a partida é jogada de novo.

No fim da série, o programa anuncia o campeão, soma um em `campeonatos_x` ou `campeonatos_o` e pergunta se o jogador quer outro campeonato com a mesma série. A resposta aceita `s`, `S`, `n` ou `N` (validada com `or`). Se for `s`, uma nova série começa com o placar zerado.

## Bônus: estatísticas da sessão 

Ao escolher **Sair**, o programa mostra o total de partidas, as vitórias de X e de O com porcentagem, os empates, a maior sequência de vitórias seguidas de cada jogador e os campeonatos vencidos. Se nenhuma partida foi jogada (`total_partidas == 0`), ele avisa isso em vez de calcular as porcentagens, evitando divisão por zero.

## Divisão de tarefas

### Maria Heloísa Mendes: tabuleiro e validação:

- Cria a estrutura inicial do projeto com a matriz do tabuleiro.
- Adiciona a exibição do tabuleiro com `for` aninhado e números de linhas e colunas.
- Adiciona a limpeza da matriz e a validação da linha escolhida.
- Adiciona a validação da coluna e a checagem de casa ocupada.
- Comenta os laços aninhados e adiciona o teste de mesa da exibição.
- Adiciona a tabela de testes de validação em docs.

### Maria Letícia Xavier: regras, turnos e vitória:

- Adiciona a seção Regras do jogo no README.
- Adiciona o laço da partida com controle de turno e contador de rodadas.
- Adiciona a verificação de vitória em linhas e colunas com `for`.
- Adiciona a verificação das diagonais com contadores.
- Adiciona a detecção de empate com `for` aninhado e mensagens de resultado.
- Comenta os Blocos 7, 8 e 9 e adiciona o teste de mesa dos laços de vitória.
- Documenta a verificação de vitória e empate no README.

### Maria Clara Araújo: menu, placar e campeonato:

- Adiciona as variáveis do placar e as instruções de execução no README.
- Adiciona o menu principal com `while` e validação da opção.
- Adiciona a escolha da série melhor de N e a tela de regras.
- Adiciona a atualização e a exibição do placar com porcentagens.
- Integra a partida ao campeonato melhor de N e ao menu.
- Adiciona o fim de série com campeão, jogar novamente e estatísticas ao sair.
- Finaliza o README com desafios escolhidos e divisão de tarefas.

## Testes

Os casos de teste de validação (entradas inválidas, casa ocupada, vitórias, empate e série completa) estão documentados em [docs/tabela_de_testes.md](docs/tabela_de_testes.md), com a entrada, o resultado esperado e o resultado obtido de cada caso.