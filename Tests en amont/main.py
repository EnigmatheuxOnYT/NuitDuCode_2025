# Projet NDC
# Réalisé par Studio ...

import pyxel

BLOCK_SIDE = 8#px

class Main:
    def __init__(self):
        pyxel.init(width=256, height=256, title="Projet NDC", fps=60, quit_key=pyxel.KEY_Q,)
        self.x=0
        pyxel.load('1.pyxres')
        self.placeholderblock = Block('Placeholder',(0,0))

    
    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        #pyxel.rect(self.x,0,8,8,9)
        self.placeholderblock.blits((0,0),6)

    def run(self):pyxel.run(self.update,self.draw)

class Block:
    def __init__(self,name,pos,colkey=None):
        self.name = name
        self.pos = pos
        self.colkey = colkey
    
    def blit(self,pos):
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