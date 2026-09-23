#inheritance

class enemy():
    type_of_enemy
    health_points
    attack_damage

    def __init__(self,type_of_enemy, health_points, attack_damage):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage


org = enemy('zombie', 50, 70)
print(org.type_of_enemy())

        