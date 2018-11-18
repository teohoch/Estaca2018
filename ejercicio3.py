import random
import numpy as np


class Player:

    def __init__(self, center, dispersion, debug=False):
        self.center = np.array(center)
        self.dispersion = dispersion
        self.shots_taken = 0
        self.victory_shots = 0
        self.debug = debug
        self.nearest_distance = 100000

    def shot(self):
        self.shots_taken += 1

        valid_shot = False
        if self.debug:
            print(f"Disparo: {self.shots_taken}")

        while not valid_shot:
            target_x = self.center[0] + ((random.random()- 0.5) * 2 * self.dispersion)
            target_y = self.center[1] + ((random.random()- 0.5) * 2 * self.dispersion)

            target = np.array([target_x, target_y])
            if self.debug:
                print(f"\t{target}")
                print(f"\t{np.linalg.norm(target - self.center)}")
            valid_shot = np.linalg.norm(target - self.center) <= self.dispersion

        if self.hit(target):
            self.victory_shots += 1
            return True
        else:
            return False

    def hit(self, target):
        bullseye = np.array([0, 0])
        distance = np.linalg.norm(target - bullseye)
        self.save_nearest(distance)
        return distance <= 1.0

    def save_nearest(self,distance):
        if distance <= self.nearest_distance:
            self.nearest_distance = distance

    def observed_probability(self):
        return self.victory_shots / self.shots_taken

    def missed_shots(self):
        return self.shots_taken - self.victory_shots


players = [Player([0, 0], 4), Player([1, 0], 6), Player([0, 0], 10), Player([0, 2], 5) ]

dice_faces = [4,1,2,3,3,3]

n = 1000


for i in range(n):
    selected = random.choice(dice_faces)
    players[selected-1].shot()

# Probabilidad que el rifle caiga en el blanco

print(f"Disparos del Jugador con Rifle:\n\tNumero de disparos: {players[0].shots_taken}, Numero de disparos acertados: {players[0].victory_shots}, Probabilidad Observada: {players[0].observed_probability()}")

# Probabilidad que slingshot sea el elegido si se acerto en el blanco

hits = 0

for i in players:
    hits += i.victory_shots

misses = n - hits
print(f"De los {hits} disparos acertados, {players[2].victory_shots} fueron por el jugador con Slingshot, dando una "
      f"probabilidad observada de { players[2].victory_shots/hits}")

# Probabilidad que arco sea el elegido si se fallo el blanco




print(f"De los {misses} disparos errados, {players[1].missed_shots()} fueron por el jugador "
      f"con Arco y fleca, dando una probabilidad observada de "
      f"{ (players[1].missed_shots()) / misses }")

# Probabilidad de acertar si no se eligio un arma de fuego


sum = hits - players[0].victory_shots

print(f"De los {hits} disparos acertados, {sum} fueron por jugadores sin un arma de fuego, dando una "
      f"probabilidad observada de { sum/hits}")

