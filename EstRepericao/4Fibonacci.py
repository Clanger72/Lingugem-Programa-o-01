def fibonacci():
    n = int(input('Digite um valor maio que 0: '))

    anterior = 0
    atual    = 1
    i        = 1

    while i < n:
        proximo  = anterior + atual
        anterior = atual
        atual    = proximo
        i        = i + 1
        print(f'{atual}')


fibonacci()