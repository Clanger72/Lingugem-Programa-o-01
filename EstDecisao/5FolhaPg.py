vHora = float(input('Qual o valor da hora trabalhada: '))
QtdHora = float(input('Qauntas horas trabalhadas: '))

sBruto = vHora * QtdHora

cinco = sBruto * 0.05
dez = sBruto * 0.10
onze = sBruto * 0.11
vinte = sBruto *0.20

if sBruto < 900:
    print(f'Salário Bruto      : R$ {sBruto}')
    print('(-) IR (0%)         : R$  Isento')
    print(f'(-) INSS (10%)     : R$ {dez}')
    print(f'FGTS (11%)         : R$ {onze}')
    print(f'Total de descontos : R$ {dez + cinco}')
    print(f'Salário Liquido    : R$ {sBruto - dez}')
elif sBruto > 900 and sBruto <= 1500:
    print(f'Salário Bruto      : R$ {sBruto}')
    print(f'(-) IR (5%)        : R$ {cinco}')
    print(f'(-) INSS (10%)     : R$ {dez}')
    print(f'FGTS (11%)         : R$ {onze}')
    print(f'Total de descontos : R$ {dez + cinco}')
    print(f'Salário Liquido    : R$ {sBruto - dez - cinco}')
elif sBruto > 1500 and sBruto <= 2500:
    print(f'Salário Bruto      : R$ {sBruto}')
    print(f'(-) IR (10%)        : R$ {dez}')
    print(f'(-) INSS (10%)     : R$ {dez}')
    print(f'FGTS (11%)         : R$ {onze}')
    print(f'Total de descontos : R$ {dez + cinco}')
    print(f'Salário Liquido    : R$ {sBruto - dez - dez}')
elif sBruto > 2500:
    print(f'Salário Bruto      : R$ {sBruto}')
    print(f'(-) IR (20%)        : R$ {vinte}')
    print(f'(-) INSS (10%)     : R$ {dez}')
    print(f'FGTS (11%)         : R$ {onze}')
    print(f'Total de descontos : R$ {dez + cinco}')
    print(f'Salário Liquido    : R$ {sBruto - dez - vinte}')