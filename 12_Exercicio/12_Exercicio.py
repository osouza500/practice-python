import random 

def lista_aleatoria():
    lista_aleatoria = []
    for ciclo in range(random.randint(1, 50)):
        lista_aleatoria.append(ciclo)   
    return lista_aleatoria


def primeiro_ultimo(lista):
    nova_lista = [
        numero for numero in lista 
        if numero == lista[0] 
        or numero == lista[-1]
        ]
    print(nova_lista)

primeiro_ultimo(lista_aleatoria())