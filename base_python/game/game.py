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
            raise Exception("NO WIN!!!!!!!!!!!")
