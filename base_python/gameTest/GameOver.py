class Game:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        enemy_fianl_hp = enemy_hp - self.power
        if final_hp > enemy_fianl_hp:
            print("I WIN!")
        elif final_hp > enemy_fianl_hp:
            print("Enemy WIN")
        else:
            print("NO WINNER!")


class HouYi(Game):
    def __init__(self, hp, power, defense):
        super().__init__(hp, power)
        self.defense = defense

    def houyi_fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power + self.defense
        enemy_fianl_hp = enemy_hp - self.power
        if final_hp > enemy_fianl_hp:
            print("I WIN!")
        elif final_hp > enemy_fianl_hp:
            print("Enemy WIN")
        else:
            print("NO WINNER!")



hp = 1000
power = 200
defence = 100
houyi = HouYi(hp, power, defence)
houyi.houyi_fight(1000, 200)
