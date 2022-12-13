def primeiro_ultimo():
    lista = [5, 10, 15, 20, 25]
    nova_lista = [
        numero for numero in lista 
        if numero == lista[0] 
        or numero == lista[-1]
        ]
    print(nova_lista)

primeiro_ultimo()