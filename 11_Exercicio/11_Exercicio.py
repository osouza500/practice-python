def input_usuario():
    numero = int(input("Digite um número.\n"))
    return numero

def numero_primo():
    numero = input_usuario()
    for ciclo in range(numero):
        if numero % ciclo == 0:
            print(f"{numero} não é um número primo.")
        else:
            print(f"{numero} é um número primo.")
        
