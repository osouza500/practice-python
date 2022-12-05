import random

def continuar_sair ():
    resposta = input("Jogar novamente? S/N.").lower()
    if resposta == "s":
        jogo_adivinhacao()
    elif resposta == "n":
        print("Até logo!")
        quit()
    else:
        print("Input inválido.")
        continuar_sair()

def jogo_adivinhacao ():
    tentativas = 0
    numero = random.randint(1, 9)
    while True:
        try:
            resposta_usuario = int(input("Digite um número de 1 a 9.\n"))
        except ValueError:
            print("Input inválido.\n")
            jogo_adivinhacao()
        if resposta_usuario < 1 or resposta_usuario > 9:
            print("Input inválido.\n")
            jogo_adivinhacao()
        elif resposta_usuario == numero:
            tentativas += 1
            print("Na mosca!")
            print(f"O número é {numero}! Você tentou "
                  f"{tentativas} vezes.")
            continuar_sair()
        elif resposta_usuario < numero:
            tentativas += 1
            print("Chutou baixo.")
        elif resposta_usuario > numero:
            tentativas += 1
            print("Chutou alto.")
    
jogo_adivinhacao()
    