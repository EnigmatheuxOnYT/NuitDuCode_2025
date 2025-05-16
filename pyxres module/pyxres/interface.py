import pygame

INTERFACE_WIDTH = 1280
INTERFACE_HEIGHT = 720
INTERFACE_SIZE = (INTERFACE_WIDTH,INTERFACE_HEIGHT)
FPS = 60

class Interface:
    def __init__(self,data):
        self.handle_data(data)
        self.get_colors()
        self.get_rects()
        self.running = True
        self.screen = pygame.display.set_mode(INTERFACE_SIZE)
        pygame.display.set_caption("Better pyxres editor")

    
    def get_colors(self):
        self.colors = [(0,0,0),
                       (43,51,95),
                       (126,32,114),
                       (25,149,156),
                       (139,72,82),
                       (57,92,152),
                       (169,193,255),
                       (238,238,238),
                       (212,24,108),
                       (211,132,65),
                       (233,195,91),
                       (112,198,169),
                       (118,150,222),
                       (163,163,163),
                       (255,151,152),
                       (237,199,176)
                       ]
    
    def handle_data(self,data):
        self.data = data
        if self.data['format_version'] != 4:
            raise ValueError("pyxres format version must be 4. Update version with normal pyxel editor.")
        self.images = data['images']
        self.tilemaps = data['tilemaps']
        self.saved_data = data
    
    def extract_images_colors(self,imageslist:list):
        images = []
        for i in range(2):
            tiles = []
            line = 0
            char = 0
            while line<=7:
                colorline = []
                if len(imageslist[i]['data'])>=line:
                    while char <=7:
                        if len(imageslist[i]['data'][line]) >= char:
                            color = self.colors[imageslist[i]['data'][line][char]]
                            colorline.append(color)
                        else:
                            colorline.append(self.colors[0])
                        char+=1
                else:
                    colorline = [self.colors[0] for _ in range(8)]
                tiles.append(colorline)
                line+=1
            images.append(tiles)



    
    def get_rects(self):
        self.window_tilemap_rect = pygame.Rect(50,50,512,512)
        self.window_tilemap_surf = pygame.Surface((512,512))
        self.window_tilemap_surf.fill("black")
        self.window_image_rect = pygame.Rect(600,50,64,64)
        self.window_image_surf = pygame.Surface((256,256))
        self.window_image_surf.fill("black")
    
    def save_data(self):
        self.saved_data = self.data
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):pass

    def draw(self):
        self.screen.fill((25,25,25))
        self.screen.blit(self.window_tilemap_surf,self.window_tilemap_rect)
        self.screen.blit(self.window_image_surf,self.window_image_rect)
        pygame.display.flip()


    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            pygame.time.Clock().tick(FPS)
        pygame.quit()
        return self.data
    
    def check_tiles():pass
