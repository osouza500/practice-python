import random

def continuar_sair():
    resposta = input("Desistir? S/N\n").lower()
    if resposta == "s":
         print("Até logo!")
         quit()
    elif resposta == "n":
        pass
    else:
        print("Input inválido.")
        continuar_sair()

def jogo_adivinhacao ():
    numero = random.randint(1, 9)
    while True:
        try:
            resposta_usuario = int(input("Digite um número de 1 a 9.\n"))
        except ValueError:
            print("Input inválido\n")
            jogo_adivinhacao()
        if resposta_usuario < 1 or resposta_usuario > 9:
            print("Input inválido.\n")
            jogo_adivinhacao()
        elif resposta_usuario == numero:
            print("Na mosca!")
            quit()
        elif resposta_usuario < numero:
            print("Chutou baixo.")
            continuar_sair()
        elif resposta_usuario > numero:
            print("Chutou alto.")
            continuar_sair()
    


jogo_adivinhacao()
    