import time


def continue_quit():
    print("Quer digitar outro número?")
    resposta = input("S/N\n").upper()
    if resposta == "S":
        menor_que()
    elif resposta == "N":
        print("Até logo!")
        quit()
    else:
        print("Por favor, digite uma resposta válida.")
        continue_quit()


def menor_que():
    try:
        lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        print("Por favor, digite um número.")
        numero_usuario = int(input())
        print([numeros for numeros in lista if numero_usuario > numeros])
        continue_quit()
    except ValueError:
        print("Por favor, digite um número válido.")
        menor_que()


if __name__ == "__main__":
    menor_que()
