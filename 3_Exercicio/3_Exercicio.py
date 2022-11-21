import time

def printar_pausar(mensagem):
    time.sleep(1)
    print(mensagem)

def continue_quit():
    while True:
        printar_pausar("Quer digitar outro número?")
        printar_pausar("S/N")
        opcao_usuario = input()
        if opcao_usuario == "S":
            menor_que()
        elif opcao_usuario == "N":
            printar_pausar("Até logo!")
            quit()
        else:
            printar_pausar("Por favor, digite uma resposta válida.")
            continue_quit()   

def menor_que():
    lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    printar_pausar("Por favor, digite um número.")
    numero_usuario = int(input())
    printar_pausar([numeros for numeros in lista if numero_usuario > numeros])
    continue_quit()

menor_que()