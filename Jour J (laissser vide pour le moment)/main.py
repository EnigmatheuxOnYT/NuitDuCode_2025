import pyxel as px

class Sprite:
    def __init__(self,img,x,y,w=16,h=16,colkey=6):
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

class EnnemyType:
    instances = []
    def __init__(self,maxpv,dmg,speed,behaviour,spritepos):
        self.maxpv,self.dmg,self.speed,self.behaviour = maxpv,dmg,speed,behaviour
        self.sprite = Sprite(0,spritepos[0],spritepos[1])
        EnnemyType.instances.append(self)

EnnemyType(2,2,2,(0,16))
EnnemyType(3,1,1,(0,32))
EnnemyType(1,3,3,(0,48))

class Ennemy(Entity):
    instances = []
    def __init__ (self,type:int,startx:tuple):
        self.typeno = type
        self.type:EnnemyType = EnnemyType.instances[type-1]
        super().__init__(startx,0,16,16,self.type.maxpv,self.type.sprite)

vague1 = [Ennemy(2,128)]

class Main:
    def __init__(self):
        self.player = Player()
        self.ennemytypes = EnnemyType.instances
        self.vague = 1
    
    def handle_input(self):
        pass

    def update (self):
        self.handle_input()

    def draw (self):
        px.cls(6)
        self.player.draw()
        for ennemy in self.ennemies:
            ennemy.draw()

    def run (self):
        px.init(256,256,title="Nom",fps=60,quit_key=px.KEY_Q)
        px.load("theme.pyxres")
        px.run(self.update,self.draw)
        px.quit()

if __name__ == "__main__":
    Jeu = Main()
    Jeu.run()