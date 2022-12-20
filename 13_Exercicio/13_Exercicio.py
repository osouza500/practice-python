import time


def printar_pausar(mensagem):
    time.sleep(.5)
    print(mensagem)


def sequencia_fibonacci():
    seq_fib = []
    printar_pausar("Quantos números na sequência?")
    qtd_num = int(input())
    for ciclo in range(qtd_num):
        if 0 not in seq_fib:
            seq_fib.append(0)
        elif 1 not in seq_fib:
            seq_fib.append(1)
        else:
            seq_fib.append(seq_fib[-1] + seq_fib[-2])
    print(", ".join(map(str, seq_fib)))

sequencia_fibonacci()

