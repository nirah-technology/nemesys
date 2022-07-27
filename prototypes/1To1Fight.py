from colorama import init, Fore
from threading import Thread
from random import random, randint
from time import sleep

init(autoreset=True)

class Character:
    def __init__(self) -> None:
        self.name: str
        self.level: int
        self.life: int
        self.damage_min: int
        self.damage_max: int
        self.attack_speed: float
        self.combat: Combat = None
        self.is_fighting: bool = False

    def attack(self, target):
        self.is_fighting = True
        if (self.combat != None):
            self.combat.terminate()
        self.combat = Combat(fighter=self, target=target)
        self.combat.start()
        
    def stop_attack(self):
        self.is_fighting = False
        if (self.combat != None):
            self.combat.terminate()

class Combat(Thread):
    def __init__(self, fighter: Character, target: Character):
        Thread.__init__(self)
        self.fighter: Character = fighter
        self.target: Character = target
        self.__must_fight: bool = False
    
    def run(self):
        self.__must_fight = True
        self.fighter.is_fighting = True
        self.target.is_fighting = True
        while (self.__must_fight and self.fighter.life > 0 and self.target.life > 0):
            print("{}{} - pv: {}".format(Fore.MAGENTA, self.target.name, self.target.life))
            damage = random() + randint(self.fighter.damage_min, self.fighter.damage_max)
            self.target.life -= damage
            print("{}{} - pv: {}".format(Fore.MAGENTA, self.target.name, self.target.life))
            sleep(self.fighter.attack_speed)
        print("{}{} stop to attack {}".format(Fore.GREEN, self.fighter.name, self.target.name))
        
        self.fighter.is_fighting = False
        self.target.is_fighting = False
    
    def terminate(self):
        self.__must_fight = False

class Warrior(Character):
    TOTAL_CREATED: int = 0
    def __init__(self) -> None:
        super().__init__()
        Warrior.TOTAL_CREATED += 1
        self.name = "Warrior-#{}".format(Warrior.TOTAL_CREATED)
        self.life = 100
        self.attack_speed = 2.5
        self.damage_min = 2
        self.damage_max = 5

class Player(Character):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name
        self.life = 100
        self.attack_speed = 0.8
        self.damage_min = 1
        self.damage_max = 3

def main():
    player = Player("Jxalo")
    vilain1 = Warrior()
    vilain2 = Warrior()

    player.attack(vilain1)
    vilain1.attack(player)
    player.attack(vilain2)
    vilain2.attack(player)

    sleep(10)
    player.stop_attack()
    vilain1.stop_attack()
    vilain2.stop_attack()

    print("{}: {} pv".format(player.name, player.life))
    print("{}: {} pv".format(vilain1.name, vilain1.life))
    print("{}: {} pv".format(vilain2.name, vilain2.life))

if (__name__ == "__main__"):
    main()
