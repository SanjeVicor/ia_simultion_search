import sys
import re

from functools import partial

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from views.config_simulation import Ui_MainWindow 

from models.map import Map
from models.character import Character
from models.goal import Goal

from views.simulations import Ui_Dialog
from views.priority import Ui_Dialog as Priority_Dialog

from extra_images.load import get_down_key,get_left_key,get_right_key,get_up_key

class SimulationConfiguration(QMainWindow, Ui_MainWindow):
    def __init__(self,character):
        super(SimulationConfiguration, self).__init__()
        self.setupUi(self)
        
        self.character = character
        self.Map = self.character.get_map()
        self.graph = self.Map.get_graph()

        self.load_coords()
        self.load_map()
 
        self.character.set_label_idx(None)
        self.load_character_lbl()
        self.load_character_errors()
        self.load_character_textline()
 
        self.goal = Goal(lbl_idx=None)
         
        self.load_goal_lbl()
        self.load_goal_errors()
        self.load_goal_textline() 

        self.adjust_sizes(None,None)

        self.load_accept_btn()


        self.priority_list = list()
        self.simulation_option = None 
        self.show()

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

#----------
#Utils
#----------

    def valid_coord(self,coords):
        coord_reg_ex = r"(\s*[1-9][0-9]*\s*\x2c\s*[a-zA-Z]+\s*)"
        if re.fullmatch(coord_reg_ex,coords):
            coords = coords.replace(" ","")
            coords = coords.replace('\n',"")
            coords = coords.replace('\r',"") 
            coords = coords.split(',')
            coords[1] = ord(coords[1].upper()) - 64
            coords[0] = int(coords[0]) - 1 
            if self.valid_ranges(coords[0], coords[1]):
                return True, coords
        return False, None

    def valid_ranges(self,row,column):
        row = row + 1
        if row < 0 or column < 0:
            return False
        if row <= len(self.graph) and column <= len(self.graph[0]):
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
        self.goalLbl = QLabel(self.goal.get_path())
        self.goalLbl.setPixmap(QPixmap(self.goal.get_path()))
        self.goalLbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
        self.goalLbl.setScaledContents(True) 
        self.contentVLayout.addWidget(self.goalLbl)        

    def load_goal_textline(self):
        self.goalTxt = QLineEdit()
        self.goalTxt.setEnabled(True)
        self.goalTxt.setMaximumSize(QSize(370, 30))
        self.goalTxt.setPlaceholderText("Fila , Columna")
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
            self.error_goal_invalid_coord_lbl.setVisible(False)
            if self.Map.get_cost_coord(coords[0], coords[1]-1) != None:
                if self.goal.get_label_idx() != None:
                    if self.mapGrd.itemAt(self.goal.get_label_idx()) != None:
                        self.delete_position_goal()
                self.load_goal(coords[0], coords[1])
            else:
                self.error_goal_invalid_coord_lbl.setVisible(True)
        else:
            self.error_goal_exist_coord_lbl.setVisible(True)

    def load_goal(self,x,y):
        old_lbl = self.mapGrd.itemAtPosition(x,y)
        old_lbl = old_lbl.widget()
        self.mapGrd.addWidget(self.goal.create_lbl(),x,y) 
        self.goal.set_last_position(x,y-1)
        self.goal.set_label_idx(self.mapGrd.count()-1)
        
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
        self.characterLbl = QLabel(self.character.get_path())
        self.characterLbl.setPixmap(QPixmap(self.character.get_path()))
        self.characterLbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
        self.characterLbl.setScaledContents(True) 
        self.contentVLayout.addWidget(self.characterLbl)

    def load_character_textline(self):
        self.characterTxt = QLineEdit()
        self.characterTxt.setEnabled(True)
        self.characterTxt.setMaximumSize(QSize(370, 30))
        self.characterTxt.setPlaceholderText("Fila , Columna")
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
            self.error_invalid_coord_lbl.setVisible(False)
            if self.Map.get_cost_coord(coords[0], coords[1]-1) != None:
                if self.character.get_label_idx() != None:
                    if self.mapGrd.itemAt(self.character.get_label_idx()) != None:
                        self.delete_position_character()
                self.load_character(coords[0], coords[1])
            else:
                self.error_invalid_coord_lbl.setVisible(True)
        else:
            self.error_exist_coord_lbl.setVisible(True)

    def load_character(self,x,y):
        old_lbl = self.mapGrd.itemAtPosition(x,y)
        old_lbl = old_lbl.widget()
        self.mapGrd.addWidget(self.character.create_lbl(),x,y) 
        self.character.set_last_position(x,y-1)
        self.character.set_label_idx(self.mapGrd.count() -1) 
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
        #self.accept_btn.setEnabled(True)
        self.accept_btn.clicked.connect(self.allow_change)
        self.contentVLayout.addWidget(self.accept_btn)

    def allow_change(self):
        self.simulations_options = OptionsDialog(self)

