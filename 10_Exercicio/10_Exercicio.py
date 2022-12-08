import random


def lista_aleatoria():
    # cria uma lista de até 50 itens
    # com números aleatórios entre 1 e 50
    lista = [random.randint(1, 50) for numero in range(random.randint(1, 50))]
    # remove duplicatas
    lista = list(set(lista))
    # reorganiza os elementos da lista
    # de forma aleatória
    random.shuffle(lista)
    return lista


def comparar_lista():
    lista_1 = lista_aleatoria()
    lista_2 = lista_aleatoria()
    # identifica qual lista é maior
    # ou se ambas têm o mesmo tamanho
    if len(lista_1) > len(lista_2) or len(lista_1) == len(lista_2):
        # adiciona os números coincidentes
        # em uma nova lista
        lista_final = [numero for numero in lista_1 if numero in lista_2]
    elif len(lista_2) > len(lista_1):
        lista_final = [numero for numero in lista_1 if numero in lista_2]
    if lista_final == []:
        print("Nenhum número em comum.")
    else:
        # remove os colchetes da lista
        lista_final = ", ".join(str(item) for item in lista_final)
        print(f"Ambas as listas têm em comum o(s) "
              f"número(s) {lista_final}.")


if __name__ == "__main__":
    comparar_lista()
