def par_ou_impar():
    try:
        numero = int(input("Por favor, digite um número.\n"))
    except ValueError:
        print("Por favor, digite um número válido.")
        par_ou_impar()
    if numero % 4 == 0 and numero % 2 == 0:
        print(f"{numero} é um número par e múltiplo de 4.")
    elif numero % 4 != 0 and numero % 2 == 0:
        print(f"{numero} é um número par.")
    elif numero % 2 != 0:
        print(f"{numero} é um número ímpar.")

    # Desafio extra: coletar dois números e verificar se a
    # divisão entre ambos é exata.
    numero_2 = int(input("Por favor, digite outro número.\n"))
    checar_numero = int(input("Agora digite outro número para "
                              "verificar se a divisão entre " 
                              "ambos é exata.\n"))
    resultado = numero_2 % checar_numero
    if resultado == 0:
        print(f"{numero_2} dividido por {checar_numero} é "
               "uma divisão exata.")
    elif resultado != 0:
        print(f"{numero_2} dividido por {checar_numero} "
               "não é uma divisão exata.") 


par_ou_impar()
