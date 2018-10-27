x = int(input('Digite um lado do triângulo: '))
y = int(input('Digite o segundo lado: '))
z = int(input('Digite o terceiro lado: '))

if x == y and y == z and z == x:
     print('Triângulo Equilátero')
elif x == y and x != z or x == z and x != y or y == z and y != x:
    print('Triângulo Isóceles')
elif x != y and y != z and z != x:
    print('Triângulo Escaleno')
else:
    print('Não é um triângulo')