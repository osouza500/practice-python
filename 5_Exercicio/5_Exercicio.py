import random 

def lista_aleatoria():
    lista = []
    for contagem in range(random.randint(1, 31)):
        numero = random.randint(1, 1000)
        if numero not in lista:
            lista.append(numero)
        else:
            pass
    print(lista)    

lista_aleatoria()