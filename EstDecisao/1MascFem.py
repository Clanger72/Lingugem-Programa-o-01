def genero(sexo):
    if sexo != 'M' and sexo != 'F':
        return print('Sexo inválido')
    if sexo == 'M':
        return print('Masculino')
    elif sexo == 'F':
        return print('Feminino')


s = str(input('Para feminino digite F ou M para masculino: '))

genero(s)
