import sys
import re
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from views.config_simulation import Ui_MainWindow 

from models.map import Map
from models.character import Character
from models.goal import Goal

class SimulationConfiguration(QMainWindow, Ui_MainWindow):
    def __init__(self,Map):
        super(SimulationConfiguration, self).__init__()
        self.setupUi(self)

        self.Map = Map
        self.graph = Map.get_graph()

        self.load_coords()
        self.load_map()

        #idx = (len(self.graph[0]) * len(self.graph)) + len(self.graph)
        idx = self.mapGrd.count()
        self.character = Character(idx)

        idx = self.mapGrd.count() + 1 
        self.goal = Goal(lbl_idx=idx)

        self.load_character_lbl()
        self.load_character_errors()
        self.load_character_textline()

        self.load_goal_lbl()
        self.load_goal_errors()
        self.load_goal_textline() 

        self.adjust_sizes(None,None)

        self.load_accept_btn()

        self.show()

#-------
#DRAG AND DROP OBJECTS (TESTING)
#-------

    class dragableLbl(QLabel):
        def __init__(self,image):
            super().__init__(None)
            self.image = image
        
        def mousePressEvent(self,e):
            print(e)
            if e.button() == Qt.LeftButton:
                self.drag_start_position = e.pos()
        
        def mouseMoveEvent(self,e):
            if not(e.buttons() & Qt.LeftButton):
                return
            else:
                drag = QDrag(self)
    
                mimedata = QMimeData()
                mimedata.setImageData(self.image)
    
                drag.setMimeData(mimedata)
    
                pixmap = QPixmap(self.size())
    
                painter = QPainter(pixmap)
                painter.drawPixmap(self.rect(), self.grab())
                painter.end()
    
                drag.setPixmap(pixmap)
                drag.setHotSpot(e.pos())
                drag.exec_(Qt.CopyAction | Qt.MoveAction)

    class lbl2(QLabel):
        def __init__(self):
            super().__init__()
            self.setAcceptDrops(True)
 
        def dragEnterEvent(self, event):
            if event.mimeData().hasImage():
                event.acceptProposedAction()
                print(event.mimeData().imageData())
    
        def dropEvent(self, event):
            pos = event.pos()
            text = event.mimeData().text()
            self.setText(text)
            event.acceptProposedAction()

#-------
#Map
#-------

    def load_coords(self):
        total_row = len(self.graph)
        total_column = len(self.graph[0])
        for i in range(total_column+1): 
            if i == 0:
                data = " "
            else:
                data = chr(64+i)
            row_lbl =  QLabel()
            
            row_lbl.setFixedSize(40,40)
            row_lbl.setText(data)
            row_lbl.setAlignment(Qt.AlignCenter) 
            self.XGrd.addWidget(row_lbl,0,i)

    def load_map(self):
        last_height = 0
        last_width = 0
        for i in range(len(self.graph)):
            row = self.graph[i] 
            data = str(i+1)
            node_lbl = QLabel() 
            node_lbl.setAlignment(Qt.AlignCenter)
            node_lbl.setFixedSize(40,40)
            node_lbl.setText(data)
            self.mapGrd.addWidget(node_lbl,i,0)
            for j in range(len(row)):
                node = row[j] 
                node_lbl = QLabel() 
                if node.get_image() != None:
                    data = node.get_image()
                    node_lbl.setPixmap(QPixmap(data))
                    node_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
                    node_lbl.setScaledContents(True) 
                    self.mapGrd.addWidget(node_lbl,i,j+1)
                    last_height = node_lbl.height()
                    last_width = node_lbl.width()

#----------
#Utils
#----------

    def valid_coord(self,coords):
        coord_reg_ex = r"(\s*[1-9][0-9]*\s*\x2c\s*[a-zA-Z]*\s*)"
        if re.fullmatch(coord_reg_ex,coords):
            coords = coords.replace(" ","")
            coords = coords.replace('\n',"")
            coords = coords.replace('\r',"") 
            coords = coords.split(',')
            print(coords[1].upper())
            coords[1] = ord(coords[1].upper()) - 64
            coords[0] = int(coords[0]) - 1
            if self.valid_ranges(coords[0], coords[1]):
                return True, coords
        return False, None

    def valid_ranges(self,row,column):
        if row < 0 or column < 0:
            return False
        if row <= len(self.graph[0]) and column <= len(self.graph):
            return True
        return False

    def adjust_sizes(self,height,width):
        self.characterLbl.setFixedSize(40,40) 
        self.goalLbl.setFixedSize(40,40)

    def enable_change_btn(self):
        c_pos1, c_pos2 = self.character.get_last_position()
        g_pos1, g_pos2 = self.goal.get_last_position()
        if c_pos1 != None and c_pos2 != None  and g_pos1  != None and g_pos2 != None :
            self.accept_btn.setEnabled(True)

