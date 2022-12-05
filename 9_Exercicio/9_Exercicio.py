import random

def jogo_adivinhacao ():
    numero = random.randint(1, 9)
    print("Bem-vindo ao jogo de adivinhação.\n")
    resposta_usuario = int(input("Digite um número de 1 a 9.\n"))
    if resposta_usuario < 1 or resposta_usuario > 9:
        print("Digite um número válido.\n")
        jogo_adivinhacao()
    elif resposta_usuario == numero:
        print("Na mosca!")
    elif resposta_usuario < numero:
        print("Chutou baixo.")
    elif resposta_usuario > numero:
        print("Chutou alto.")

jogo_adivinhacao()
    