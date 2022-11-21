# Practice Python
## Exercício 3
O objetivo do exercício é escrever um programa que printe todos os elementos da lista **a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]**
menores que cinco. 

Os desafios extras são:
1. Ao invés de printar os elementos um por um, criar uma nova lista que contenha todos os elementos menores que 5 e printar essa nova lista.
2. Escrever isso em apenas uma linha.
3. Pedir ao usuário que digite um número e retornar uma lista que contenha apenas os elementos da lista original menores que o número digitado
   pelo usuário.

## Minha solução
Usei **list comprehension** para criar uma nova lista contendo os números da lista original menores que o número
digitado pelo usuário apenas em uma linha. Inseri uma instrução **try/except ValueError** para assegurar que o programa 
não crashe caso o input seja inválido. 
