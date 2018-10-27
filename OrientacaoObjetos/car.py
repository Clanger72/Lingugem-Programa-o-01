class car:
    def __init__(self, consume):
        self.consume = consume
        self.amount = 0

    def walk(self, andar):
        self.amount =  self.amount - (andar / self.consume)


mycar = car(15)
mycar.amount = 20
mycar.walk(100)
print(mycar.amount)