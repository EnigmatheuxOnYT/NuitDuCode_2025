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
        return (self.x+self.width>entity.x and self.x<entity.x+entity.width and self.y+self.height>entity.y and self.y<entity.y+entity.height)


class Player(Entity):
    dead=False
    def __init__(self):
        self.width,self.height = 16,32
        sprite = Sprite(0,0,0,self.width,self.height)
        super().__init__(128,224,16,32,10,sprite)
        self.speed = 2
    
    def move(self,modx,mody):
        self.x+=modx
        self.y+=mody
        if self.x>240:
            self.x=240
        elif self.x<0:
            self.x=0
        if self.y>224:
            self.y=224
        elif self.y<0:
            self.y=0
    
    def update(self):
        for ennemy in Ennemy.instances:
            if self.check_collision(ennemy):
                self.damage(1)
                ennemy.destroy()
        for bullet in Bullet.instances:
            if (not bullet.friendly) and self.check_collision(bullet):
                self.damage(1)
                bullet.destroy()
        for obstacle in Obstacle.instances:
            if self.check_collision(obstacle):
                self.damage(1)
                obstacle.destroy()
    
    def damage(self,amount):
        self.pv-=amount
        if self.pv<=0:
            Player.dead=True
            Explosion(self.x,self.y)
            print("Défaite... Votre score est : ",Ennemy.killed)
            px.quit()


class EnnemyType:
    instances = []
    def __init__(self,maxpv,dmg,speed,behaviour,spritepos):
        self.maxpv,self.dmg,self.speed,self.behaviour = maxpv,dmg,speed,behaviour
        self.sprite = Sprite(0,spritepos[0],spritepos[1])
        EnnemyType.instances.append(self)

EnnemyType(2,2,2,0,(16,0))
EnnemyType(3,2,1,0,(32,0))
EnnemyType(1,3,3,0,(48,0))

