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
    # determina qual lista é maior
    if len(lista_1) > len(lista_2):
        maior_lista = lista_1
        menor_lista = lista_2
    else:
        maior_lista = lista_2
        menor_lista = lista_1
    # adiciona os números coincidentes em
    # em uma nova lista
    lista_final = [numero for numero in maior_lista if numero in menor_lista]
    if lista_final == []:
        print("Nenhum número em comum.")
    else:
        # remove os colchetes da lista
        lista_final = ", ".join(str(item) for item in lista_final)
        print(f"Ambas as listas têm em comum o(s) "
              f"número(s) {lista_final}.")


if __name__ == "__main__":
    comparar_lista()
