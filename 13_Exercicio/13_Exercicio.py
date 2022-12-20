import time


def printar_pausar(mensagem):
    time.sleep(1)
    print(mensagem)


def sequencia_fibonacci():
    seq_fib = []
    try:
        printar_pausar("Quantos números de Fibonacci você quer gerar?")
        qtd_num = int(input())
        print("")
        for ciclo in range(qtd_num):
            if 0 not in seq_fib:
                seq_fib.append(0)
            elif 1 not in seq_fib:
                seq_fib.append(1)
            else:
                seq_fib.append(seq_fib[-1] + seq_fib[-2])
        printar_pausar(f"Sua sequência é: {', '.join(map(str, seq_fib))}.\n")
        printar_pausar("Até logo!")
    except ValueError:
        printar_pausar("Input inválido.\n")
        sequencia_fibonacci()


if __name__ == "__main__":
    sequencia_fibonacci()
