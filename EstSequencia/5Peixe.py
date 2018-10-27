def peixes(peso):
    if peso <= 50:
        return peso
    elif peso > 50:
        multa = (peso - 50) * 4
    return peso, multa


p = float(input('Quantos kg de peixe tem: '))

print('O peso e a multa são: {}'.format(peixes(p)))
