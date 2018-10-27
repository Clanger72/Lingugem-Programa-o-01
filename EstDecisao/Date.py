from datetime import datetime

strDate = str(input('Digite uma data no formato 00/00/00: '))

objDate = datetime.strptime(strDate, '%d/%m/%y')


day = datetime.strftime(objDate, '%d')
month = datetime.strftime(objDate, '%m')
year = datetime.strftime(objDate, '%y')

valid = False

if month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12':
    if day <= '31':
        valid = True
elif month == '02':
    if day <= '28':
        valid = True
elif month == '04' or month == '06' or month == '09' or month == '11':
    if day <= '30':
        valid = True


if valid == True:
    print('Data Válida')
else:
    print('Data Inválida')