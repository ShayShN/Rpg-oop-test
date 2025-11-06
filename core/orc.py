import random

class Orc:
    weapons = ["knife", "sword", "axe"]
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.type = "orc"
        self.speed = random.randint(0, 5)
        self.power = random.randint(10, 15)
        self.rating_armor = random.randint(2, 8)
        self.weapon = random.choice(Orc.weapons)
        
    def speak(self):
        print(f'the {self.type} {self.name} is angry!')
        
    def attack(self):
        pass
    
#     def __str__(self):
#         return f'{self.name}, {self.hp}, {self.type}, {self.speed}, {self.power}, {self.rating_armor}, {self.weapon}'
    
# o1 = Orc("godzila")
# print(o1)