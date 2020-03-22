
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QSizePolicy

from extra_images.load import get_initial_image

class Initial_point(object):
    def __init__(self,lbl_idx=None):
        self.path = get_initial_image()
        print("PATH INITIAL ", self.path )
        self.label_index = lbl_idx
        self.row = None
        self.column = None
    
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
        goal_lbl = QLabel()
        goal_lbl.setPixmap(QPixmap(self.path))
        goal_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
        goal_lbl.setScaledContents(True)
        return goal_lbl
