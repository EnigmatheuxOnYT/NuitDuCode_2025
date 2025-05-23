# Projet NDC
# Réalisé par Studio ...

import pyxel

TILE_SIDE = 8#px
TILE_SIZE = (TILE_SIDE,TILE_SIDE)

class Main:
    def __init__(self):
        pyxel.init(width=256, height=256, title="Projet NDC", fps=60, quit_key=pyxel.KEY_Q)
        pyxel.mouse(True)
        self.x=0
        pyxel.load('../my_resource.pyxres')
        self.tiles = [Tile(((i*TILE_SIDE)%256,(i*TILE_SIDE)//256),0) for i in range(16)]
        self.offset = 0

    
    def update(self):
        self.x = (self.x + 1) % pyxel.width
        self.offset+=1


    def draw(self):
        pyxel.cls(1)
        #pyxel.rect(self.x,0,8,8,9)
        #self.placeholderblock.blits((0,0),25)
        for y in range(pyxel.height//TILE_SIDE):
            for x in range(pyxel.width//TILE_SIDE):
                self.draw_tile(0,(x*TILE_SIDE,y*TILE_SIDE))
        #self.testscreen()
    
    def draw_tile(self,id:int,pos:tuple)->None:self.tiles[id].blit(pos)

    def testscreen(self):
        for i in range(len(self.tiles)):
            self.draw_tile(i,self.tiles[i].pos)

    def run(self):pyxel.run(self.update,self.draw)


class Tile:
    instances = []
    def __init__(self,pos,colkey:int|None=None):
        self.pos = pos
        self.colkey = colkey
        Tile.instances.append(self)
        self.id = len(Tile.instances)
    
    def blit(self,pos:tuple):
        if self.colkey!=None:
            pyxel.blt(pos[0],pos[1],0,self.pos[0],self.pos[1],TILE_SIDE,TILE_SIDE,self.colkey)
        else:
            pyxel.blt(pos[0],pos[1],0,self.pos[0],self.pos[1],TILE_SIDE,TILE_SIDE)

class Entity:
    instances = []
    def __init__(self,pos:tuple,size:tuple):
        self.pos = pos
        Entity.instances.append(self)
        self.id = len(Entity.instances)

class MapManager:
    def __init__(self):
        self.display_frame = (0,0)

if __name__ == '__main__':
    game = Main()
    game.run()
    #Tile((17,0))
    #print(Tile.instances[0].pos)
    pass