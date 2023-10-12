from utils import rand_bool

class Clouds:

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.cells = [[0 for i in range(weight)] for j in range(height)]

    # обработка обнавления облаков и гроз на карте
    def update_clouds(self, r=1, mxr=10, g=1, mxg=30):
        for i in range(self.height):
            for j in range(self.weight):
                if rand_bool(r, mxr):
                    self.cells[i][j] = 1
                    if rand_bool(g, mxg):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0

    def export_data(self):
        return {'cells': self.cells}

    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.weight)] for j in range(self.height)]
