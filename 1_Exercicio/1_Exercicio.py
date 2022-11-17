import time

def printar_pausar(message):
    print(message)
    time.sleep(2)

# Esta função coleta a idade do usuário e retorna o ano em que o mesmo fará 100 anos.
# Se o usuário inserir uma idade maior ou igual a 100, o programa printará solicitará
# que o mesmo digite um número válido. Após a exibição do resultado, há a opção de 
# inserir uma nova idade ou encerrar o programa.
def cem_anos_em():
    ano_corrente = 2022
    idade_usuario = input("Qual é a sua idade?\n")
    while True:
        if int(idade_usuario) >= 100:
            printar_pausar("Você já tem 100 anos ou mais. Por favor, "
                           "digite um número válido.")
            cem_anos_em()
        else:
            subtracao_anos = 100 - int(idade_usuario)
            printar_pausar(f"Você fará 100 anos em {ano_corrente + subtracao_anos}.")
            while True:
                printar_pausar("Quer digitar uma nova idade?")
                resposta = input("S/N\n").upper()
                if resposta == "S":
                    cem_anos_em()
                elif resposta == "N":
                    printar_pausar("Até logo!")
                    quit()
                else:
                    printar_pausar("Por favor, digite uma resposta válida.")
            
cem_anos_em()
