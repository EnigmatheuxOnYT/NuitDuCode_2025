# Projet NDC
# Réalisé par Studio ...

import pyxel

class Main:
    def __init__(self):
        pyxel.init(width=256, height=256, title="Projet NDC", fps=60, quit_key=pyxel.KEY_Q,)
        self.x=0

    
    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x,0,8,8,9)

    def run(self):pyxel.run(self.update,self.draw)

if __name__ == '__main__':
    game = Main()
    game.run()