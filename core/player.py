import random
from ...RPGproject import game

class Player:
    professional = ["cure", "fighter"]
    
    def __init__(self, name):
        self.name = name
        
        self.profession = random.choice(Player.professional)
        
        self.hp = 50 
        if self.profession == "cure":
            if self.hp <= 0:
                return "dead"
            else:
                self.hp += 10 
                       
        self.speed = random.randint(5, 10)
        
        self.power = random.randint(5, 10)
        if self.profession == "fighter":
            self.power += 2
            
        self.rating_armor = random.randint(5, 15)
        
        
    # def __str__(self):
    #     return f'name: {self.name}, hp: {self.hp}, speed: {self.speed}, power: {self.power}, armor: {self.rating_armor}, profession: {self.profession}'    
    
    def speak(self):
        print(f'Hi {self.name} Good luck')
        
    def attack(self):
        rool_20 = game.Game.roll_dice(20)
        self.speed += rool_20
        print(rool_20)
    
p1 = Player("shay")
p2 = Player("ossi")
p1.attack()
print(p2)
