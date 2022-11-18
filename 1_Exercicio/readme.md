# Practice Python - Básico

## Exercício 1

O objetivo deste exercício é criar um programa que pergunte o nome e a idade do usuário;
em seguida, baseado nas informações coletadas, printe uma mensagem comunicando ao usuário
o ano em que ele completará 100 anos.

## Minha solução

Para resolver este desafio, criei uma função chamada **"cem_anos_em()"** que coleta o nome
e a idade de usuário. Em seguida, inseri um loop while para assegurar que, caso o usuário digite
uma idade igual ou maior que 100, o programa printe uma mensagem solicitando um número válido e retorne
ao início.

Caso o número digitado pelo usuário seja válido, ele será subtraído de 100 e a diferença será somada ao
ano corrente (obtido por meio do módulo **datetime**). O total é apresentado ao usuário.

Em seguida, inseri outro loop while para perguntar ao usuário se ele deseja digitar uma nova idade.
Caso a resposta seja positiva, o programa retorna ao início; caso seja negativa, ele é encerrado. 
