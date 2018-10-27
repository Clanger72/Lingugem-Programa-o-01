lista = []


def impar():
    for i in range(2):
        numero = int(input('Digite o %d° número: ' % (i + 1)))
        lista.append(numero)
    for i in lista:
        if i % 2 != 0:
            print(f'O número {i} é impar')


impar()
