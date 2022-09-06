from utilis import randcel
class Helicopter:
    def __init__(self, w, h):
        rc=randcel(w,h)
        rx, ry=rc[0], rc[1]
        self.x=rx
        self.y=ry
        self.h=h
        self.w=w
        self.tenk=0
        self.mxtenk=1
        self.score=0

    
    
    def move (self, dx, dy):
        
        nx=dx+self.x
        ny=dy+self.y    
        if (nx>=0 and ny>=0 and nx<self.h and ny< self.w):
             self.x,self.y = nx,ny

    def print_meny(self):
        print("🪣 ", self.tenk, "/", self.mxtenk, sep="", end=" | ")
        print('🏆 ', self.score)