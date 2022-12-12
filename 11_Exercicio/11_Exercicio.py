def input_usuario():
    while True:
        try:
            resposta = int(input("Digite um número maior que 1.\n"))
            if resposta <= 1:
                print("Input inválido.")
            else:
                return resposta
        except ValueError:
            print("Input inválido.")

def numero_primo(numero):
    for ciclo in range(2, numero):
        if numero % ciclo == 0:
            print(f"{numero} não é um número primo.")
            break
        else:
            print(f"{numero} é um número primo.")
            break
        
numero_primo(input_usuario())