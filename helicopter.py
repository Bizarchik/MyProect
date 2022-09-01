from utilis import randcel
class Helicopter:
    def __init__(self, w, h):
        rc=randcel(w,h)
        rx, ry=rc[0], rc[1]
        self.x=rx
        self.y=ry
        
    