lista = []


def numero():
    for i in range(5):
        numeros = int(input('Digite o %d° número: ' % (i + 1)))
        lista.append(numeros)
    maior = max(lista)
    return print(f'O maior número é: {maior}')


numero()
