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
        self.pv,self.maxpv = maxpv,maxpv
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
    
    def check_collision(self,entity):
        return (self.x+self.width>entity.x and self.x<entity.x+entity.width and self.y+self.width>entity.y and self.y<entity.y+entity.width)


class Player(Entity):
    def __init__(self):
        self.width,self.height = 16,32
        sprite = Sprite(0,0,0,self.width,self.height)
        super().__init__(128,224,16,32,5,sprite)
        self.speed = 2
    
    def move(self,modx,mody):
        self.x+=modx
        self.y+=mody
        if self.x>250:
            self.x=250
        elif self.x<0:
            self.x=0
        if self.y>224:
            self.y=224
        elif self.y<0:
            self.y = 0

class EnnemyType:
    instances = []
    def __init__(self,maxpv,dmg,speed,behaviour,spritepos):
        self.maxpv,self.dmg,self.speed,self.behaviour = maxpv,dmg,speed,behaviour
        self.sprite = Sprite(0,spritepos[0],spritepos[1])
        EnnemyType.instances.append(self)

EnnemyType(2,2,2,0,(16,0))
EnnemyType(3,1,1,0,(32,0))
EnnemyType(1,3,3,0,(48,0))

class Ennemy(Entity):
    instances = []
    def __init__ (self,type:int,startx:tuple):
        self.typeno = type
        self.type:EnnemyType = EnnemyType.instances[type-1]
        super().__init__(startx,0,16,16,self.type.maxpv,self.type.sprite)
        Ennemy.instances.append(self)
    
    def damage (self,damage):
        self.pv-=damage
        if self.pv<=0:
            self.destroy()
    
    def destroy(self):
        Ennemy.instances.remove(self)
    
    def update(self):
        self.move(self.speed,0)

class Bullet(Entity):
    instances = []
    def __init__(self,friendly,pos):
        self.friendly = friendly
        sprite = Sprite(0,0,32,8,8)
        super().__init__(0,32,8,8,1,sprite)
        Bullet.instances.append(self)
    
    def update (self):
        self.y-=3


vague1 = [Ennemy(1,128)]
vagues = [None,vague1]

class Main:
    def __init__(self):
        self.player = Player()
        self.ennemytypes = EnnemyType.instances
        self.vagueno = 1
    
    @property
    def current_vague(self):return vagues[self.vagueno]
    
    def start_wave(self):pass


    
    def handle_input(self):
        if px.btn(px.KEY_Z) or px.btn(px.KEY_UP):
            self.player.move(0,-self.player.speed)
        if px.btn(px.KEY_S) or px.btn(px.KEY_DOWN):
            self.player.move(0,self.player.speed)
        if px.btn(px.KEY_Q) or px.btn(px.KEY_LEFT):
            self.player.move(-self.player.speed,0)
        if px.btn(px.KEY_D) or px.btn(px.KEY_RIGHT):
            self.player.move(self.player.speed,0)
        if px.btnp(px.KEY_SPACE):
            print("E")


    def update (self):
        self.handle_input()
        for ennemy in Ennemy.instances:
            #print(ennemy.pos,self.player.pos)
            if self.player.check_collision(ennemy):
                print("1")
        for bullet in Bullet.instances:
            bullet.update()

    def draw (self):
        px.cls(6)
        self.player.draw()
        for ennemy in Ennemy.instances:
            ennemy.draw()

    def run (self):
        px.init(256,256,title="Nom",fps=60,quit_key=px.KEY_Q)
        px.load("theme.pyxres")
        px.run(self.update,self.draw)
        px.quit()

if __name__ == "__main__":
    Jeu = Main()
    Jeu.run()