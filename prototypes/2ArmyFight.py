from threading import Thread
from random import random, randint
from time import sleep

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
    
    def is_alive(self) -> bool:
        return self.life > 0

    def attack(self, target):
        print("{} will start combat againt {} ({} pv)".format(self.name, target.name, target.life))
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
            damage = round(random() + randint(self.fighter.damage_min, self.fighter.damage_max), 2)
            print("{} generate {} damage.".format(self.fighter.name, damage))
            self.target.life -= int(damage)
            print("{} lost {} pv. ({} pv)".format(self.target.name, damage, self.target.life))
            sleep(self.fighter.attack_speed)
        print("{} stop to attack {}".format(self.fighter.name, self.target.name))
        
        self.fighter.is_fighting = False
        self.target.is_fighting = False
    
    def terminate(self):
        self.__must_fight = False

class Warrior(Character):
    TOTAL_CREATED: int = 0
    def __init__(self, name: str = "Warrior") -> None:
        super().__init__()
        Warrior.TOTAL_CREATED += 1
        self.name = "{}-#{}".format(name[0:3], Warrior.TOTAL_CREATED)
        self.life = 100
        self.attack_speed = 2.5
        self.damage_min = 2
        self.damage_max = 5

    def __repr__(self) -> str:
        return str(self.__dict__)

class Army:
    def __init__(self, name: str, total_warriors: int) -> None:
        self.name: str = name
        self.warriors: list[Warrior] = []
        self.battle: Battle = None

        for _ in range(total_warriors):
            self.warriors.append(Warrior(name=self.name))
    
    def remove_warrior(self, warrior: Warrior):
        self.warriors.remove(warrior)

    def attack(self, target_army):
        print("{} will fight {}".format(self.name, target_army.name))
        if (self.battle != None):
            self.battle.terminate()
        self.battle = Battle(fighter_army=self, target_army=target_army)
        self.battle.start()
        print("{} start battle against {}".format(self.name, target_army.name))

    def had_survivor(self) -> bool:
        return len(self.warriors) > 0

class Battle(Thread):
    def __init__(self, fighter_army: Army, target_army: Army):
        Thread.__init__(self)
        self.fighter_army: Army = fighter_army
        self.target_army: Army = target_army
        self.__must_fight: bool = False
        print("Battle {} ({} warriors) againt {} ({} warriors) is ready.".format(self.fighter_army.name, len(self.fighter_army.warriors), self.target_army.name, len(self.target_army.warriors)))

    def run(self):
        self.__must_fight = True
        print("Battle {} againt {} is starting.".format(self.fighter_army.name, self.target_army.name))
        while (self.__must_fight and self.fighter_army.had_survivor() and self.target_army.had_survivor()):
            for warrior in self.fighter_army.warriors:
                if (not warrior.is_alive()):
                    self.fighter_army.remove_warrior(warrior)

            for enemy in self.target_army.warriors:
                if (not enemy.is_alive()):
                    self.target_army.remove_warrior(enemy)    
            
            for warrior in self.fighter_army.warriors:
                if (not warrior.is_fighting):
                    for enemy in self.target_army.warriors:
                        if (not enemy.is_fighting):
                            warrior.attack(enemy)
                            break
        
        print("Battle {} againt {} is finished.".format(self.fighter_army.name, self.target_army.name))
        print("Winer: {}".format(self.fighter_army.name if self.fighter_army.had_survivor() else self.target_army.name))

    def terminate(self): 
        self.__must_fight = False

def main():
    shadows_army = Army("Shadows", 10)
    undead_army = Army("Undeads", 10)
    print("{}: {} warriors".format(shadows_army.name, shadows_army.warriors))
    print("{}: {} warriors".format(undead_army.name, undead_army.warriors))
    shadows_army.attack(target_army=undead_army)
    undead_army.attack(target_army=shadows_army)

if (__name__ == "__main__"):
    main()
