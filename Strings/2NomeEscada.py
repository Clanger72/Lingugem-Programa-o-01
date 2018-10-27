def vertical(nome):
    j = 1
    for v in nome:
        print(str(v) * j)
        j += 1


n = str(input('Digite um nome: '))

vertical(n)