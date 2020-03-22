
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QPushButton
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QSizePolicy

from models.map import Map

import copy

class Character(object):
    def __init__(self,lbl_idx=None, Map=None, name=""):
        #self.path = '/home/c0d3br34k3r/proyectos/proyectoIA1/project/characters/mario.png'
        self.path = None
        #self.character_lbl = None
        self.label_index = lbl_idx
        self.row = 0
        self.column = None
        self.visits = 0
        self.name = name.upper()
        self.Map = copy.deepcopy(Map)
    
    def make_new_copy_of_map(self,m):
        self.Map = copy.deepcopy(m)

    def get_map(self):
        return self.Map

    def set_name(self,n):
        self.name = n
    
    def get_name(self):
        return self.name

    def clear_visits(self):
        self.visits = 0

    def set_new_visit(self):
        self.visits+=1

    def get_visits(self):
        return self.visits
        
    def set_last_position(self,row,column):
        self.row  = row
        self.column = column

    def get_last_position(self):
        return self.row,self.column

    def set_path(self,p):
        self.path = p

    def get_path(self):
        return self.path

    def set_label_idx(self, idx):
        self.label_index = idx

    def get_label_idx(self):
        return self.label_index

    def clear_lands(self):
        self.Map.clear_available_lands()

    def create_lbl(self):
        character_lbl = QLabel()
        character_lbl.setPixmap(QPixmap(self.path))
        character_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
        character_lbl.setScaledContents(True)
        return character_lbl

    def is_configuration_complete(self):
        print(self.Map.is_complete_configuration())
        print(self.path)
        if self.Map.is_complete_configuration():
            if self.path != None:
                return True
        return False