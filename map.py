from utils import rand_bool, rand_cell, rand_next_cell

# константы
CELL_TYPES = "🟩🌲🌊🏥🏬🔥"
TREE_BONUS = 100
UPGRADE_COST = 500
LIVE_COST = 1000

class Map:

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.cells = [[0 for i in range(weight)]for j in range(height)]
        self.generate_forest(20, 50)
        self.generate_river(10)
        self.generate_river(20)
        self.generate_upgrade_shop()
        self.generate_hospital()

    # проверка принадлежности клетки
    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.height or y >= self.weight:
            return False
        return True

    # обработка изначального создания объектов
    def print_map(self, copter, clouds):
        print('⬛' * (self.weight + 2))
        for ri in range(self.height):
            print('⬛', end="")
            for ci in range(self.weight):
                cell = self.cells[ri][ci]
                if (clouds.cells[ri][ci] == 1):
                    print('☁️', end="")
                elif (clouds.cells[ri][ci] == 2):
                    print('⚡️', end="")
                elif (copter.x == ri and copter.y == ci):
                    print('🛸', end="")
                elif (cell >= 0 and cell <= len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print('⬛')
        print('⬛' * (self.weight + 2))

    # обработка создания рек
    def generate_river(self, l):
        rc = rand_cell(self.weight, self.height)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rnc = rand_next_cell(rx, ry)
            rnx, rny = rnc[0], rnc[1]
            if (self.check_bounds(rnx, rny)):
                self.cells[rnx][rny] = 2
                rx, ry = rnx, rny
                l -= 1

    # обработка изначального создания деревьев на карте
    def generate_forest(self, r, mxr):
        for ri in range(self.height):
            for ci in range(self.weight):
                if rand_bool(r, mxr):
                    self.cells[ri][ci] = 1

    # обработка создания новых деревьев
    def generate_tree(self):
        c = rand_cell(self.weight, self.height)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1

    # обработка создания магазина
    def generate_upgrade_shop(self):
        c = rand_cell(self.weight, self.height)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    # обработка создания госпиталя
    def generate_hospital(self):
        c = rand_cell(self.weight, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 3:
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()

    # обработка создания огня
    def add_fire(self):
        c = rand_cell(self.weight, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    # обработка обновления огня
    def update_fires(self):
        for ri in range(self.height):
            for ci in range(self.weight):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(5):
            self.add_fire()

    # обработка механик вертолета
    def process_copter(self, copter, clouds):
        c = self.cells[copter.x][copter.y]
        d = clouds.cells[copter.x][copter.y]
        if c == 2:
            copter.tank = copter.maxtank
        if (c == 5 and copter.tank > 0):
            copter.tank -= 1
            copter.score += TREE_BONUS
            self.cells[copter.x][copter.y] = 1
        if (c == 4 and copter.score >= UPGRADE_COST):
            copter.maxtank += 1
            copter.score -= UPGRADE_COST
        if (c == 3 and copter.score >= UPGRADE_COST):
            copter.lives += 10
            copter.score -= LIVE_COST
        if (d == 2):
            copter.lives -= 1
            if copter.lives == 0:
                copter.game_over()

    def export_data(self):
        return {'cells': self.cells}

    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.weight)] for j in range(self.height)]
