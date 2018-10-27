def formatar(num):
    if len(num) == 8:
        num1 = '9' + num[:4] + '-' + num[4:]
        return print(num1)
    elif len(num) == 9 and num[4:5] != '-':
        numero = num[:5] + '-' + num[5:]
        return print(numero)
    elif len(num) == 9 and num[4:5] == '-':
        numero = '9' + num[0:9]
        return print(numero)
    else:
        return print(num)


n = str(input('Digite o seu celular: '))

formatar(n)
