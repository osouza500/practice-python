def divisao_exata():
    try:
        usuario_numero = int(input("Digite um número de 1 a 100.\n"))
        lista = []
        for numeros in range(1, 101):
            if usuario_numero % numeros == 0:
                lista.append(numeros)
            elif usuario_numero > 100:
                print("Por favor, digite um número válido")
                divisao_exata()
        resultado_final = ', '.join(str(item) for item in lista)
        print(f"O número {usuario_numero} produz uma divisão exata "
              f"quando dividido pelo(s) seguinte(s) número(s): "
              f"{resultado_final}.")
    except ValueError:
        print("Por favor, digite um número válido.")
        divisao_exata()


if __name__ == "__main__":
    divisao_exata()
