import random
from core.player import Player
import core.orc
import core.goblin

class Game:
    def __init__(self):
        pass
    
  
    def show_menu(self):
        user_input = input("enter a quit or battle Q/B: ").lower()
        return user_input
    
    def create_player(self):
        return Player("shay")
    
    def choos_random_monster(self):
        choice_monster = ["orc", "goblin"]
        if random.choice(choice_monster) == "orc":
            return core.orc.Orc("Godzila")
        if random.choice(choice_monster) == "goblin":
            return core.goblin.Goblin("Megaldon")
        
    
    def battle(self, player, monster):
        roll_player = g1.roll_dice(6)
        roll_player += player.speed
        
        roll_monster = g1.roll_dice(6)
        roll_monster += monster.speed
        
        while player.hp > 0 or monster.hp > 0:
            
            if roll_player == roll_monster or roll_player > roll_monster:
                player.speak()
                roll_20 = g1.roll_dice(20)
                roll_20 += player.speed
                if roll_20 > monster.rating_armor:
                    rool_attack = g1.roll_dice(6) + player.power
                    monster.ph -= rool_attack
                    
                else:
                    break
            
            if roll_player < roll_monster:
                monster.speak()
                roll_20 = g1.roll_dice(20)
                roll_20 += monster.speed
                if roll_20 < player.rating_armor:
                    rool_attack = g1.roll_dice(6) + monster.power
                    if monster.weapon == "knife":
                        rool_attack *= 0.5
                        player.hp -= rool_attack
                    if monster.weapon == "sword":
                        rool_attack *= 1
                        player.hp -= rool_attack
                    if monster.weapon == "axe":  
                        rool_attack *= 1.5
                        player.hp -= rool_attack 
                    
               
        
    
    def roll_dice(self, sides):
        side6 = 0
        side20 = 0
        if sides == 6:
            side6 += random.randint(1, 6)
            return side6
        elif sides == 20:
            side20 += random.randint(1, 20)
            return side20
            
    
    def start(self):
        
        g1 = Game()
        player = g1.create_player()
        monster = g1.choos_random_monster() 
        g1.battle(player, monster)
