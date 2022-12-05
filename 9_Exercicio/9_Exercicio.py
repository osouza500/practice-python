import random

def jogo_adivinhacao ():
    tentativas = 0
    numero = random.randint(1, 9)
    while True:
        try:
            resposta_usuario = int(input("Digite um número de 1 a 9 "
                                         "ou SAIR para sair.\n"))
        except ValueError:
            if resposta_usuario == "SAIR":
                print("Até logo!")
                quit()
            else:
                print("Input inválido.")
                jogo_adivinhacao()
        if int(resposta_usuario) < 1 or int(resposta_usuario) > 9:
            print("Input inválido.\n")
            jogo_adivinhacao()
        elif resposta_usuario == numero:
            tentativas += 1
            print("Na mosca!")
            print(f"Você tentou {tentativas} vezes.")
            print("Até logo!")
            quit()
        elif resposta_usuario < numero:
            tentativas += 1
            print("Chutou baixo.")
            continuar_sair()
        elif resposta_usuario > numero:
            tentativas += 1
            print("Chutou alto.")
            continuar_sair()
    
jogo_adivinhacao()
    