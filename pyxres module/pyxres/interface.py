import pyxel

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
        #print(data)
        #print(self.images)
        #print(self.tilemaps)
        #print(self.save_data())
        #print(data==self.save_data())
        pyxel.init(INTERFACE_WIDTH,INTERFACE_HEIGHT,title="Better pyxres editor",fps=FPS,quit_key=pyxel.KEY_Q)
        pyxel.mouse(True)

    
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
        self.saved_data = data
        self.images = self.extract_images_colors(data['images'])
        self.tilemaps = self.extract_tilemaps_dirs(data['tilemaps'])
    
    def extract_images_colors(self,imageslist:list):
        images = [ [ [] for row in range(image['height']) ] for image in imageslist]
        for imageno in range(len(imageslist)):
            data = imageslist[imageno]['data']
            for rowno in range(len(data)):
                row = data[rowno]
                for cellno in range(len(row)-1):
                    images[imageno][rowno].append(row[cellno])
        return images

    def extract_tilemaps_dirs(self,tilemapslist:list):
        tilemaps = [ [ [] for row in range(tilemap['height']//8)] for tilemap in tilemapslist]
        for tmapno in range(len(tilemapslist)):
            data = tilemapslist[tmapno]['data']
            for rowno in range(len(data)):
                row = data[rowno]
                for blockno in range(len(row)//2):
                    tilemaps[tmapno][rowno].append((row[2*blockno],row[2*blockno+1]))
        return tilemaps
    
    def get_pyxres_format (self):
        images_data = [ [] for image in range(len(self.images))]
        tilemaps_data = [ [] for image in range(len(self.tilemaps))]
        for imageno in range(len(self.images)):
            modedimage = self.images[imageno]
            for rowno in range(len(modedimage)):
                row = modedimage[rowno]
                if row != []:
                    images_data[imageno].append(row+[0])
            images_data[imageno].append([0])
        for tmno in range(len(self.tilemaps)):
            modedtm = self.tilemaps[tmno]
            for rowno in range(len(modedtm)):
                modedrow = modedtm[rowno]
                if modedrow != []:
                    row = []
                    for blockno in range(len(modedrow)):
                        row.append(modedrow[blockno][0])
                        row.append(modedrow[blockno][1])
                    tilemaps_data[tmno].append(row+[0])
            tilemaps_data[imageno].append([0])
        return images_data,tilemaps_data
    
    def save_data(self):
        saved_data = self.saved_data
        images_data,tilemaps_data = self.get_pyxres_format()
        for imgaeno in range(len(images_data)):
            saved_data['images'][imgaeno]['data'] = images_data[imgaeno]
        for tmno in range(len(tilemaps_data)):
            saved_data['tilemaps'][tmno]['data'] = tilemaps_data[tmno]
        return saved_data

    
    def handle_input(self):pass
    
    def update(self):
        self.handle_input()

    def draw(self):
        pyxel.cls(0)


    def run(self):
        pyxel.run(self.update,self.draw)
        return self.saved_data
    
    def check_tiles():pass
