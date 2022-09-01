from map import Map
from helicopter import Helicopter as Helico
import time
import os

TIME_SLEEP=0.05
TREE_UPDATE=50
FIRE_UPDATE=100
MAP_W, MAP_H=20, 10

tmp=Map(MAP_W, MAP_H)
tmp.generate_forest(4,9)
tmp.generate_riwers(10)




helico=Helico(MAP_W, MAP_H)

tick=1
while True:
    os.system("clear")
    print("TICK", tick )
    tmp.print_map(helico)
    tick+=1
    time.sleep(TIME_SLEEP)
    if (tick % TREE_UPDATE == 0):
        tmp.generate_tree
    if (tick % FIRE_UPDATE==0):
        tmp.update_fires()
    