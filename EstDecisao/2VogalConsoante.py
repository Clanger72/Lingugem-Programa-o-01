def letra(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return print('É uma vogal')
    elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        return print('É uma vogal')
    else:
        return print('É uma consoante')


l = str(input('Digite uma letra: '))

letra(l)
