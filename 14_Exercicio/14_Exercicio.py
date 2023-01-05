import random

def gerador_lista():
    lista_aleatoria = [random.randint(1, 50) for ciclo in range(random.randint(1, 50))]
    return lista_aleatoria

def remover_repetidos(lista):
    print(f"Primeira lista: {lista}\n")
    lista = list(set(lista))
    print(f"Segunda lista (sem repetições): {lista}")

remover_repetidos(gerador_lista())