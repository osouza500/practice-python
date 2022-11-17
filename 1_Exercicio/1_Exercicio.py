import time

def print_pause(message):
    print(message)
    time.sleep(1)

def cem_anos_em():
    ano_corrente = 2022
    idade_usuario = print_pause(input("Qual é a sua idade?\n"))
    if idade_usuario > 100:
        print_pause("Por favor, digite um número válido.")
    else:
        subtracao_anos = 100 - int(idade_usuario)
        resultado = ano_corrente + subtracao_anos
        print_pause(f"Você fará 100 anos em {resultado }.")
