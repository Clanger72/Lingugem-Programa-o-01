class Bicho_Virtual:
    def __init__(self, name, hunger, health):
        self.name = name
        self.hunger = hunger
        self.health = health
        self.age = 0

    def humor(self, new_hunger, new_health):
        self.hunger += new_hunger
        self.health += new_health

    def get_humor(self):
        return self.hunger, self.health


first_name = str(input('De uma nome para o seu Tamagotchi: '))

tamagotsh = Bicho_Virtual(first_name, 0, 0)

while tamagotsh.age <= 10:
    month = 0
    while month <= 12:
        print(tamagotsh.hunger, tamagotsh.health)
        print(f'{tamagotsh.name}, quer atenção, escolha uma opção!')
        option = int(input('Para Da comida -> 1 \nPara cuidar da saúde -> 2 \nPara saber a idade -> 3 \nPara saber o humor -> 4 \nPara sair -> 0\n'))
        if option == 1:
            eat = int(input(('Batatas fritas -> 1 \nSopa -> 2 \nfruta -> 3 \nChocolate -> 4\n')))
            tamagotsh.humor(1, 0)
        elif option == 2:
            take_care = int(input('Dar banho -> 1 \nBrincar -> 2 \nColocar para dormir -> 3\n'))
            tamagotsh.humor(0, 1)
        elif option == 3:
            print(f'\n{tamagotsh.name} tem {tamagotsh.age} anos!\n')
        elif option == 4:
            if tamagotsh.hunger == 0 and tamagotsh.health == 0:
                print(f'{tamagotsh.name} está triste, cuide dele!\n')
            elif tamagotsh.health >= 1 and tamagotsh.hunger == 0:
                print(f'{tamagotsh.name} precisa comer!\n')
            elif tamagotsh.health == 0 and tamagotsh.hunger >= 1:
                print(f'{tamagotsh.name} precisa cuidar da saúde!\n')
            elif tamagotsh.hunger >= 1 and tamagotsh.health >= 1:
                print(f'{tamagotsh.name} esta bem, para ficar feliz, de mais carino!\n')
        elif option == 0:
            month = 13
            tamagotsh.age = 11
        else:
            print('Opção errada!\n')
        month += 1
    tamagotsh.age += 1



