import pyxel as px

class Sprite:
    def __init__(self,img,x,y,w=16,h=16,colkey=2):
        self.img,self.x,self.y,self.width,self.height,self.colkey = img,x,y,w,h,colkey
    
    def draw(self,x,y):
        px.blt(x,y,self.img,self.x,self.y,self.width,self.height,self.colkey)

class Entity:
    def __init__(self,x:int,y:int,w:int,h:int,maxpv:int,sprite:Sprite):
        self.x,self.y=x,y
        self.width,self.height = w,h
        self.pv,self.maxpv = maxpv
        self.sprite = sprite
    
    @property
    def pos(self):return (self.x,self.y)
    @property
    def size(self):return (self.width,self.height)

    def move(self,modx,mody):
        self.x+=modx
        self.y+=mody
    
    def setpos (self,x,y):
        self.y,self.y = x,y

    def draw(self):
        self.sprite.draw(self.x,self.y)


class Player(Entity):
    def __init__(self):
        sprite = Sprite(0,0,0,self.width,self.height)
        super().__init__(128,256,16,32,5,sprite)

class Ennemi(Entity):
    instances = []
    def __init__ (self,maxpv,dmg,speed,sprite):
        super().__init__(0,0,16,16,maxpv,sprite)
        self.dmg = dmg
        self.speed = speed
        Ennemi.instances.append(self)
        self.id = len(Ennemi.instances)


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