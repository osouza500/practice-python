import time

def printar_pausar(mensagem):
    time.sleep(1)
    print(mensagem)

lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

numero_usuario = int(input("Por favor, digite um número.\n"))
print([numeros for numeros in lista if numero_usuario < numeros])


# for numero in lista:
#     if numero < 5:
#         nova_lista.append(numero)
# print(nova_lista)