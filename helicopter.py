from utils import rand_cell
import os

class Helicopter:

    def __init__(self, weight, height):
        rc = rand_cell(weight, height)
        rx, ry = rc[0], rc[1]
        self.weight = weight
        self.height = height
        self.x = rx
        self.y = ry
        self.tank = 0
        self.maxtank = 1
        self.score = 0
        self.lives = 20

    # обработка движения вертолета
    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.height and ny < self.weight):
            self.x, self.y = nx, ny

    # вывод статуса разных характеристик вертолета
    def print_stats(self):
        print('💧 ', self.tank, '/', self.maxtank, sep="", end="|")
        print('🏆', self.score, end="|")
        print('🧡', self.lives)

    # обработка проигрыша
    def game_over(self):
        # os.system('cls')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('X                                X')
        print('X  GAME OVER! YOUR SCORE IS', self.score, ' X')
        print('X                                X')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        exit(0)

    def export_data(self):
        return {'score': self.score,
                'lives': self.lives,
                'x': self.x,
                'y': self.y,
                'tank': self.tank,
                'maxtank': self.maxtank}

    def import_data(self, data):
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 0
        self.maxtank = data["maxtank"] or 1
        self.lives = data["lives"] or 20
        self.score = data["score"] or 0