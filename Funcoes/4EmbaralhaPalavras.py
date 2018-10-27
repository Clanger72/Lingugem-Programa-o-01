import random


def embaralhar(p):
    embaralha = random.sample(p, len(p))
    s = ''.join(embaralha)
    return print(s)


text = str(input('Digite o texto a ser embaralhado'))

embaralhar(text)
