import sys 
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from views.simulation import Ui_MainWindow 

from models.map import Map
from models.character import Character
from models.goal import Goal

class SimulationWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, Map, character, goal): 
        super(SimulationWindow, self).__init__()
        self.setupUi(self)
        self.Map = Map
        self.graph = Map.get_graph()
        self.character = character
        self.goal = goal
        self.i = 1
        self.total_cost = 0
        self.load_graph()
        
        t_r, t_c = self.goal.get_last_position()
        self.target = [t_r,t_c]

        idx = self.mapGrd.count()
        self.goal.set_label_idx(idx)
        self.load_goal()


        idx = self.mapGrd.count()
        self.character.set_label_idx(idx)

        x,y = self.character.get_last_position()
        self.load_character(x,y)
        self.assign_widgets()
        self.show()

    def assign_widgets(self):
        pass

    def load_character(self,x,y):
        old_lbl = self.mapGrd.itemAtPosition(x,y)
        old_lbl = old_lbl.widget()
        self.mapGrd.addWidget(self.character.create_lbl(),x,y) 

    def load_goal(self):
        x,y = self.goal.get_last_position()
        old_lbl = self.mapGrd.itemAtPosition(x,y)
        old_lbl = old_lbl.widget()
        self.mapGrd.addWidget(self.goal.create_lbl(),x,y) 

    def load_new_visit(self,x,y):
        visits = self.Map.get_visits(x,y)
        node_layout = self.mapGrd.itemAtPosition(x,y)
        node_layout = node_layout.layout() 
        node_info = node_layout.itemAt(1)
        node_info = node_info.layout()
        if len(visits) == 1: # Se añade en la funcion anterior
            old_lbl = node_info.itemAt(0)
            print("Item at 0 : ", old_lbl)
            old_lbl = node_info.indexOf(old_lbl)
            old_lbl = node_info.takeAt(old_lbl) 
            old_lbl.widget().deleteLater()

        if node_info.count() < 4:
            node_data = QLabel()
            node_data.setMaximumHeight(15)
            node_data.setText(str(self.character.get_visits()))
            node_data.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
            node_data.setStyleSheet("QLabel {border: 1px solid gray;border-color: rgb(0, 0, 0);}")
            node_info.addWidget(node_data)
        node_lbl = node_layout.itemAt(0).widget()
        
        print(visits)
        visits_str = "Visitas : ["
        for v in visits:
            visits_str += str(v) + " ,"
        visits_str += "]"
        node_lbl.setToolTip(visits_str)

    def update_cost_lbl(self,x,y):
        self.total_cost += self.Map.get_weight(x,y)
        data = f"Costo Total : {self.total_cost}"
        self.rewardLbl.setText(data)

    def delete_position_character(self):
        old_lbl = self.mapGrd.itemAt(self.character.get_label_idx())
        old_lbl = self.mapGrd.indexOf(old_lbl)
        old_lbl = self.mapGrd.takeAt(old_lbl) 
        old_lbl.widget().deleteLater()

    def update_movement(self,row,column):
        self.character.set_new_visit()
        self.Map.set_visit(row,column,self.character.get_visits())
        self.delete_position_character()
        self.load_character(row,column)
        self.load_new_visit(row,column)
        self.update_cost_lbl(row,column)
        self.character.set_last_position(row,column)

    def is_done(self,row,column):
        if self.target[0] == row and self.target[1] == column:
            done = QMessageBox().about(self,"Simulación terminada","Simulación terminada con exito") 

    def keyPressEvent(self, event: QKeyEvent):
        print("posicion actual del personaje : ", self.character.get_last_position() )
        row,column = self.character.get_last_position()
        if event.key() == Qt.Key_Up:
            if self.Map.return_up_down(row-1):
                self.update_movement(row-1,column)
                self.is_done(row-1,column)
        if event.key() == Qt.Key_Down:
            if self.Map.return_up_down(row+1):
                self.update_movement(row+1,column)
                self.is_done(row+1,column)
        if event.key() == Qt.Key_Left:
            if self.Map.return_left_right(column-1):
                self.update_movement(row,column-1)
                self.is_done(row,column-1)
        if event.key() == Qt.Key_Right:
            if self.Map.return_left_right(column+1):
                self.update_movement(row,column+1)
                self.is_done(row,column+1)

    def load_graph(self): 
        for i in range(len(self.graph)):
            row = self.graph[i] 
            for j in range(len(row)):
                node = row[j]
                cell = QVBoxLayout()
                cell_data = QHBoxLayout()
                node_lbl = QLabel() 
                if node.get_image() != None:
                    data = node.get_image()
                    node_lbl.setPixmap(QPixmap(data))
                    node_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
                    node_lbl.setScaledContents(True)
                    cell.addWidget(node_lbl)
                    
                    node_data = QLabel()
                    node_data.setMaximumHeight(0) 
                    node_data.setText("_")
                    node_data.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
                    node_data.setStyleSheet("QLabel {border: 1px solid gray;border-color: rgb(0, 0, 0);}")
                    cell_data.addWidget(node_data)
                    """
                    node_data = QLabel()
                    node_data.setMaximumHeight(15)
                    node_data.setText("16")
                    node_data.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
                    node_data.setStyleSheet("QLabel {border: 1px solid gray;border-color: rgb(0, 0, 0);}")
                    cell_data.addWidget(node_data)

                    node_data = QLabel()
                    node_data.setMaximumHeight(15)
                    node_data.setText("14")
                    node_data.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
                    node_data.setStyleSheet("QLabel {border: 1px solid gray;border-color: rgb(0, 0, 0);}")
                    cell_data.addWidget(node_data)


                    node_data = QLabel()
                    node_data.setMaximumHeight(15)
                    node_data.setText("13")
                    node_data.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
                    node_data.setStyleSheet("QLabel {border: 1px solid gray;border-color: rgb(0, 0, 0);}")
                    cell_data.addWidget(node_data)
                    """

                    cell.addLayout(cell_data)

                    self.mapGrd.addLayout(cell,i,j)
