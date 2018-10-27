def farorial():
    n = int(input('Digite um valor positivo: '))

    i      = 1
    numFat = 1

    while i <= n:
        numFat = numFat * i
        i = i + 1
    print(f'{n}! = {numFat}')


farorial()