def convercao(celsius):
    return (celsius * 1.8) + 32


f = float(input('Digite a temperatura e Celsius: '))

print('Convertida para Fahrenheit é: {:.2f}'.format(convercao(f)))
