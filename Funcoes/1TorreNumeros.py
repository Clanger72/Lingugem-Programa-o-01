def torre(elem):
    i = 0
    while elem > i:
        i += 1
        print(str(i) * i)


n = int(input('Digite um número inteiro: '))

torre(n)