#--------
# SIMULATIONS
#-------         
    def manual_simulation(self, sm = 0):
        from scripts.simulation import SimulationWindow
        g_pos1, g_pos2 = self.goal.get_last_position()
        self.Map.set_goal(g_pos1, g_pos2)
        self.simulation = SimulationWindow(self.Map,self.character, self.goal,sm)
        self.close()

    def set_priority_list(self,l): 
        self.priority_list = l 

    def automatic_simulation(self):
        self.close()
        from scripts.simulation import SimulationWindow
        g_pos1, g_pos2 = self.goal.get_last_position()
        self.Map.set_goal(g_pos1, g_pos2)
        self.simulation = SimulationWindow(self.Map,self.character,self.goal,self.simulation_option, self.priority_list)
        

    def priority_selection(self,sm):
        self.simulation_option = sm
        self.priority_options = PriorityDialog(self)

class OptionsDialog(QDialog,Ui_Dialog):
    def __init__(self,MainWindow):
        super(OptionsDialog,self).__init__() 
        self.setupUi(self)
        self.assign_widgets()
        self.mw = MainWindow
        self.show()

    def assign_widgets(self): 
        self.manualBtn.clicked.connect(self.manual_simulation)
        self.depthBtn.clicked.connect(partial(self.priority_selection,1))
        self.breathBtn.clicked.connect(partial(self.priority_selection,2))
        self.backtrackingBtn.clicked.connect(partial(self.priority_selection,3))

    def manual_simulation(self):
        self.close()
        self.mw.manual_simulation()

    def priority_selection(self,sm): 
        self.close()
        self.mw.priority_selection(sm)

class PriorityDialog(QDialog,Priority_Dialog):
    def __init__(self,MainWindow):
        super(PriorityDialog, self).__init__()
        self.setupUi(self)
        self.mw = MainWindow
        self.load_images()
        self.vr = [] 
        self.show()
    
    def assign_simulation(self):
        self.close()
        self.mw.set_priority_list(self.vr) 
        self.mw.automatic_simulation()

    def load_images(self):
        self.leftKeyLbl = DragableLabel(get_left_key(),"left") 
        self.ketHLyt.addWidget(self.leftKeyLbl)
        self.downKeyLbl = DragableLabel(get_down_key(),"down")
        self.ketHLyt.addWidget(self.downKeyLbl)
        self.rightKeyLbl = DragableLabel(get_right_key(),"right")
        self.ketHLyt.addWidget(self.rightKeyLbl)
        self.upKeyLbl = DragableLabel(get_up_key(),"up")
        self.ketHLyt.addWidget(self.upKeyLbl)
        
        self.firstPriorityLbl = DropLbl("1",self)
        self.priorityHLyt.addWidget(self.firstPriorityLbl)
        self.secondPriorityLbl = DropLbl("2",self)
        self.priorityHLyt.addWidget(self.secondPriorityLbl)
        self.thirdPriorityLbl = DropLbl("3",self)
        self.priorityHLyt.addWidget(self.thirdPriorityLbl)
        self.fourthPriorityLbl = DropLbl("4",self)
        self.priorityHLyt.addWidget(self.fourthPriorityLbl)

    def is_complete(self):
        self.vr = []
        self.vr.append(self.firstPriorityLbl.get_priority())
        self.vr.append(self.secondPriorityLbl.get_priority())
        self.vr.append(self.thirdPriorityLbl.get_priority())
        self.vr.append(self.fourthPriorityLbl.get_priority())

        if not (self.firstPriorityLbl.get_priority() and self.secondPriorityLbl.get_priority() and self.thirdPriorityLbl.get_priority() and self.fourthPriorityLbl.get_priority()) == None:
            if len(set(self.vr)) == len(self.vr): 
                self.pushButton.setEnabled(True)
                self.pushButton.clicked.connect(self.assign_simulation)
            else:
                self.pushButton.setDisabled(True)

class DragableLabel(QLabel):
    def __init__(self,img,p):
        super().__init__()
        self.image = img
        self.priority = p 
        self.setPixmap(QPixmap(self.image)) 
        self.setScaledContents(True)
    
    def mousePressEvent(self,e): 
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

class DropLbl(QLabel):
    def __init__(self,text, MainDialog):
        super().__init__()
        self.md = MainDialog
        self.setText(text)
        self.setAcceptDrops(True)
        self.img = None
        self.priority = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            event.acceptProposedAction()  

    def get_priority(self):
        return self.priority

    def dropEvent(self, event):
        pos = event.pos() 
        self.img = event.mimeData().imageData()
        self.priority = re.search('(up|left|right|down).png',self.img).group(0)
        self.priority = self.priority.split('.')[0]
        self.setPixmap(QPixmap(self.img)) 
        self.md.is_complete()
        event.acceptProposedAction()