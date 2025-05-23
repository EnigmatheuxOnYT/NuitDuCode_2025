import pyxel as px

class Sprite:
    def __init__(self,img,x,y,w=16,h=16,colkey=2):
        self.img,self.x,self.y,self.width,self.height,self.colkey = img,x,y,w,h,colkey
    
    def draw(self,x,y):
        px.blt(x,y,self.img,self.x,self.y,self.width,self.height,self.colkey,)

class Player:
    def __init__(self):
        self.x,self.y=128,256
        self.pos = (self.x,self.y)
        self.maxpv = 5
        self.pv = 5
        self.spritepos = (0,0,0)
        self.spritesize = (16,16)
    
    def draw(self):
        px.bltm()

class Main:
    def __init__(self):
        self.vague = 0
    
    def handle_input(self):
        pass

    def update (self):
        self.handle_input()

    def draw (self):
        px.cls(0)

    def run (self):
        px.init(256,256,title="Nom",fps=60,quit_key=px.KEY_Q)
        px.load("theme.pyxres")
        px.run(self.update,self.draw)
        px.quit()

if __name__ == "__main__":
    Jeu = Main()
    Jeu.run()