import pyxel as px

class Main:
    def __init__(self):
        pass

    def update (self):
        pass

    def draw (self):
        pass

    def run (self):
        px.init(256,256,title="Nom",fps=60,quit_key=px.KEY_Q)
        px.run(self.update,self.draw)
        px.quit()

if __name__ == "__main__":
    Jeu = Main()
    Jeu.run()