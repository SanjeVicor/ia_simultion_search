import sys
import re

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
 
from views.configuration_map import Ui_TemplateWindow

from scripts.main_window import MainWindow

from lands.load import get_images
from lands.load import copy_image

from models.map import Map

class TemplateWindow(QMainWindow, Ui_TemplateWindow):
    def __init__(self, file_direction="",  graph=[]): #Inicializa Mapa, este crea una matriz con nodos
        super(TemplateWindow, self).__init__()
        self.setupUi(self)
        self.Map = Map(graph,file_direction,file_direction)
        self.graph = self.Map.get_graph()
        self.landPaths = []
        self.load_coords()
        self.load_graph()
        self.load_lands()
        self.assign_widgets()
        self.show()

    def assign_widgets(self):
        self.addLandBtn.clicked.connect(self.add_lands)
        self.landLst.clicked.connect(self.get_land)
        self.updateBtn.clicked.connect(self.update_nodes)
        self.go_backBtn.clicked.connect(self.go_back)
        self.nextBtn.clicked.connect(self.allow_change)

    def go_back(self):
        self.main_w = MainWindow()
        self.close()

    def allow_change(self):
        from scripts.simulation import SimulationWindow
        from scripts.simulation_configuration import SimulationConfiguration
        self.simulation = SimulationConfiguration(self.Map)
        self.close()
        """
        self.Map.store_lands()
        print(self.Map.get_available_lands())
        self.simulation = SimulationWindow(self.Map)
        self.close()
        """
        
    def update_nodes(self):
        coords = self.coordTxt.toPlainText()
        land = self.landLbl.text()
        coord_reg_ex = r"(\s*[0-9]+\s*|\s*[1-9][0-9]*\s*\x2c\s*[a-zA-Z]*\s*)"
        coord_reg_ex2 = r"([1-9][0-9]*\s*\x2c\s*[a-zA-Z]*)"
        coord_reg_ex3 = r"(\s*[0-9]+\s*)"
        if len(self.landLst.selectedItems()) == 1:
            if re.fullmatch(coord_reg_ex,coords):
                self.coordTxt.setText("")
                self.landLbl.setText("No Seleccionado")
                self.landLst.clearSelection()
                coords = coords.replace(" ","")
                coords = coords.replace('\n',"")
                coords = coords.replace('\r',"")
                print(coords)
                if re.fullmatch(coord_reg_ex2,coords):
                    coords = coords.split(',')
                    coords[1] = ord(coords[1].upper()) - 65
                    coords[0] = int(coords[0]) - 1
                    print(coords)
                    self.Map.set_land_node(coords, land, self.get_path_of_land(land))
                elif re.fullmatch(coord_reg_ex3,coords):
                    print("Categoria : ", coords)
                    self.Map.set_land_nodes(int(coords), land, self.get_path_of_land(land))
                self.update_grap_layout()
        if self.Map.is_complete():
            self.nextBtn.setEnabled(True)
    
    def get_path_of_land(self, land):
        for path in self.landPaths:
            if re.search(land,path):
                return path
        
    def get_land(self):
        land = self.landLst.selectedItems()[0]
        for path in self.landPaths:
            if re.search(land.text(),path):
                print(path)
                image_name = path.split('/')[-1]
                land_name = image_name.split('.')[0]
                print(image_name)
                print(land_name)
        self.landLbl.setText(land_name)
        
    def add_lands(self): #Agregar terrenos a la lista
        self.landLst.clear()
        if re.fullmatch(r"([a-zA-Z]|[0-9]|_)+",self.landTxt.toPlainText()):
            file_name = QFileDialog.getOpenFileName(self,"Images (*.png *.xpm *.jpg)")
            path =file_name[0]
            path = copy_image(path,self.landTxt.toPlainText())

            itm = QListWidgetItem(QIcon(path), self.landTxt.toPlainText())
            self.landLst.addItem(itm)
            print(path)
            self.landPaths.append(path)
            print(self.landPaths)
            self.landTxt.setPlainText("")
            self.landLst.clear()
        self.load_lands()

    def load_lands(self): #Cargar terrenos ubicados en /project/lands
        self.landLst.setViewMode(QListView.IconMode)
        self.landLst.setIconSize(QSize(50,50)) 
        self.landLst.setDragEnabled(True)
        paths = get_images()
        for path in paths: 
            x = path.split('/')
            name = x[-1]
            print(path)
            self.landPaths.append(path)
            itm = QListWidgetItem(QIcon(path), name)
            self.landLst.addItem(itm)
        print(self.landPaths)

    
    

#-----------
#PRUEBAS
#-----------

    def update_grap_layout(self):
        for i in range(len(self.graph)):
            row = self.graph[i] 
            for j in range(len(row)):
                node = row[j]
                node_lbl = QLabel()  
                if node.get_image() != None:
                    data = node.get_image()
                    node_lbl.setPixmap(QPixmap(data))
                    node_lbl.setFixedSize(40,40)
                    msg = f"Coordenadas : {node.get_name()}" +'\n' +f"Tipo : {node.get_category()}"+ '\n' + f"Terreno : {node.get_land()}"
                    node_lbl.setToolTip(msg)
                    old_lbl = self.mapGrd.itemAtPosition(i,j+1)
                    old_lbl = old_lbl.widget()
                    old_lbl = self.mapGrd.indexOf(old_lbl)
                    old_lbl = self.mapGrd.takeAt(old_lbl)
                    old_lbl.widget().deleteLater()
                    self.mapGrd.addWidget(node_lbl,i,j+1)

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



    #-----------
    #PRUEBAS
    #-----------
    class lbl(QLabel):
        def __init__(self):
            super().__init__()
        
        def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.drag_start_position = event.pos()
    
        def mouseMoveEvent(self, event):
            if not(event.buttons() & Qt.LeftButton):
                return
            else:
                drag = QDrag(self)
    
                mimedata = QMimeData()
                mimedata.setText(self.text())
                mimedata.setImageData("ssds")
    
                drag.setMimeData(mimedata)
    
                # createing the dragging effect
                pixmap = QPixmap(self.size()) # label size
    
                painter = QPainter(pixmap)
                painter.drawPixmap(self.rect(), self.grab())
                painter.end()
    
                drag.setPixmap(pixmap)
                drag.setHotSpot(event.pos())
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

    def load_graph(self): #Cargar matriz a la grafica
        for i in range(len(self.graph)):
            row = self.graph[i] 

            data = str(i+1)
            #node_lbl = QLabel()
            node_lbl = self.lbl()
            node_lbl.setAlignment(Qt.AlignCenter)
            node_lbl.setFixedSize(40,40)
            node_lbl.setText(data)
            self.mapGrd.addWidget(node_lbl,i,0)

            for j in range(len(row)):
                node = row[j] 
                data  = str(node.get_category())
                #node_lbl = QLabel()
                node_lbl = self.lbl2()
                node_lbl.setAlignment(Qt.AlignCenter)
                node_lbl.setFixedSize(40,40)
                node_lbl.setText(data) 
                self.mapGrd.addWidget(node_lbl,i,j+1)
