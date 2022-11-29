def e_palindromo():
    print("Escreva uma palavra ou frase.")
    resposta = input().lower()
    ao_contrario = []
    indice = -1
    for letra in resposta:
        ao_contrario.append(resposta[indice])
        indice -= 1
    ao_contrario = "".join(ao_contrario)
    if ao_contrario == resposta:
        print(f"A palavra/frase {resposta} é um palíndromo.")
    else:
        print(f"A palavra {resposta} não é um palíndromo.")      

e_palindromo()