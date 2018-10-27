def salrio(hora, hMes):
    salario = hora * hMes
    ir = salario * 0.11
    inss = salario * 0.08
    sind = salario * 0.05
    sLiquido = salario - ir - inss- sind
    return salario, ir, inss, sind, sLiquido

h = float(input('Qual o seu salário hora: '))
m = float(input('Quantas horas trabalhou neste mês: '))

print('Sua folha de pagamento é: {}'.format(salrio(h, m)))