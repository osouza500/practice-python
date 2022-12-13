def input_usuario():
    while True:
        try:
            resposta = int(input("Digite um número de 2 a 100.\n"))
            if resposta <= 1 or resposta > 100:
                print("Input inválido.")
            else:
                return resposta
        except ValueError:
            print("Input inválido.")


def numero_primo(numero):
    if numero == 2:
        print("2 é um número primo.")
        quit()
    for ciclo in range(2, numero):
        if numero % ciclo == 0:
            print(f"{numero} não é um número primo.")
            quit()
    print(f"{numero} é um número primo.")


if __name__ == "__main__":
    numero_primo(input_usuario())
