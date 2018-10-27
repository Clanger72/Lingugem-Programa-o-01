def valor(v):
    if v == '':
        return int(1)
    else:
        return faixa(int(v))


def faixa(v):
    if v < 1:
        return 1
    elif v > 20:
        return 20
    else:
        return v


def linha(l):
    li = '+'
    for x in range(l):
        li += '-'
    li += '+'
    print(li)


def coluna(l, c):
    for y in range(c):
        co = '|'
        co += ' ' * l
        co += '|'
        print(co)


def desenha(l, c):
    linha(l)
    coluna(l, c)
    linha(l)


linhas = int(input('Digite quantos --- entre 1 e 20 você deseja: '))
colunas = int(input('Digite qantos | | entre 1 a 2 voc}e deseja: '))
desenha(valor(linhas), faixa(colunas))