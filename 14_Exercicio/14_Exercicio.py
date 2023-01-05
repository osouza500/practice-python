import random


def gerador_lista():
    # cria uma lista aleatória
    lista_aleatoria = [random.randint(1, 50) for ciclo in range(random.randint(1, 50))]
    return lista_aleatoria


def remover_repetidos(lista):
    print(f"Primeira lista: {lista}\n")
    # remove números repetidos
    print(f"Segunda lista (sem repetições): {list(set(lista))}")


if __name__ == "__main__":
    remover_repetidos(gerador_lista())
