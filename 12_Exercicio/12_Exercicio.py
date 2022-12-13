import random 

def lista_aleatoria():
    lista_aleatoria = [random.randint(1, 50) for ciclo in range(random.randint(1, 50))]
    print(lista_aleatoria)
    return lista_aleatoria


def primeiro_ultimo(lista):
    nova_lista = [
        numero for numero in lista 
        if numero == lista[0] 
        or numero == lista[-1]
        ]
    print(nova_lista)

primeiro_ultimo(lista_aleatoria())