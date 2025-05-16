# Projet NDC
# Réalisé par Studio ...

import pyxel

BLOCK_SIDE = 8#px
BLOCK_SIZE = (BLOCK_SIDE,BLOCK_SIDE)

class Main:
    def __init__(self):
        pyxel.init(width=256, height=256, title="Projet NDC", fps=60, quit_key=pyxel.KEY_Q)
        pyxel.mouse(True)
        self.x=0
        pyxel.load('../my_resource.pyxres')
        self.blocks = [Block(i,0) for i in range(16)]
        self.offset = 0

    
    def update(self):
        self.x = (self.x + 1) % pyxel.width
        self.offset+=1


    def draw(self):
        pyxel.cls(0)
        #pyxel.rect(self.x,0,8,8,9)
        #self.placeholderblock.blits((0,0),25)
        for y in range(pyxel.height//BLOCK_SIDE):
            for x in range(pyxel.width//BLOCK_SIDE):
                self.draw_block(9,(x*BLOCK_SIDE,y*BLOCK_SIDE))
        #self.testscreen()
    
    def draw_block(self,id:int,pos:tuple)->None:self.blocks[id].blit(pos)

    def testscreen(self):
        for i in range(len(self.blocks)):
            self.draw_block(i,self.blocks[i].pos)

    def run(self):pyxel.run(self.update,self.draw)


class Block:
    def __init__(self,id:int,colkey:int|None=None):
        self.id = id
        self.pos = ((id*BLOCK_SIDE)%256,(id*BLOCK_SIDE)//256)
        self.colkey = colkey
    
    def blit(self,pos:tuple):
        if self.colkey:
            pyxel.blt(pos[0],pos[1],0,self.pos[0],self.pos[1],BLOCK_SIDE,BLOCK_SIDE,self.colkey)
        else:
            pyxel.blt(pos[0],pos[1],0,self.pos[0],self.pos[1],BLOCK_SIDE,BLOCK_SIDE)

    def blits(self,pos,amount):
        for i in range(amount):
            self.blit((i*BLOCK_SIDE+pos[0],pos[1]))


class MapManager:
    def __init__(self):
        self.display_frame = (0,0)

if __name__ == '__main__':
    game = Main()
    game.run()