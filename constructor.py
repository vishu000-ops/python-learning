class Enemy:
    def __init__(self, typeofenemy, healthpoints, attackdamage):
        self.typeofenemy = typeofenemy
        self.healthpoints = healthpoints
        self.attackdamage = attackdamage

        def talk(self):
            print("I am enemy")

zombie = Enemy('zombie', 50, 10)

print(zombie.attackdamage)