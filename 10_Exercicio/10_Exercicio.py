import random

def lista_aleatoria():
    lista = [random.randint(1, 50) for numero in range(random.randint(1, 50))]
    lista = list(set(lista))
    return lista
   
def comparar_lista():
    lista_1 = lista_aleatoria()
    lista_2 = lista_aleatoria()
    
    if len(lista_1) > len(lista_2):
        maior_lista = lista_1
        menor_lista = lista_2
    else:
        maior_lista = lista_2
        menor_lista = lista_1
    lista_final = [numero for numero in maior_lista if numero in menor_lista]
    if lista_final == []:
        print("Nenhum número em comum.")
    else:
        lista_final = ", ".join(str(item) for item in lista_final)
        print(f"Ambas as listas têm em comum o(s) "
              f"número(s) {lista_final}.")
    
lista_aleatoria()
