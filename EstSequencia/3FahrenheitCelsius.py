def converte(fahrenheit):
    return 5 * (fahrenheit - 32) / 9


c = float(input('Qual a temperatura em Fahrenheit: '))

print('Convertida em Celsius é: {:.2f}'.format(converte(c)))