class Ennemy(Entity):
    instances = []
    killed = 0
    y = -20
    speedmod = 0
    def __init__ (self,type:int,startx:tuple,resetround:bool=False):
        if resetround:
            Ennemy.y = -20
        else:
            Ennemy.y -= 70
        self.typeno = type
        self.type:EnnemyType = EnnemyType.instances[type-1]
        super().__init__(startx,Ennemy.y,16,16,self.type.maxpv,self.type.sprite)
        self.speed = self.type.speed
    
    def damage (self,damage):
        self.pv-=damage
        if self.pv<=0:
            self.destroy()
    
    def destroy(self):
        Ennemy.instances.remove(self)
        Ennemy.killed+=1
        Explosion(self.x,self.y)
    
    def update(self):
        self.move(0,self.speed+Ennemy.speedmod)
        for bullet in Bullet.instances:
            if bullet.friendly and self.check_collision(bullet):
                self.damage(1)
                bullet.destroy()
                break
        if self.y>256:
            Ennemy.instances.remove(self)
        if self.y>0 and px.rndi(0,200) == 0:
            Bullet(False,(self.x+(self.width//2)-4,self.y+self.height))

class ObstacleType:
    instances = []
    def __init__(self,spritepos):
        self.sprite = Sprite(0,spritepos[0],spritepos[1])
        ObstacleType.instances.append(self)
    
ObstacleType((0,48))
ObstacleType((0,64))

class Obstacle(Entity):
    instances = []
    y = -20
    def __init__ (self,type:int,startx:tuple):
        self.typeno = type
        self.type:ObstacleType = ObstacleType.instances[type-1]
        super().__init__(startx,Obstacle.y,16,16,1,self.type.sprite)
        Obstacle.instances.append(self)
        if Obstacle.y>-8000:
            Obstacle.y-=80
    
    def destroy(self):
        Obstacle.instances.remove(self)
    
    def update(self):
        self.move(0,1)
        if self.y>256:
            Obstacle.instances.remove(self)
            Obstacle(px.rndi(0,1),px.rndi(0,240))

class Bullet(Entity):
    instances = []
    speed = 3
    def __init__(self,friendly,pos):
        self.friendly = friendly
        sprite = Sprite(0,8,32,8,8)
        super().__init__(pos[0],pos[1],8,8,1,sprite)
        Bullet.instances.append(self)
    
    def update (self):
        if self.friendly:
            self.y-=Bullet.speed
        else:
            self.y+=Bullet.speed
        if self.y>256 or self.y<-8:
            self.destroy()
    
    def destroy (self):
        Bullet.instances.remove(self)

class Explosion:
    instances = []
    DELAY = 3
    def __init__(self,x,y):
        self.x,self.y = x,y
        self.index = 0
        self.delay = 0
        Explosion.instances.append(self)
    
    def update(self):
        if self.delay == Explosion.DELAY:
            self.delay = 0
            if self.index >=5:
                Explosion.instances.remove(self)
            else:
                self.index+=1
        else:
            self.delay+=1
        
    def draw(self):
        px.blt(self.x,self.y,1,self.index*16,16,16,16,0)

vague1 = [Ennemy(px.rndi(1,3),px.rndi(0,240)) for _ in range(15)]+[Ennemy(px.rndi(1,3),px.rndi(0,240),True)]
vague2 = [Ennemy(px.rndi(1,3),px.rndi(0,240)) for _ in range(30)]+[Ennemy(px.rndi(1,3),px.rndi(0,240),True)]
vague3 = [Ennemy(px.rndi(1,3),px.rndi(0,240)) for _ in range(45)]+[Ennemy(px.rndi(1,3),px.rndi(0,240),True)]
vague4 = [Ennemy(px.rndi(1,3),px.rndi(0,240)) for _ in range(120)]+[Ennemy(px.rndi(1,3),px.rndi(0,240),True)]
vagues = [None,vague1,vague2,vague3,vague4]

obstacles = [Obstacle(px.rndi(0,1),px.rndi(0,240)) for _ in range(50)]

class Main:
    def __init__(self):
        self.player = Player()
        self.ennemytypes = EnnemyType.instances
        self.vagueno = 1
        Ennemy.instances = self.current_vague
    
    @property
    def current_vague(self):return vagues[self.vagueno]

    def next_vague(self):
        if self.vagueno < len(vagues)-1:
            self.vagueno +=1
            Ennemy.instances = self.current_vague
            Ennemy.speedmod+=1
            Bullet.speed +=1
            self.player.pv+=5
        else:
            print("Victoire ! Votre score est : "+str(Ennemy.killed+self.player.pv))
            px.quit()
    
    def intro(self):
        px.cls(0)
        px.text(50,100,"Pixare Games presents",7)
    
    def intro2 (self):
        px.text(50,150,"Pixel Armada",7)

    
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
            Bullet(True,(self.player.x+4,self.player.y-8))


    def update (self):
        if px.frame_count>=400:
            self.update_waves()
            self.handle_input()
            self.player.update()
            for ennemy in Ennemy.instances:
                ennemy.update()
            for bullet in Bullet.instances:
                bullet.update()
            for explosion in Explosion.instances:
                explosion.update()
            for obstacle in Obstacle.instances:
                obstacle.update()
            if len(Ennemy.instances) == 0:
                self.next_vague()
    
    def init_waves(self):
        self.waves = []
        for i in range(17):
            self.waves.append([])
            for j in range(16):
                wavex = px.rndi(0,2)*16
                self.waves[i].append(wavex)
        self.wave_offset=0
    
    def update_waves(self):
        self.wave_offset+=1
        if self.wave_offset>=16:
            self.wave_offset-=16
            self.waves.pop()
            newrow=[]
            for i in range(16):
                newrow.append(px.rndi(0,2)*16)
            self.waves.insert(0,newrow)

    
    def draw_waves(self):
        for i in range(17):
            for j in range(16):
                px.blt(j*16,((i*16)+self.wave_offset-16),1,self.waves[i][j],0,16,16)
   
    def draw (self):
        if px.frame_count<200:
            self.intro()
        elif px.frame_count<400:
            self.intro2()
        else:
            self.draw_waves()
            for bullet in Bullet.instances:
                bullet.draw()
            for obstacle in Obstacle.instances:
                obstacle.draw()
            for ennemy in Ennemy.instances:
                ennemy.draw()
            for explosion in Explosion.instances:
                explosion.draw()
            self.player.draw()
            px.text(5,5,"Vies : "+str(self.player.pv),0)
            px.text(50,5,"Score : "+str(Ennemy.killed),0)
            px.text(100,5,"Vague : "+str(self.vagueno),0)


    def run (self):
        px.init(256,256,title="Pixel Armada",fps=60,quit_key=px.KEY_ESCAPE)
        px.load("theme.pyxres")
        self.init_waves()
        px.run(self.update,self.draw)
        px.quit()

if __name__ == "__main__":
    Jeu = Main()
    Jeu.run()