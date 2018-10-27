import math


def area(raio):
    return math.pow(raio, 2) * math.pi


r = float(input('Qual o raio do circulo: '))
print('A área do circuli é: {:.2f}'.format(area(r)))
