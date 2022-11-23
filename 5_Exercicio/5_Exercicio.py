import random


def lista_aleatoria():
    lista = []
    for count in range(random.randint(1, 30)):
        numero = random.randint(1, 30)
        if numero not in lista:
            lista.append(numero)
        else:
            pass
    return lista


def comparar_listas():
    lista_1 = lista_aleatoria()
    lista_2 = lista_aleatoria()
    lista_final = []
    # descobre qual lista é maior
    if len(lista_1) > len(lista_2):
        maior_lista = lista_1
        menor_lista = lista_2
    else:
        maior_lista = lista_2
        menor_lista = lista_1
    # determina o número de iterações baseado
    # na lista com o maior número de itens
    for numero in maior_lista:
        if numero in menor_lista:
            lista_final.append(numero)
        else:
            pass
    # para printar a lista sem colchetes
    resultado_final = ', '.join(str(item) for item in lista_final)
    if lista_final == []:
        print("Não há nenhum número em comum.")
    else:
        print(f"Ambas as listas tem em comum o(s) "
              f"número(s) {resultado_final}.")


if __name__ == "__main__":
    comparar_listas()
