import random


def random_success(probability):
    choice = random.random()
    return (choice <= probability)


class PhantomAssasin:

    def __init__(self, blur = True, coup = True):
        self.hp = 1500.0
        self.attack_value = 122.0
        self.blur = blur
        self.coup = coup

    def receive_attack(self, attack):
        if self.blur and random_success(0.75):
            # print('Ataque evadido')
            pass
        else:
            self.hp = self.hp - attack
        return self.is_dead()

    def attack(self):
        if self.coup and random_success(0.2):
            return self.attack_value * 4.5
        else:
            return self.attack_value

    def is_dead(self):
        return self.hp <= 0


class Enemy:

    def __init__(self):
        self.hp = 1500.0 * 3
        self.attack_value = 122.0 * 3

    def receive_attack(self, attack):
        self.hp = self.hp - attack
        return self.is_dead()

    def attack(self):
        return self.attack_value

    def is_dead(self):
        return self.hp <= 0


class Match:

    def __init__(self, blur = True, coup = True):
        self.assasin = PhantomAssasin(blur,coup)
        self.enemy = Enemy()
        self.turn = 0

    def execute_turn(self):
        self.turn += 1
        end = self.enemy.receive_attack(self.assasin.attack())
        if end:
            return end
        end = self.assasin.receive_attack(self.enemy.attack())
        return end

    def run(self):
        end = False
        while not end:
            end = self.execute_turn()
            # print(f"Turno {self.turn}: Phantom HP => {self.assasin.hp}, Enemigo => {self.enemy.hp}")
        return self.enemy.is_dead()


victories = 0
n = 10000

for i in range(n):
    m = Match()
    if m.run():
        victories += 1

print(f"Batallas con Blur y Coup de Grace\n\tNumero de Victorias: {victories}, Probabilidad Observada: {victories/n}")

victories = 0

for i in range(n):
    m = Match(False, True)
    if m.run():
        victories += 1

print(f"Batallas con Coup de Grace\n\tNumero de Victorias: {victories}, Probabilidad Observada: {victories/n}")


victories = 0

for i in range(n):
    m = Match(True, False)
    if m.run():
        victories += 1

print(f"Batallas con Blur\n\tNumero de Victorias: {victories}, Probabilidad Observada: {victories/n}")