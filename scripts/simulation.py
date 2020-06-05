import sys 
import time
import copy

from graphviz import Digraph

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import * 


from views.simulation import Ui_MainWindow 

from models.map import Map
from models.character import Character
from models.goal import Goal

from models.inital import Initial_point

from extra_images.load import get_solution_image


import platform

class SimulationWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, Map, character, goal, simulation,priority=[],distance=None): 
        super(SimulationWindow, self).__init__()
        self.setupUi(self) 
        self.simulation = simulation 

        self.distance = distance
        self.Map =  copy.deepcopy(Map)
        self.graph = self.Map.get_graph()
        
        self.character = character
        self.goal = goal
        self.i = 1
        self.total_cost = 0

        t_r, t_c = self.goal.get_last_position()
        self.target = [t_r,t_c]
        self.graph[t_r][t_c].set_extra_data("FINAL")

        if distance == 0:
            self.Map.generate_euclidean(t_r, t_c )
        elif distance == 1:
            self.Map.generate_manhattan(t_r, t_c )

        #if simulation in {0,4,5,6}:
        #    self.load_graph()
        #elif simulation in {1,2,3}:
        #    self.load_graph_blind()
        self.load_graph_blind()

        x,y = self.character.get_last_position()

        idx = self.mapGrd.count()
        self.initial = Initial_point(idx)
        self.initial.set_last_position(x,y)
        self.graph[x][y].set_extra_data("INICIAL")
        self.load_initial()

        idx = self.mapGrd.count()
        self.goal.set_label_idx(idx)
        self.load_goal()

        idx = self.mapGrd.count()
        self.character.set_label_idx(idx)

        self.load_first(x,y)
        self.first = True
        self.assign_widgets()

        self.done = False
        row,column = self.character.get_last_position()
        if simulation == 0:
            self.is_done(row,column)
        self.priority = priority
        self.restart_btn.setFocusPolicy(Qt.NoFocus)
        
        
        PrimaryBtnStyleEnabled = "QPushButton:enabled{background-color:#4e73df;border-radius:6px;color:#ffffff;font-family:Verdana;text-decoration:none;}" 
        btnStyleDisabled = "QPushButton:disabled{background-color:#949494;border-radius:6px;font-family:Verdana;text-decoration:none; }"
        clickEffect = "QPushButton:pressed{border-style:solid;border-width:1px;}"
        stl = PrimaryBtnStyleEnabled + btnStyleDisabled + clickEffect
        
        self.restart_btn.setStyleSheet(stl)
        
        
        self.showMaximized()
        #self.show() 

        self.visited_nodes = list()
        self.to_be_visited_nodes = list() 


        graph_name = self.character.get_name()
        row,column = self.character.get_last_position()
        self.to_be_visited_nodes.append( self.graph[row][column])
        self.setStyleSheet("font-family:Verdana;")
        if self.simulation == 1:
            graph_name += "_profundidad"
            self.graphical_graphviz = Digraph(graph_name,format="png")
            self.graphical_graphviz.attr(label=r'Árbol de Búsqueda (Profundidad)')
            graph_name += "_profundidad_solution"
            self.graphical_solution_graphviz = Digraph(graph_name,format="png")
            self.graphical_solution_graphviz.attr(label=r'Ruta de Solución (Profundidad)')
            QTimer.singleShot(1000, lambda:self.depth_first_search(row, column))
        elif self.simulation == 2:
            graph_name += "_anchura"
            self.graphical_graphviz = Digraph(graph_name,format="png")
            self.graphical_graphviz.attr(label=r'Árbol de Búsqueda (Anchura)')
            graph_name += "_anchura_solution"
            self.graphical_solution_graphviz = Digraph(graph_name,format="png")
            self.graphical_solution_graphviz.attr(label=r'Ruta de Solución  (Anchura)')
            QTimer.singleShot(1000, lambda:self.breath_first_search(row, column)) 
        elif self.simulation == 3:
            graph_name += "_backtracking"
            self.graphical_graphviz = Digraph(graph_name,format="png")
            self.graphical_graphviz.attr(label=r'Árbol de Búsqueda (Backtracking)')
            graph_name += "_backtracking_solution"
            self.graphical_solution_graphviz = Digraph(graph_name,format="png")
            self.graphical_solution_graphviz.attr(label=r'Ruta de Solución  (Backtracking)')
            QTimer.singleShot(1000, lambda:self.backtracking_search(row, column)) 
        elif self.simulation == 4:
            graph_name += "_coste_uniforme"
            self.graphical_graphviz = Digraph(graph_name,format="png")
            self.graphical_graphviz.attr(label=r'Árbol de Búsqueda (Coste Uniforme)')
            graph_name += "_coste_uniforme_solution"
            self.graphical_solution_graphviz = Digraph(graph_name,format="png")
            self.graphical_solution_graphviz.attr(label=r'Ruta de Solución  (Coste Uniforme)')
            QTimer.singleShot(1000, lambda:self.ucs(row,column)) 
            
        elif self.simulation == 5:
            graph_name += "_voraz"
            self.graphical_graphviz = Digraph(graph_name,format="png")
            self.graphical_graphviz.attr(label=r'Árbol de Búsqueda (Voraz Primero el Mejor)')
            graph_name += "_voraz_solution"
            self.graphical_solution_graphviz = Digraph(graph_name,format="png")
            self.graphical_solution_graphviz.attr(label=r'Ruta de Solución  (Voraz Primero el Mejor)')
            QTimer.singleShot(1000, lambda:self.greedy(row,column))  
        elif self.simulation == 6:
            graph_name += "_A" 
            self.graphical_graphviz = Digraph(graph_name,format="png")
            self.graphical_graphviz.attr(label=r'Árbol de Búsqueda (A*)')
            graph_name += "_A_solution"
            self.graphical_solution_graphviz = Digraph(graph_name,format="png")
            self.graphical_solution_graphviz.attr(label=r'Ruta de Solución  (A*)')
            QTimer.singleShot(1000, lambda:self.A_star(row,column))  
 
