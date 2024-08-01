from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "удар мечом"


class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"


class Fighter:
    def __init__(self):
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return f"Боец наносит {self.weapon.attack()}."
        else:
            return "Боец бьет без оружия!"


fighter = Fighter()
monster = "Монстр"

sword = Sword()
bow = Bow()

fighter.change_weapon(sword)
print("Боец выбирает меч.")
print(fighter.attack())
print(f"{monster} побежден!\n")

fighter.change_weapon(bow)
print("Боец выбирает лук.")
print(fighter.attack())
print(f"{monster} побежден!")
