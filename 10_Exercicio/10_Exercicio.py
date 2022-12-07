import random

def lista_aleatoria():
    lista = []
    for numero in range(random.randint(1,50)):
        numero_aleatorio = random.randint(1, 50)
        if numero_aleatorio not in lista:
            lista.append(numero_aleatorio)
        else:
            pass
    return lista

def comparar_lista():
    lista_1 = lista_aleatoria()
    lista_2 = lista_aleatoria()
    lista_final = []
    if len(lista_1) > len(lista_2):
        maior_lista = lista_1
        menor_lista = lista_2