#----------
# MAP
#----------
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

                    cell.addLayout(cell_data)

                    self.mapGrd.addLayout(cell,i,j)

    def load_graph_blind(self):
        for i in range(len(self.graph)):
            row = self.graph[i] 
            for j in range(len(row)):
                node = row[j] 
                cell = QVBoxLayout()
                cell_data = QHBoxLayout()
                node_lbl = QLabel() 
                if node.get_image() != None:
                    if (i,j) != self.goal.get_last_position(): 
                        data = node.get_cover()
                        node_lbl.setPixmap(QPixmap(data))
                        node_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
                        node_lbl.setScaledContents(True)
                        cell.addWidget(node_lbl)
                    else:
                        data = node.get_image()
                        node_lbl.setPixmap(QPixmap(data))
                        node_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
                        node_lbl.setScaledContents(True)
                        cell.addWidget(node_lbl)
                    
                    if self.simulation > 3:
                        node_data = QLabel("_") 
                        node_data.setMaximumHeight(0) 
                        node_data.setScaledContents(True)
                        node_data.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
                        node_data.setStyleSheet("QLabel {border: 1px solid gray;border-color: rgb(0, 0, 0);}")
                        cell_data.addWidget(node_data)
                        cell.addLayout(cell_data)

                    cell_data = QHBoxLayout()
                    node_data = QLabel()
                    node_data.setMaximumHeight(0) 
                    node_data.setText("_")
                    node_data.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
                    node_data.setStyleSheet("QLabel {border: 1px solid gray;border-color: rgb(0, 0, 0);}")
                    cell_data.addWidget(node_data)

                    cell.addLayout(cell_data)

                    self.mapGrd.addLayout(cell,i,j) 
        self.load_coords()

    def load_coords(self): 
        for i in range(len(self.graph)):
            data = QLabel(str(i+1))
            
            data.setAlignment(Qt.AlignCenter)
            data.setScaledContents(True) 
            data.setFixedWidth(data.fontMetrics().width(data.text()))
            self.RowLyt.addWidget(data)

        for i in range(len(self.graph[0]) ):
            data = QLabel(chr(65+i))
            data.setAlignment(Qt.AlignCenter)
            data.setScaledContents(True)
            data.setFixedHeight(data.fontMetrics().height())
            self.ColumnLyt.addWidget(data)

    def load_initial(self):
        x,y = self.initial.get_last_position()
        old_lbl = self.mapGrd.itemAtPosition(x,y)
        old_lbl = old_lbl.widget()
        self.mapGrd.addWidget(self.initial.create_lbl(),x,y)

    def assign_widgets(self):
        self.restart_btn.clicked.connect(self.restart)

    def restart(self): 
        self.character.clear_visits()
        self.character.Map.clear_visits() 
        i_pos1, i_pos2 = self.initial.get_last_position()
        self.character.set_last_position(i_pos1, i_pos2)
        self.close()
        from scripts.simulation_configuration import SimulationConfiguration
        self.simulation = SimulationConfiguration(self.character, self.goal) 

    def load_first(self,x,y):
        if self.simulation == 0:
            self.character.set_new_visit()
            self.Map.set_visit(x,y,self.character.get_visits())
            old_lbl = self.mapGrd.itemAtPosition(x,y)
            old_lbl = old_lbl.widget()
            self.load_new_visit(x,y)
            self.get_and_uncover_neigbors(x,y)
        self.mapGrd.addWidget(self.character.create_lbl(),x,y) 
        
        #if self.simulation in {1,2,3}:
        #    self.uncover_neigbor(x,y)
        self.uncover_neigbor(x,y)

    def load_character(self,x,y):
        self.character.set_new_visit()
        self.Map.set_visit(x,y,self.character.get_visits())
        old_lbl = self.mapGrd.itemAtPosition(x,y)
        old_lbl = old_lbl.widget()
        self.mapGrd.addWidget(self.character.create_lbl(),x,y) 
        self.load_new_visit(x,y)
        
        if self.simulation in {0,4,6} and not self.first:
            self.update_cost_lbl(x,y)
        self.first = False

    def load_goal(self):
        x,y = self.goal.get_last_position()
        old_lbl = self.mapGrd.itemAtPosition(x,y)
        old_lbl = old_lbl.widget()
        self.mapGrd.addWidget(self.goal.create_lbl(),x,y) 

    def load_new_visit(self,x,y):
        visits = self.Map.get_visits(x,y)
        node_layout = self.mapGrd.itemAtPosition(x,y)
        node_layout = node_layout.layout()  

        if self.simulation > 3:
            item = 2
        else:
            item = 1
        node_info = node_layout.itemAt(item)
        node_info = node_info.layout()
        if len(visits) == 1: # Se añade en la funcion anterior
            old_lbl = node_info.itemAt(0) 
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
         
        visits_str = "Visitas : ["
        for v in visits:
            visits_str += str(v) + " ,"
        visits_str += "]"
        node_lbl.setToolTip(visits_str)

        row,column = self.initial.get_last_position()

        if row == x and column == y:
            self.mapGrd.itemAt(self.initial.get_label_idx()).widget().setToolTip(visits_str)

    def delete_position_character(self):
        old_lbl = self.mapGrd.itemAt(self.character.get_label_idx())
        old_lbl = self.mapGrd.indexOf(old_lbl)
        old_lbl = self.mapGrd.takeAt(old_lbl) 
        old_lbl.widget().deleteLater()

    def update_movement(self,row,column):
        self.delete_position_character()
        self.load_character(row,column)
        self.character.set_last_position(row,column)

    def get_and_uncover_neigbors(self,row,column):
        if self.Map.is_up_down(row-1,column):
            self.uncover_neigbor(row-1,column)
        if self.Map.is_left_right(row,column+1):
            self.uncover_neigbor(row,column+1)
        if self.Map.is_up_down(row+1,column):
            self.uncover_neigbor(row+1,column)
        if self.Map.is_left_right(row,column-1):
            self.uncover_neigbor(row,column-1)

    def uncover_neigbor(self,row,column): 
        node = self.graph[row][column]
        data = node.get_image()
        self.mapGrd.itemAtPosition(row,column).layout().itemAt(0).widget().setPixmap(QPixmap(data))  
        
        if self.simulation > 3 and node.get_weight() != None:
            LBL = self.mapGrd.itemAtPosition(row,column).itemAt(1).itemAt(0).widget()
            cumulative_cost = node.get_cumulative_cost()
            distance = node.get_distance()
            if self.simulation == 4:
                data = (f"C.A : {cumulative_cost}")
            elif self.simulation == 5:
                data = (f"D : {distance}")
            elif self.simulation == 6:
                data = (f"C({cumulative_cost}) + D({distance}) = {cumulative_cost + distance}")
            LBL.setText(data)
            LBL.setMaximumHeight(15)
    
