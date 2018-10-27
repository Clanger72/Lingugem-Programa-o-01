class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = 0
        self.perimeter = 0

    def alteration_volues(self, newx, newy):
        self.x = newx
        self.y = newy

    def __str__(self):
        return f"Ponto x : ({self.x}) Ponto y: ({self.y})"

    def calculate_area(self):
        self.area = self.y * self.x
        return self.area

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.x + self.y)
        return self.perimeter


def tile_home(height, weight):
    tile = Retangulo(height, weight)
    return tile.calculate_area()


def foot_wheel(height, weight):
    foot = Retangulo(height, weight)
    return foot.calculate_perimeter()


print(f'Você vai precisar compras {tile_home(10, 6)}m2')
print(f'Você precisa comprar {foot_wheel(10, 6)}')