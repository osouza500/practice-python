import time


def printar_pausar(mensagem):
    time.sleep(.5)
    print(mensagem)

def sequencia_fibonacci():
    printar_pausar("Digite o número correspondente à quantidade de números na sequência:")
    qtdnum_sequencia = int(input())