#----------
# SIMULATIONS
#----------

    def keyPressEvent(self, event: QKeyEvent):
        self.restart_btn.clearFocus()
        if self.simulation != 0:
            event.ignore()
                
        elif not self.done : 
            row,column = self.character.get_last_position()
            if event.key() == Qt.Key_Up:
                if self.Map.return_up_down(row-1,column):
                    self.update_movement(row-1,column)
                    self.get_and_uncover_neigbors(row-1,column)
                    self.is_done(row-1,column)
            if event.key() == Qt.Key_Down:
                if self.Map.return_up_down(row+1,column):
                    self.update_movement(row+1,column)
                    self.get_and_uncover_neigbors(row+1,column)
                    self.is_done(row+1,column)
            if event.key() == Qt.Key_Left:
                if self.Map.return_left_right(row,column-1):
                    self.update_movement(row,column-1) 
                    self.get_and_uncover_neigbors(row,column-1)
                    self.is_done(row,column-1)
            if event.key() == Qt.Key_Right:
                if self.Map.return_left_right(row,column+1):
                    self.update_movement(row,column+1)
                    self.get_and_uncover_neigbors(row,column+1)
                    self.is_done(row,column+1)
           
    def depth_first_search(self, row, column):  
        self.update_movement(row,column) 
        node = self.graph[row][column]
        self.visited_nodes.append(node)  
        self.to_be_visited_nodes.remove(node)
        self.is_done(row,column)           
        if self.done:
            self.generate_graphs()
            return 
        self.set_neighbors(row,column) 
        self.get_and_uncover_neigbors(row,column)
        if self.is_error():
            return
        node = self.to_be_visited_nodes[-1]
        row=node.get_coord_x()
        column = node.get_coord_y()
        QTimer.singleShot(500, lambda:self.depth_first_search(row,column))

    def breath_first_search(self,row,column):  
        self.update_movement(row,column) 
        node = self.graph[row][column]
        self.visited_nodes.append(node)  
        self.to_be_visited_nodes.remove(node)
        self.is_done(row,column)               
        if self.done:
            self.generate_graphs()
            return 
        self.set_neighbors(row,column)
        self.get_and_uncover_neigbors(row,column)
        if self.is_error():
            return
        node = self.to_be_visited_nodes[0]
        row=node.get_coord_x()
        column = node.get_coord_y()
        QTimer.singleShot(500, lambda:self.breath_first_search(row,column))

    def backtracking_search(self, row, column): 
        self.update_movement(row,column) 
        node = self.graph[row][column]
        self.visited_nodes.append(node)  
        self.is_done(row,column)          
        if self.done:
            self.generate_graphs()
            return 
        self.set_neighbors(row,column)
        self.get_and_uncover_neigbors(row,column)
        if not self.pending_nodes(row,column):
            self.to_be_visited_nodes.remove(node)
        if self.is_error():
            return 
        node = self.to_be_visited_nodes[-1]
        row=node.get_coord_x()
        column = node.get_coord_y()
        QTimer.singleShot(500, lambda:self.backtracking_search(row,column))

    def ucs(self,row,column):
        self.update_movement(row,column) 
        node = self.graph[row][column]
        self.visited_nodes.append(node)  
        self.to_be_visited_nodes.remove(node)
        self.is_done(row,column)               
        if self.done:
            self.generate_graphs()
            return 
        self.set_neighbors(row,column)
        self.get_and_uncover_neigbors(row,column)
        self.to_be_visited_nodes.sort(key=lambda e: e.get_cumulative_cost())
        #print(self.to_be_visited_nodes[0].get_cumulative_cost())
        #print(self.to_be_visited_nodes[-1].get_cumulative_cost())
        if self.is_error():
            return
        node = self.to_be_visited_nodes[0]
        row=node.get_coord_x()
        column = node.get_coord_y()
        QTimer.singleShot(500, lambda:self.ucs(row,column))

    def greedy(self, row, column):
        self.update_movement(row,column) 
        node = self.graph[row][column]
        self.visited_nodes.append(node)  
        self.to_be_visited_nodes.remove(node)
        self.is_done(row,column)               
        if self.done:
            self.generate_graphs()
            return 
        self.set_neighbors(row,column)
        self.get_and_uncover_neigbors(row,column)
        self.to_be_visited_nodes.sort(key=lambda e: e.get_distance())
        #print(self.to_be_visited_nodes[0].get_distance())
        #print(self.to_be_visited_nodes[-1].get_distance())
        if self.is_error():
            return
        node = self.to_be_visited_nodes[0]
        row=node.get_coord_x()
        column = node.get_coord_y()
        QTimer.singleShot(500, lambda:self.greedy(row,column))

    def A_star(self, row, column):
        self.update_movement(row,column) 
        node = self.graph[row][column]
        self.visited_nodes.append(node)  
        self.to_be_visited_nodes.remove(node)
        self.is_done(row,column)               
        if self.done:
            self.generate_graphs()
            return 
        self.set_neighbors(row,column)
        self.get_and_uncover_neigbors(row,column)
        self.to_be_visited_nodes.sort(key=lambda e: (e.get_distance() + e.get_cumulative_cost()))
        #print(self.to_be_visited_nodes[0].get_name() ," ", (self.to_be_visited_nodes[0].get_distance() + self.to_be_visited_nodes[0].get_weight()) )
        if self.is_error():
            return
        node = self.to_be_visited_nodes[0]
        row=node.get_coord_x()
        column = node.get_coord_y()
        QTimer.singleShot(500, lambda:self.A_star(row,column))

