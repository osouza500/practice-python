def e_palindromo():
    print("Escreva uma palavra ou frase.")
    resposta_original = input()
    comparar_resposta = resposta_original.lower().replace(" ", "")
    ao_contrario = []
    indice = -1
    for letra in comparar_resposta:
        ao_contrario.append(comparar_resposta[indice])
        indice -= 1
    ao_contrario = "".join(ao_contrario)
    if ao_contrario == comparar_resposta:
        print(f"A palavra/frase {resposta_original} é um palíndromo.")
    else:
        print(f"A palavra/frase {resposta_original} não é um palíndromo.")      

if __name__ == "__main__":
    e_palindromo()