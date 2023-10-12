# 🌲🌊🛸🟩🔥🏥🧡💧🏬☁️⚡️⬛

from map import Map
from helicopter import Helicopter as Copter
from pynput import keyboard
from clouds import Clouds
import time
import os
import json

# константы
TICK_SLEEP = 0.5
TREE_UPDATE = 50
FIRE_UPDATE = 20
CLOUDS_UPDATE = 30
MAP_WEIGHT, MAP_HEIGHT = 20, 10
MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
# создание начальных парамтров игры
fields = Map(MAP_WEIGHT, MAP_HEIGHT)
clouds = Clouds(MAP_WEIGHT, MAP_HEIGHT)
copter = Copter(MAP_WEIGHT, MAP_HEIGHT)
tick = 1

def process_key(key):
    # обработка движения
    global copter, tick, clouds, fields
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        copter.move(dx, dy)
    # сохранение игры
    elif c == 'f':
        data = {'copter': copter.export_data(),
                'clouds': clouds.export_data(),
                'fields': fields.export_data(),
                'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
    # загрузка игры
    elif c == 'g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data["tick"] or 1
            copter.import_data(data["copter"])
            fields.import_data(data["fields"])
            clouds.import_data(data["clouds"])

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

# выполнение игры
while True:
    os.system('cls')
    fields.process_copter(copter, clouds)
    copter.print_stats()
    fields.print_map(copter, clouds)
    print('TICK', tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        fields.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        fields.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update_clouds()