#----------
# UTILS
#----------
    def update_cost_lbl(self,x,y):
        self.total_cost += self.Map.get_weight(x,y)
        data = f"Costo Total : {self.total_cost:.2f}"
        self.rewardLbl.setText(data)
   
    def is_done(self,row,column):
        if self.target[0] == row and self.target[1] == column:
            if self.simulation > 0 and self.simulation < 4:
                done_box = QMessageBox().about(self,"Simulación terminada",f"{self.character.get_name()} - Simulación terminada con exito \n*A continuación se mostrara la solución en el mapa en forma de \u2714 y se entregará las imagenes de los grafos correspondientes") 
            elif self.simulation > 3:
                cost_solution =  self.graph[row][column].get_cumulative_cost()
                done_box = QMessageBox().about(self,f"Simulación terminada",f"{self.character.get_name()} - Simulación terminada con exito \n*A continuación se mostrara la solución en el mapa en forma de \u2714 y se entregará las imagenes de los grafos correspondientes \n*Coste total de solución : {cost_solution}") 
            elif self.simulation == 0:
                done_box = QMessageBox().about(self,"Simulación terminada",f"{self.character.get_name()} - Simulación terminada con exito") 
            self.done = True

    def is_error(self):
        if len(self.to_be_visited_nodes) == 0:
             done_box = QMessageBox().about(self,"Simulación terminada",f"{self.character.get_name()} - Simulación terminada sin exito")
             return True
        return False

    def add_n(self,c_r,c_c,n_r,n_c):
        c_n_aux = self.graph[c_r][c_c].get_neighbors()
        n_aux = self.graph[n_r][n_c]
        #n = [n_r,n_c]
        n = self.graph[n_r][n_c]
        if n_aux not in c_n_aux:
            self.Map.set_parent(c_r,c_c,n_r,n_c)
            self.Map.set_new_neighbor(c_r,c_c,n_r,n_c)
        self.to_be_visited_nodes.append(n)

    def remove_n(self,c_r,c_c,n_r,n_c):
        n = self.graph[n_r][n_c]
        if n in self.to_be_visited_nodes:
            n_current = self.graph[c_r][c_c]
            n_current_cumulative_w = n_current.get_cumulative_cost()
            n_child_w = float(n.get_weight())
            new_cost = n_current_cumulative_w + n_child_w
            if n.get_cumulative_cost() > new_cost:
                p = n.get_parent()
                p.remove_neighbor(n)
                self.to_be_visited_nodes.remove(n)
                
    def set_neighbors(self,row,column,fn=None,gn=None):
        for i in range(len(self.priority)):         
            if self.priority[i] == 'up' and self.Map.return_up_down(row-1,column): 
                n = self.graph[row-1][column]

                if self.simulation == 4: #UCS
                    self.remove_n(row,column,row-1,column) 

                if (n not in self.visited_nodes and n not in self.to_be_visited_nodes):
                    self.add_n(row,column,row-1,column) 
                    if self.simulation in {3} :
                        break

            elif self.priority[i] == 'down' and self.Map.return_up_down(row+1,column):
                      
                n = self.graph[row+1][column] 

                if self.simulation == 4: #UCS
                    self.remove_n(row,column,row+1,column) 
                
                if (n not in self.visited_nodes and n not in self.to_be_visited_nodes):
                    self.add_n(row,column,row+1,column) 
                    if self.simulation in {3}:
                        break

            elif self.priority[i] == 'right' and self.Map.return_left_right(row,column+1):
                
                n = self.graph[row][column+1]
                
                if self.simulation == 4: #UCS
                    self.remove_n(row,column,row,column+1) 
                
                if (n not in self.visited_nodes and n not in self.to_be_visited_nodes):
                    self.add_n(row,column,row,column+1) 
                    if self.simulation  in {3}:
                        break

            elif self.priority[i] == 'left' and self.Map.return_left_right(row,column-1):
                
                n = self.graph[row][column-1]
                
                if self.simulation == 4: #UCS
                    self.remove_n(row,column,row,column-1) 
                
                if (n not in self.visited_nodes and n not in self.to_be_visited_nodes):
                    self.add_n(row,column,row,column-1) 
                    if self.simulation  in {3}:
                        break
                    
    def generate_graphs(self):
        e = self.visited_nodes[0]
        r = e.get_coord_x()
        c = e.get_coord_y()
        n = self.Map.get_node(r,c)
        
        self.get_path(n)
        if platform.system() == "Windows":
            path_graph = "img_graphs\x5c" + self.graphical_graphviz.name
        else:
            path_graph = "img_graphs/" + self.graphical_graphviz.name
        self.graphical_graphviz.render(path_graph, view=True)
        
        e = self.visited_nodes[-1]
        r = e.get_coord_x()
        c = e.get_coord_y()
        n = self.Map.get_node(r,c)

        self.get_solution(n)
        if platform.system() == "Windows":
            path_graph = "img_graphs\x5c" + self.graphical_solution_graphviz.name
        else: 
            path_graph = "img_graphs/" + self.graphical_solution_graphviz.name
        self.graphical_solution_graphviz.render(path_graph, view=True)
            
    def pending_nodes(self, row,column): 
        total_ns = 0
        if self.Map.return_up_down(row-1,column) and [row-1,column] not in self.visited_nodes: 
            total_ns += 1
        if self.Map.return_up_down(row+1,column) and [row+1,column] not in self.visited_nodes: 
            total_ns += 1
        if self.Map.return_left_right(row,column-1) and [row,column-1] not in self.visited_nodes: 
            total_ns += 1
        if self.Map.return_left_right(row,column+1) and [row,column+1] not in self.visited_nodes: 
            total_ns += 1 
        if total_ns == 0:
            return False
        else:
            return True

    def get_path(self, n):
        node_name = n.get_name()
        node_visits = n.get_visits()
        neighbors = n.get_neighbors()
        node_lbl = node_name + "\n" + "Visitas : "
        for v in node_visits:
            node_lbl+=str(v) + ","    

        if self.simulation in {4,6}:
            node_lbl += "\n" + "Coste Acumulado : " + str(n.get_cumulative_cost()) 
        if self.simulation in {5,6}:
            node_lbl += "\n" + "Distancia : " + str(n.get_distance())
            if self.simulation == 6:
                cost = n.get_distance() + n.get_cumulative_cost()
                node_lbl += "\n" + "Costo Total : " + str(cost)

        node_lbl += "\n" + str(n.get_extra_data())    
        self.graphical_graphviz.node(node_name,node_lbl)

        sons = list()
        
        for n in neighbors:
            sons.append(n.get_name())

        for n_s in neighbors: 
            self.get_path(n_s)
            if self.simulation < 4:
                self.graphical_graphviz.edge(node_name,n_s.get_name())
            else:
                lbl = str(n_s.get_weight())
                self.graphical_graphviz.edge(node_name,n_s.get_name() , label=lbl)

    def get_solution(self,n):
        self.add_solution_map(n.get_coord_x(),n.get_coord_y())
        node_name = n.get_name()
        node_visits = n.get_visits()
        node_lbl = node_name + "\n" + "Visitas : "
        for v in node_visits:
            node_lbl+=str(v) + ","    

        if self.simulation == 4:
            node_lbl += "\n" + "Coste Acumulado : " + str(n.get_cumulative_cost()) 
        elif self.simulation in {5,6}:
            node_lbl += "\n" + "Distancia : " + str(n.get_distance())

        node_lbl += "\n" + str(n.get_extra_data())    
        self.graphical_solution_graphviz.node(node_name,node_lbl)

        n_p = n.get_parent()
        if n_p == None:
            return

        if self.simulation < 4:
            self.graphical_solution_graphviz.edge(n_p.get_name(),node_name)
        else:
                lbl = str(n.get_weight())
                self.graphical_solution_graphviz.edge(n_p.get_name(),node_name , label=lbl)

        self.get_solution(n_p)

    def add_solution_map(self,x,y): 
        old_lbl = self.mapGrd.itemAtPosition(x,y)
        old_lbl = old_lbl.widget()
        solution_lbl = QLabel() 
        solution_lbl.setPixmap(QPixmap(get_solution_image()))
        solution_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
        solution_lbl.setScaledContents(True) 
        self.mapGrd.addWidget(solution_lbl,x,y)

    