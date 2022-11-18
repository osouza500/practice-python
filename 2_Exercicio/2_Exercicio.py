def par_ou_impar():
    numero = int(input("Por favor, digite um número\n"))
    if numero % 4 == 0 and numero % 2 == 0:
        print(f"{numero} é um número par e múltiplo de 4.")
    elif numero % 4 != 0 and numero % 2 == 0:
        print(f"{numero} é um número par.")
    elif numero % 2 != 0:
        print(f"{numero} é um número ímpar.")

par_ou_impar()
