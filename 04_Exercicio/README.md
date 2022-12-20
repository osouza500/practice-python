# Practice Python
## Exercício 4
O desafio de hoje é escrever um programa que pegue um número digitado pelo usuário e retorne
uma lista contendo os números que, divididos pelo input, produzem uma divisão exata.

## Minha solução
Limitei o alcance da lista contendo os números a serem divididos a partir da função 
**range(1, 101)**. Inseri um loop **for** para dividir o input do usuário por todos os
números desta lista. Usei a instrução condicional **if** e o operador **módulo** para
descobrir se a divisão é exata.

Caso a divisão seja exata, o número originário da primeira lista é adicionado a uma nova lista
a partir do método **.append()**. Ao cabo do loop, a nova lista é printada.

Usei o método **.join()** para apresentar a lista sem os colchetes.
