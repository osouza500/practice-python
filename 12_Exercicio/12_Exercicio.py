import random


def lista_aleatoria():
    # cria uma lista aleatória
    lista_aleatoria = [random.randint(1, 50) for ciclo in range(random.randint(1, 50))]
    # remove números repetidos
    lista_aleatoria = list(set(lista_aleatoria))
    return lista_aleatoria


def primeiro_ultimo(lista):
    # cria uma nova lista contendo
    # o primeiro e o último elemento
    # da lista original
    nova_lista = [lista[0], lista[-1]]
    print(nova_lista)

if __name__ == "__main__":
    primeiro_ultimo(lista_aleatoria())

