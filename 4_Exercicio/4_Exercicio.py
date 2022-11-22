def divisao_exata():
    try:
        usuario_numero = int(input("Digite um número de 1 a 100.\n"))
        resultado_lista = []
        for numeros in range(1, 101):
            if usuario_numero % numeros == 0:
                resultado_lista.append(numeros)
            elif usuario_numero > 100:
                print("Por favor, digite um número válido")
                divisao_exata()
        print(f"O número {usuario_numero} produz uma divisão exata "
              f"quando dividido pelos seguintes números: {resultado_lista}.")                
    except ValueError:
        print("Por favor, digite um número válido.")
        divisao_exata()
        
divisao_exata()                    
