def e_palindromo():
    print("Escreva uma palavra ou frase.")
    resposta = input().lower()
    indice = 0
    for count in range(len(resposta)):
        print(resposta[indice])
        indice += 1


e_palindromo()