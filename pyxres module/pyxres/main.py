import zipfile
import toml
import os
from typing import Any
from interface import Interface

extracted_file_directory = "pyxres module/extractor/"
extracted_file_name = "pyxel_resource.toml"

class extractor:
    def extract_zip(file:str)->None:
        with zipfile.ZipFile(file, 'r') as archive:
            archive.extractall(extracted_file_directory)

    def extract_toml(file:str)->dict[str|Any]:
        with open(file, "r", encoding="utf-8") as f:
            data = toml.load(f)
        return data
    
    def extract_data(file:str)->dict[str|Any]:
        extractor.extract_zip(file)
        data = extractor.extract_toml(extracted_file_directory+extracted_file_name)
        #os.remove(self.extracted_file_directory)
        return data




class filebuilder:
    def save_toml(data:dict[str|Any],file:str)->None:
        with open(file, "w", encoding="utf-8") as f:
            toml.dump(data, f)

    def save_pyxres(file:str,original_file:str):
        with zipfile.ZipFile(original_file, 'w', zipfile.ZIP_DEFLATED) as archive:
            filepath = file
            arcname = os.path.relpath(filepath, "extrait")
            archive.write(filepath, arcname)
    
    def save_data(data:dict[str|Any],originalfile:str)->None:
        filebuilder.save_toml(data,extracted_file_directory+extracted_file_name)
        filebuilder.save_pyxres(extracted_file_directory+extracted_file_name,originalfile)


class pyxres:
    def __init__(self):
        self.extractor = extractor
        self.filebuilder = filebuilder
        self.extract_pyxres = self.extractor.extract_data
    
    def init_file(self,file:str):
        self.file = file
        self.data = self.extract_pyxres(file)
        self.interface = Interface(self.data)
    
    def set_tileset(self,tiles:list,hitboxes:list,entities:list):
        self.tiles = tiles
        self.hitboxes = hitboxes
        self.entities = entities
    
    def start(self):
        try:
            self.interface.load_tileset(self.tiles,self.hitboxes,self.entities)
        except:
            raise AttributeError("You have to execute the set_tileset function before starting modifs.")
        self.data = self.interface.run()
        self.filebuilder.save_data(self.data,self.file)
        

if __name__ == "__main__":
    file_name = "pyxres module/test1"
    file = f"{file_name}.pyxres"
    toml_file = f"pyxres/extractor/pyxel_resource.toml"
    Pyxres = pyxres()
    Pyxres.init_file(file)
    Pyxres.set_tileset([],[],[])
    Pyxres.start()
    #data = extractor.extract_data(file)
    #print(data['tilemaps'])
