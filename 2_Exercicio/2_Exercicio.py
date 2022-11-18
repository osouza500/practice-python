import time


def executar_programa():
    par_ou_impar()
    divisao_exata()


def printar_pausar(mensagem):
    time.sleep(1)
    print(mensagem)


def par_ou_impar():
    try:
        printar_pausar("Vamos descobrir se um número é par, par "
                       "e múltiplo de 4 ou ímpar.")
        printar_pausar("Por favor, digite um número.")
        numero = int(input())
        if numero % 4 == 0 and numero % 2 == 0:
            printar_pausar(f"{numero} é um número par e múltiplo de 4.\n")
        elif numero % 4 != 0 and numero % 2 == 0:
            printar_pausar(f"{numero} é um número par.\n")
        elif numero % 2 != 0:
            printar_pausar(f"{numero} é um número ímpar.\n")
    except ValueError:
        printar_pausar("Por favor, digite um número válido.")
        par_ou_impar()

    # Desafio extra: coletar dois números e verificar se a
    # divisão entre ambos é exata.


def divisao_exata():
    try:
        printar_pausar("Agora vamos verificar se a divisão "
                       "entre dois números é exata.")
        printar_pausar("Por favor, digite um número.")
        numero_2 = int(input())
        printar_pausar("Agora digite outro número.")
        checar_numero = int(input())
        resultado = numero_2 % checar_numero
        if resultado == 0:
            printar_pausar(f"{numero_2} dividido por {checar_numero} é "
                           "uma divisão exata.")
            printar_pausar("Até logo!")
        elif resultado != 0:
            printar_pausar(f"{numero_2} dividido por {checar_numero} "
                           "não é uma divisão exata.")
            printar_pausar("Até logo!")
    except ValueError:
        printar_pausar("Por favor, digite um número válido.")
        divisao_exata()


executar_programa()
