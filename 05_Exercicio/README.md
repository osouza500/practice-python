# Practice Python
## Exercício 5
O desafio de hoje é pegar duas listas e escrever um programa que retorne uma nova lista 
que contenha apenas os elementos em comum entre as duas listas originais (sem duplicações).
É preciso assegurar que o programa funciona com duas listas de tamanhos diferentes.

Desafios extras:
  1. Gerar duas listas aleatórias;
  2. Escrever em apenas uma linha de código.
  
 ## Minha solução
 Honestamente, tenho a impressão que compliquei algo simples - em outras palavras, que o código ficou
 maior do que deveria (o que significa que não consegui cumprir o desafio extra 2). 
 A resposta oficial não se encontra no site, então não pude compará-la com a minha.
 
 Criei a função **lista_aleatoria()** para gerar listas aleatorias de tamanhos diferentes, limitadas a no 
 máximo 30 itens e contendo números aleatórios de 1 a 30, sem duplicações. 
 
 A função **comparar_listas** cria duas listas aleatórias, verifica qual tem mais itens e, a partir de um loop
 **for** com a quantidade de iterações baseada na lista maior, checa se o número corrente se encontra na 
 lista menor. Se houver coincidência, o número é adicionado a uma lista vazia. Ao cabo do loop, esta lista é 
 printada.
