class Fila:
    def __init__(self):
        self.dados = []
        self.tamanho = 0

    def insere(self, elemento):
        self.dados.append(elemento)
        self.tamanho = self.tamanho + 1

    def remove(self):
        self.tamanho = self.tamanho - 1
        return self.dados.pop(0)

    def testa_vazia(self):
        return len(self.dados) == 0

    def to_list(self):
        return self.dados


fila = Fila()
fila.insere(1)

assert [1] == fila.to_list()
assert 1 == fila.tamanho

fila.insere(2)

assert [1, 2] == fila.to_list()
assert 2 == fila.tamanho

fila.insere(3)

assert [1, 2, 3] == fila.to_list()
assert 3 == fila.tamanho

fila.remove()

assert [2, 3] == fila.to_list()
assert 2 == fila.tamanho

fila.remove()

assert [3] == fila.to_list()
assert 1 == fila.tamanho

fila.remove()

assert [] == fila.to_list()
assert fila.testa_vazia()