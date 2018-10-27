codigo = {}
cdg = 0

while cdg != '1':
    print('Produto        Código    Valor')
    print('Cachorro Quente  100     R$1.20')
    print('Bauru Simples    101     R$1.30')
    print('Bauru com ovo    102     R$1.50')
    print('Humbúrguer       103     R$1.20')
    print('Cheeseburguer    104     R$1.30')
    print('Refrigerante     105     R$1.00')
    cdg = str(input('Digite o código do produto ou 1 para encerrar pedido: '))

    if cdg == '100':
        codigo['Cachorro Quente'] = 1.20
    if cdg == '101':
        codigo['Bauru Simples'] = 1.30
    if cdg == '102':
        codigo['Bauru com ovo'] = 1.50
    if cdg == '103':
        codigo['Humbúrguer'] = 1.20
    if cdg == '104':
        codigo['Cheeseburguer'] = 1.30
    if cdg == '105':
        codigo['Refrigerante'] = 1.00

print('Produto           Valor')
for k, v in codigo.items():
    print(k, '- R$', v)

print('\nTotal do pedido R$%.2f' % sum(codigo.values()))
