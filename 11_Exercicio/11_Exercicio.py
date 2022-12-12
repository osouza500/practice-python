def input_usuario():
    try:
        numero = int(input("Digite um número maior que 1.\n"))
        if numero <= 1:
            print("Input inválido.")
            input_usuario()
        else:
            return numero
    except ValueError:
        print("Input inválido.")
        input_usuario()

def numero_primo():
    numero = input_usuario()
    for ciclo in range(2, numero):
        if numero % ciclo == 0:
            print(f"{numero} não é um número primo.")
            break
        else:
            print(f"{numero} é um número primo.")
            break
        
numero_primo()