import random

def condicoes_vitoria(primeira_jogada, segunda_jogada):
    return((primeira_jogada == "pedra" and segunda_jogada == "tesoura") or
           (primeira_jogada == "tesoura" and segunda_jogada == "papel" ) or
           (primeira_jogada == "papel" and segunda_jogada == "pedra"))


def jogo():
    jogadas = ["pedra", "papel", "tesoura"]
    jogada_humano = input("Pedra, papel ou tesour?\n").lower()
    jogada_computador = random.choice(jogadas)
    if jogada_humano == jogada_computador:
        print("Empate!")
        jogo()