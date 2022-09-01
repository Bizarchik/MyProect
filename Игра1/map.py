from utilis import randbool
from utilis import randcel2
from utilis import randcel
#0-Поле
#1-дерево
# 2-волна
# 3-госпиталь
# 4-апгрейд-шоп


CELL_TYPE="🟩🌲🌊🏥🚉🔥"


class Map:
    
    def __init__(self, w, h):  
        self.w=w
        self.h=h  
        self.cells=[[0 for i in range(w)] for j in range(h)]
        
    def check_bounds(self, x, y):
        if (x<0 or y<0 or x>=self.h or y>=self.w):
            return False
        return True
    
    
    def print_map(self, helico):
        print("⬛" * (self.w + 2))
        for ri in range(self.h):
            print("⬛", end="")
            for ci in range(self.w):
                cell=self.cells[ri][ci]
                if (helico.x==ri and helico.y==ci):
                    print("🚁", end="")
                elif (cell>=0 and cell<len(CELL_TYPE)):
                    print(CELL_TYPE[cell], end="")
            print("⬛")    
        print("⬛" * (self.w + 2)) 
        
    
    def generate_riwers(self, l):
        rc=randcel(self.w, self.h)
        rx, ry=rc[0], rc[1]
        self.cells[ry][rx]=2
        while l>0:
            rc2=randcel2(rx,ry)
            rx2, ry2=rc2[0],rc2[1]
            if (self.check_bounds(rx2,ry2)):
                self.cells[rx2][ry2]=2
                rx,ry=rx2,ry2
                l-=1 
        
    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci]=1
                    
                    
    def generate_tree(self):
        c=randcel(self.w, self.h)
        cx, cy=c[0], c[1]
        if (self.cells[cx][cy]==0):
            self.cells[cx][cy]=1
            
        
    def add_fire(self):
        c=randcel(self.w, self.h)
        cx, cy=c[0], c[1]
        if self.cells[cy][cx]==1:# ошибка была тут в лекции if self.cells [cx][cy]
            self.cells[cy][cx]=5 # ошибка была тут в лекции if self.cells [cx][cy]
        
       
    
    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell=self.cells[ri][ci]
                if cell==5:
                    self.cells[ri][ci]=0  
            for i in range(5):
                
                self.add_fire()
                                      
    
                      
             
                        
         
        

