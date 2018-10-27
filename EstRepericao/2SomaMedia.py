lista = []


def numeros():
    for i in range(2):
        entrada = int(input('Digite o %d° número: ' % (i + 1)))
        lista.append(entrada)
    soma = sum(lista)
    media = soma / i
    return print(f'A soma é {soma} e a media é {media}')


numeros()
