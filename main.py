# Projet NDC
# Réalisé par Studio ...

import pyxel

class Main:
    def __init__(self):
        pyxel.init(width=256, height=256, title="Projet NDC", fps=60, quit_key=pyxel.KEY_Q,)
    
    def update(self):pass
    def draw(self):pass
    def run(self):pyxel.run(self.update,self.draw)

if __name__ == '__main__':
    game = Main()
    game.run()