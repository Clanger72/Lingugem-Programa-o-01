def alunos(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media == 10:
        return print('Aprovado com Destinção')
    elif media >= 6:
        return print('Aprovado')
    elif media < 6:
        return print('Reprovado')


n01 = float(input('Digite a n1: '))
n02 = float(input('Digite a n2: '))
n03 = float(input('Digite a n3: '))

alunos(n01, n02, n03)
