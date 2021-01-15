from base_python.game import Game

class HouYi(Game):
    def __init__(self, hp, power, defense):
        super().__init__(hp, power)
        self.defense = defense

    def houyi_fight(self, enemy_hp, enemy_power):
        while True:
            self.hp = self.hp - enemy_power + self.defense
            enemy_hp = enemy_hp - self.power
            if self.hp <= 0:
                print("I WIN!")
                break
            elif enemy_hp <= 0:
                print("Enemy WIN")
                break

