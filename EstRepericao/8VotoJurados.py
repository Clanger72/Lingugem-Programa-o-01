notas = []

nome = str(input('Digite o nome: '))
for i in range(7):
    nota = float(input('Digite a %d° nota: ' % (i + 1)))
    notas.append(nota)


def maiorNota():
    maior = max(notas)
    notas.remove(max(notas))
    return maior


def medias():
    soma = sum(notas)
    media = soma / 5
    return media


def buscaMenor(note):
    menor = note[0]
    for i in note:
        if i < menor:
            menor = i
    notas.remove(menor)
    return menor


print('\nResultado final:')
print(f'Atleta: {nome}')
print(f'Melhor nota: {maiorNota()}')
print(f'Pior nota: {buscaMenor(notas)}')
print('Média: %.2f' % (medias()))

