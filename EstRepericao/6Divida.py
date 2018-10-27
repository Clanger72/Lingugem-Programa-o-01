conta = float(input('Digite o valo da conta: '))
parcela = int(input('Digite a quantidade de parcelas: '))

uma = conta * 0
tres = conta * 0.10
seis = conta * 0.15
nove = conta * 0.20
doze = conta * 0.25

if parcela == 1:
    print('Valor    Juros   Qtd Parcelas    Valor Parcela')
    print('%.2f     %.2f       %.2f          %.2f' % (conta, tres, parcela, conta))
elif parcela == 3:
    print('Valor    Juros   Qtd Parcelas    Valor Parcela')
    print('%.2f     %.2f       %.2f          %.2f' % (conta, tres, parcela, (conta + tres) / parcela))
elif parcela == 6:
    print('Valor    Juros   Qtd Parcelas    Valor Parcela')
    print('%.2f   %.2f       %.2f          %.2f' % (conta, seis, parcela, (conta + seis) / parcela))
elif parcela == 9:
    print('Valor    Juros   Qtd Parcelas    Valor Parcela')
    print('%.2f   %.2f       %.2f          %.2f' % (conta, nove, parcela, (conta + nove) / parcela))
elif parcela == 12:
    print('Valor    Juros   Qtd Parcelas    Valor Parcela')
    print('%.2f     %.2f       %.2f          %.2f' % (conta, doze, parcela, (conta + doze) / parcela))