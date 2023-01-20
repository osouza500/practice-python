
def frase_contrario():
    resposta = input("Digite uma frase.\n")
    frase = resposta.split()
    frase_contrario = []
    for i in range(len(frase)):
        frase_contrario.append(frase[-1])
        frase.pop()
    nova_frase = ' '.join(frase_contrario)
    print(nova_frase)


if __name__ == "__main__":
    frase_contrario()
