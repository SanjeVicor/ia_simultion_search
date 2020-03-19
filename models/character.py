
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QSizePolicy


class Character(object):
    def __init__(self,lbl_idx=None):
        self.path = '/home/c0d3br34k3r/proyectos/proyectoIA1/project/characters/mario.png'
        #self.character_lbl = None
        self.label_index = lbl_idx
        self.row = 0
        self.column = None
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

    def get_path(self):
        return self.path

    def set_label_idx(self, idx):
        self.label_index = idx

    def get_label_idx(self):
        return self.label_index

    def create_lbl(self):
        character_lbl = QLabel()
        character_lbl.setPixmap(QPixmap(self.path))
        character_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
        character_lbl.setScaledContents(True)
        return character_lbl