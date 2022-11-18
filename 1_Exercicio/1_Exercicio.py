import datetime


# Esta função coleta a idade do usuário e retorna
# o ano em que o mesmo fará 100 anos.
# Se o usuário inserir uma idade maior ou igual a
# 100, o programa printará solicitará
# que o mesmo digite um número válido. Após a
# exibição do resultado, há a opção de
# inserir uma nova idade ou encerrar o programa.
def cem_anos_em():
    data_completa = datetime.date.today()
    ano_corrente = data_completa.year
    nome_usuario = input("Qual é o seu nome?\n")
    idade_usuario = int(input("Qual é a sua idade?\n"))
    while True:
        if int(idade_usuario) >= 100:
            print("Você já tem 100 anos ou mais. Por favor, "
                  "digite um número válido.")
            cem_anos_em()
        else:
            subtracao_anos = 100 - idade_usuario
            print(f"{nome_usuario}, você fará 100 anos "
                  f"em {ano_corrente + subtracao_anos}.")
            while True:
                print("Quer digitar uma nova idade?")
                resposta = input("S/N\n").upper()
                if resposta == "S":
                    cem_anos_em()
                elif resposta == "N":
                    print("Até logo!")
                    quit()
                else:
                    print("Por favor, digite uma resposta válida.")


cem_anos_em()
