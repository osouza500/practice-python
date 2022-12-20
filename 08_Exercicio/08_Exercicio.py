import random


def condicoes_vitoria(primeira_jogada, segunda_jogada):
    return ((primeira_jogada == "pedra" and segunda_jogada == "tesoura") or
            (primeira_jogada == "tesoura" and segunda_jogada == "papel") or
            (primeira_jogada == "papel" and segunda_jogada == "pedra"))


def jogo():
    jogadas = ["pedra", "papel", "tesoura"]
    while True:
        jogada_humano = input("Pedra, papel ou tesoura?\n").lower()
        jogada_computador = random.choice(jogadas)
        if jogada_humano not in jogadas:
            print("Digite um input válido.\n")
        else:
            if jogada_humano == jogada_computador:
                print(f"Humano: {jogada_humano}; "
                      f"Computador: {jogada_computador}")
                print("Empate!\n")
                jogo()
            if condicoes_vitoria(jogada_humano, jogada_computador):
                print(f"Humano: {jogada_humano}; "
                      f"Computador: {jogada_computador}")
                print("Humano vence máquina!\n")
            elif condicoes_vitoria(jogada_computador, jogada_humano):
                print(f"Humano: {jogada_humano}; "
                      f"Computador: {jogada_computador} ")
                print("Computador vence humano!\n")
            while True:
                continuar_sair = input("Jogar novamente? S/N\n").lower()
                if continuar_sair == "s":
                    jogo()
                elif continuar_sair == "n":
                    print("Até logo!")
                    quit()
                else:
                    print("Digite um input válido.\n")


if __name__ == '__main__':
    jogo()
