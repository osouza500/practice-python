import time

def printar_pausar(mensagem):
    time.sleep(1)
    print(mensagem)

def continue_quit():
    while True:
        printar_pausar("Quer digitar outro número?")
        resposta = input("S/N\n").upper()
        if resposta == "S":
            menor_que()
        elif resposta == "N":
            printar_pausar("Até logo!")
            quit()
        else:
            printar_pausar("Por favor, digite uma resposta válida.")
            continue_quit()   

def menor_que():
    try:
        lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        printar_pausar("Por favor, digite um número.")
        numero_usuario = int(input())
        printar_pausar([numeros for numeros in lista if numero_usuario > numeros])
        continue_quit()
    except ValueError:
        printar_pausar("Por favor, digite um número válido.")
        menor_que()    

menor_que()