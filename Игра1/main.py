from map import Map
from helicopter import Helicopter as Helico
import time
import os

from pynput import keyboard

TIME_SLEEP=0.05
TREE_UPDATE=50
FIRE_UPDATE=100    
MAP_W, MAP_H=20, 10

tmp=Map(MAP_W, MAP_H)
tmp.generate_forest(4,9)
tmp.generate_riwers(10)






helico=Helico(MAP_W, MAP_H)

MOVES={'w':(-1,0), 's':(1,0), 'a':(0,-1), 'd':(0,1)}
def on_release(key):
    global helico
    c=key.char.lower()
    if c in MOVES.keys():
        dx, dy= MOVES[c][0],MOVES[c][1]
        helico.move(dx,dy)
    # if key == keyboard.Key.esc:
    #     # Stop listener
    #     return False

     

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=None,
    on_release=on_release)
listener.start()


tick=1
while True:
    os.system("clear")
    print("TICK", tick )
    tmp.process_helicopter(helico)
    helico.print_meny()
    tmp.print_map(helico)
    tick+=1
    time.sleep(TIME_SLEEP)
    if (tick % TREE_UPDATE == 0):
        tmp.generate_tree
    if (tick % FIRE_UPDATE==0):
        tmp.update_fires()
