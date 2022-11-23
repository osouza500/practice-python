import random 

def lista_aleatoria():
    lista = []
    for count in range(random.randint(1, 31)):
        numero = random.randint(1, 100)
        if numero not in lista:
            lista.append(numero)
        else:
            pass
    return lista

def comparar_listas():
    lista_1 = lista_aleatoria()
    lista_2 = lista_aleatoria()
    lista_final = []
    contagem = 0
    for numero in range(1, 100):
        if lista_1[contagem] == lista_2[contagem]:
            
            contagem += 1
    print(lista_final)        

comparar_listas()        

