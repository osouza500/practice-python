def par_ou_impar():
    numero = int(input("Por favor, digite um número\n"))
    if numero % 2 == 0:
        print(f"{numero} é um número par")
    elif numero % 2 != 0:
        print(f"{numero} é um número ímpar")

par_ou_impar()