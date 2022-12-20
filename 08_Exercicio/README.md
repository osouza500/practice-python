# Practice Python
## Exercício 8
Proposta: criar um jogo de joquempô para dois jogadores. As jogadas devem ser comparadas e uma mensagem printada indicando
o vencedor. O jogo deve oferecer a opção de iniciar uma nova partida. 

## Minha solução
Há poucos dias concluí o projeto final de Python II do curso **"Introduction to programming"** que, por coincidência, também
exigia do estudante um jogo de joquempô — porém, com mais camadas que este exercício. Portanto, a matéria está fresca 
em minha cabeça.

Para este desafio criei um jogo mais simples, de uma rodada só. O jogador 2, controlado pelo computador, escolhe seu movimento aleatoriamente
a partir do método **random.choice()**. Os resultados são comparados baseados na função **condicao_vitoria** e o resultado é printado. Em caso de
empate, a partida é reiniciada. Ao fim do jogo, há a opção de jogar uma nova partida ou encerrar o programa.
