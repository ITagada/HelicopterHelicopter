from random import randint as rand
# генерация рандомного булевого значения
def rand_bool(r, mxr):
    t = rand(0, mxr)
    return (t <= r)
# генерация рандомной клетки
def rand_cell(w, h):
    tw = rand(0, w - 1)
    th = rand(0, h - 1)
    return (th, tw)
# генерация рандомной последовательности связанных клеток
def rand_next_cell(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)