import random 

def lista_aleatoria():
    lista = []
    for count in range(random.randint(1, 30)):
        numero = random.randint(1, 30)
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
    if len(lista_1) > len(lista_2):
        

    
      

    # print(lista_1)
    # print(lista_2)    
    # print(len(lista_1))
    # print(len(lista_2))
    

comparar_listas()        
