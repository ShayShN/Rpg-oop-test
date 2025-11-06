import random

class Goblin:
    weapons = ["knife", "sword", "axe"]

    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.type = "goblin"
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.rating_armor = 1
        self.weapon = random.choice(Goblin.weapons)
    
    def speak(self):
        print(f'the {self.type} {self.name} is angry!')
        
    def attack(self):
        pass
    
    def run_away(self):
        pass
    
#     def __str__(self):
#         return f'{self.name}, {self.hp}, {self.type}, {self.speed}, {self.power}, {self.rating_armor}, {self.weapon}'
    
# g1 = Goblin("ddd")
# print(g1)