#-------
#Goal
#-------
    def load_goal_lbl(self):
        self.goalLbl = self.dragableLbl(self.goal.get_path())
        self.goalLbl.setPixmap(QPixmap(self.goal.get_path()))
        self.goalLbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
        self.goalLbl.setScaledContents(True) 
        self.contentVLayout.addWidget(self.goalLbl)        

    def load_goal_textline(self):
        self.goalTxt = QLineEdit()
        self.goalTxt.setEnabled(True)
        self.goalTxt.setMaximumSize(QSize(370, 30))
        self.contentVLayout.addWidget(self.goalTxt)

        self.goalTxt.textChanged.connect(self.goal_changed_textLine)
    
    def load_goal_errors(self):
        self.error_goal_exist_coord_lbl = QLabel("Coordenada inexistente")
        self.error_goal_exist_coord_lbl.setVisible(False)
        self.contentVLayout.addWidget(self.error_goal_exist_coord_lbl)
    
        self.error_goal_invalid_coord_lbl = QLabel("Coordenada invalida para el personaje")
        self.error_goal_invalid_coord_lbl.setVisible(False)
        self.contentVLayout.addWidget(self.error_goal_invalid_coord_lbl)

    def goal_changed_textLine(self):
        coords = self.goalTxt.text() 
        ok, coords = self.valid_coord(coords)
        if ok:
            self.error_goal_exist_coord_lbl.setVisible(False)
            
            if self.mapGrd.itemAt(self.goal.get_label_idx()) != None:
                self.delete_position_goal()

            self.load_goal(coords[0], coords[1])
        else:
            self.error_goal_exist_coord_lbl.setVisible(True)

    def load_goal(self,x,y):
        old_lbl = self.mapGrd.itemAtPosition(x,y)
        old_lbl = old_lbl.widget()
        self.mapGrd.addWidget(self.goal.create_lbl(),x,y) 
        self.goal.set_last_position(x,y-1)
        print("posiciones de la meta : ", self.goal.get_last_position())
        self.enable_change_btn()

    def delete_position_goal(self):
        old_lbl = self.mapGrd.itemAt(self.goal.get_label_idx())
        old_lbl = self.mapGrd.indexOf(old_lbl)
        old_lbl = self.mapGrd.takeAt(old_lbl) 
        old_lbl.widget().deleteLater()

#----------
#Character
#---------- 
    def load_character_lbl(self):
        self.characterLbl = self.dragableLbl(self.character.get_path())
        self.characterLbl.setPixmap(QPixmap(self.character.get_path()))
        self.characterLbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
        self.characterLbl.setScaledContents(True) 
        self.contentVLayout.addWidget(self.characterLbl)
        """        
        self.x = self.lbl2()
        self.x.setText("ddss")
        self.contentVLayout.addWidget(self.x)
        """

    def load_character_textline(self):
        self.characterTxt = QLineEdit()
        self.characterTxt.setEnabled(True)
        self.characterTxt.setMaximumSize(QSize(370, 30))
        self.contentVLayout.addWidget(self.characterTxt)

        self.characterTxt.textChanged.connect(self.character_changed_textLine)
    
    def load_character_errors(self):
        self.error_exist_coord_lbl = QLabel("Coordenada inexistente")
        self.error_exist_coord_lbl.setVisible(False)
        self.contentVLayout.addWidget(self.error_exist_coord_lbl)
    
        self.error_invalid_coord_lbl = QLabel("Coordenada invalida para el personaje")
        self.error_invalid_coord_lbl.setVisible(False)
        self.contentVLayout.addWidget(self.error_invalid_coord_lbl)

    def character_changed_textLine(self):
        coords = self.characterTxt.text() 
        ok, coords = self.valid_coord(coords)
        if ok:
            self.error_exist_coord_lbl.setVisible(False)
            
            if self.mapGrd.itemAt(self.character.get_label_idx()) != None:
                self.delete_position_character()

            self.load_character(coords[0], coords[1])
        else:
            self.error_exist_coord_lbl.setVisible(True)

    def load_character(self,x,y):
        old_lbl = self.mapGrd.itemAtPosition(x,y)
        old_lbl = old_lbl.widget()
        self.mapGrd.addWidget(self.character.create_lbl(),x,y) 
        self.character.set_last_position(x,y-1)
        print("posiciones del personaje : ", self.character.get_last_position())
        self.enable_change_btn()

    def delete_position_character(self):
        old_lbl = self.mapGrd.itemAt(self.character.get_label_idx())
        old_lbl = self.mapGrd.indexOf(old_lbl)
        old_lbl = self.mapGrd.takeAt(old_lbl) 
        old_lbl.widget().deleteLater()

#--------
# Accept Button
#------- 
    def load_accept_btn(self):
        self.accept_btn = QPushButton("Aceptar")
        self.accept_btn.setEnabled(False)
        self.accept_btn.clicked.connect(self.allow_change)

        self.contentVLayout.addWidget(self.accept_btn)

    def allow_change(self):
        from scripts.simulation import SimulationWindow
        g_pos1, g_pos2 = self.goal.get_last_position()
        self.Map.set_goal(g_pos1, g_pos2)
        self.simulation = SimulationWindow(self.Map,self.character, self.goal)
        self.close()