import time

def printar_pausar(mensagem):
    time.sleep(1)
    print(mensagem)

lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
nova_lista = []
for numero in lista:
    if numero < 5:
        nova_lista.append(numero)
print(nova_lista)