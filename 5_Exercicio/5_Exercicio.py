import random 

def lista_aleatoria():
    lista = []
    for count in range(random.randint(1, 31)):
        numero = random.randint(1, 10)
        if numero not in lista:
            lista.append(numero)
        else:
            pass
    return lista

def comparar_listas():
    

comparar_listas()        

