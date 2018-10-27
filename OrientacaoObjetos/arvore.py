class No:
    """
    Estruturação da arvore, para cada nó dou um dado,
     e tendo um filho esquerdo um filho direito e um pai
    """
    def __init__(self, dado):
        self.dado = dado
        self.filhoesq = None
        self.filhodir = None
        self.pai = None

    def getDado(self):
        return self.dado

    def setDado(self, novo):
        self.dado = novo

    def getFilhoesq(self):
        return self.filhoesq

    def setFilhoesq(self, filho):
        self.filhoesq = filho

    def getFilhodir(self):
        return self.filhodir

    def setFilhodir(self, filho):
        self.filhodir = filho

    def getPai(self):
        return self.pai

    def setPai(self, pai):
        self.pai = pai

    def __str__(self):
        return str("No:" + str(self.getDado()))


class Arvore(No):
    def __init__(self):
        self.raiz = None

    def getRaiz(self):
        return self.raiz

    def setRaiz(self, nova):
        self.raiz = nova

    def buscar(self, x, d):
        if x is None or x.getDado() is d:
            return x
        if d < x.getDado():
            return self.buscar(x.getFilhoesq(), d)
        else:
            return self.buscar(x.getFilhodir(), d)

    def minimo(self, x):
        while x.getFilhoesq() is not None:
            x = x.getFilhoesq()
        return x

    def maximo(self, x):
        while x.getFilhodir() is not None:
            x = x.getFilhodir
        return x

    def sucessor(self, x):
        if x.getFilhodir() is not None:
            return self.minimo(x.getFilhodir())
        y = x.getPai()
        while y is not None and x is y.getFilhodir():
            x = y
            y = y.getPai()
        return y

    def predecessor(self, x):
        if x.getFilhoesq() is not None:
            return self.maximo(x.getFilhoesq())
        y = x.getPai()
        while y is not None and x is y.getFilhoesq():
            x = y
            y = y.getPai()
        return y

    def inserir(self, z):
        y = None
        x = self.getRaiz()
        while x is not None:
            y = x
            if z.getDado() < x.getDado():
                x = x.getFilhoesq()
            else:
                x = x.getFilhodir()
        z.setPai(y)
        if y is None:
            self.setRaiz(z)
        else:
            if z.getDado() < y.getDado():
                y.setFilhoesq(z)
            else:
                y.setFilhodir(z)

    def remover(self, x):
        if x.getFilhoesq() is None or x.Filhodir() is None:
            y = x
        else:
            y = self.sucessor(x)
        if y.getFilhoesq() is not None:
            z = y.getFilhoesq()
        else:
            z = y.getFilhodir()
        if z is not None:
            z.setPai(y.getPai())
        if y.getPai() is None:
            self.setRaiz(z)
        else:
            if y is y.getPai().getFilhoesq():
                y.getPai().setFilhoesq(z)
            else:
                y.getPai().setFilhodir(z)
        if y is not x:
            x.setDado(y.getDado)


