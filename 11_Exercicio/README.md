# Practice Python
## Exercício 11
A proposta do exercício é criar um programa que peça um número ao usuário e retorne
uma mensagem comunicando se tal número é primo ou não.
## Minha solução
A função **input_usuário()** coleta e retorna o input do usuário (um número de 2 a 100). A instrução **try/except** 
evita que o programa quebre em caso de **ValueError**.

Já a função **numero_primo(numero)** avalia se o número é primo ou não a partir de um loop **for** e uma instrução 
**if** baseada em uma operação módulo.

O programa é iniciado a partir da função **número_primo(numero)** passando a função **input_usuario()** como argumento.
