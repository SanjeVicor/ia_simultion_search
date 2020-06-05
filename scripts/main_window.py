import sys 
import re
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from views.main import Ui_MainWindow

from utils.map_treatment import read_file

from lands.load import get_images, copy_image

from models.map import Map

from views.simulations import Ui_Dialog

import platform

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, graph=None, characters=[]):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.load_form()
        self.mapGrd.setSpacing(0)
        self.map = graph 
        self.characters = characters
        self.land_paths = list()
        self.assign_widgets()
        self.load_lands()

        if self.map != None:
            self.load_map()
        self.setStyleSheet("font-family:Verdana;")
        self.showMaximized()
        #self.setStyleSheet("background-color: #e7eff6;")
         
        #self.show() 

        #self.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.setStyleSheet("QPushButton { 	box-shadow:inset 0px 1px 0px 0px #ffffff;background-color:#ededed; border-top-left-radius:20px; border-top-right-radius:20px;  border-bottom-right-radius:20px; border-bottom-left-radius:20px;text-indent:0px;border:1px solid #dcdcdc;display:inline-block;color:#777777;font-family:Georgia;font-size:15px;font-weight:bold;font-style:normal;padding-top:15px;padding-bottom:15px;padding-left:15px;padding-right:15px;text-decoration:none;text-align:center; text-shadow:1px 1px 0px #ffffff;}")
    
    """
    FORM
    """
    def load_form(self):
        self.landLbl = QLabel("Terrenos")
        self.landLbl.setMaximumWidth(177)
        self.verticalLayout.addWidget(self.landLbl)

        self.landLbl_indication = QLabel("Arrastre el terreno al mapa")
        self.landLbl_indication.setMaximumWidth(205)
        self.verticalLayout.addWidget(self.landLbl_indication)

        self.landLst = self.LandLstWidget()
        self.landLst.setMaximumWidth(205)
        self.verticalLayout.addWidget(self.landLst)

        self.landTxt = QLineEdit()
        self.landTxt.setMaximumWidth(205)
        self.landTxt.setPlaceholderText("Nombre del terreno")
        self.verticalLayout.addWidget(self.landTxt)
 
        SecundaryBtnStyleEnabled = "QPushButton:enabled{background-color:rgb(221,221,221);border-radius:6px;color:rgb(58,59,59);font-family:Verdana;text-decoration:none;}"
        
        PrimaryBtnStyleEnabled = "QPushButton:enabled{background-color:#4e73df;border-radius:6px;color:#ffffff;font-family:Verdana;text-decoration:none;}" 
        
        btnStyleDisabled = "QPushButton:disabled{background-color:#949494;border-radius:6px;font-family:Verdana;text-decoration:none; }"

        clickEffect = "QPushButton:pressed{border-style:solid;border-width:1px;}"

        self.addLandBtn = QPushButton("Agregar terreno nuevo")
        self.addLandBtn.setEnabled(False)
        self.addLandBtn.setStyleSheet(btnStyleDisabled+SecundaryBtnStyleEnabled+clickEffect)
        self.addLandBtn.setMaximumWidth(205)
        self.verticalLayout.addWidget(self.addLandBtn)

        self.nextBtn = QPushButton("Siguiente")
        self.nextBtn.setEnabled(False)
        self.nextBtn.setStyleSheet(btnStyleDisabled+PrimaryBtnStyleEnabled+clickEffect)
        self.nextBtn.setMaximumWidth(205)
        self.verticalLayout.addWidget(self.nextBtn)

    def assign_widgets(self):
        self.actionSearch.triggered.connect(self.file_dialog)
        self.landTxt.textChanged.connect(self.land_changed_textLine)
        self.addLandBtn.clicked.connect(self.add_lands)
        self.nextBtn.clicked.connect(self.allow_change)
    
    def allow_change(self): 
        from scripts.character_edition import CharacterEditionWindow
        self.map.clear_available_lands()
        self.map.store_lands()
        self.edition = CharacterEditionWindow(Map=self.map,characters=self.characters)
        self.close()  

    class LandLstWidget(QListWidget):
        def __init__(self):
            super().__init__()
            self.setViewMode(QListView.IconMode)
            self.setSelectionMode(QAbstractItemView.SingleSelection)
            self.setDragEnabled(True)
            self.setDefaultDropAction(Qt.MoveAction)
            self.setDropIndicatorShown(True)

        def startDrag(self,supportedActions):
            item = self.currentItem()
            mimedata = self.model().mimeData(self.selectedIndexes())
            mimedata.setText(item.data(Qt.UserRole))
            drag = QDrag(self)
            drag.setMimeData(mimedata)
            if drag.start(Qt.MoveAction) == Qt.MoveAction:
                for item in self.selectedItems():
                    self.takeItem(self.row(item))
 
    
    """
    MAP
    """
    def file_dialog(self): 
        file_name = QFileDialog.getOpenFileName(self,"Text files (*.txt)") 
        if file_name[0] != '':
            matrix, exception = read_file(file_name[0])
            if matrix:
                if self.map != None:
                    self.clean_map()
                    self.nextBtn.setEnabled(False)
                self.map = Map(matrix)
                self.load_map()
            elif exception:
                error_dialog  = QErrorMessage(self)          
                error_dialog.setWindowTitle('Error al cargar mapa')
                error_dialog.showMessage(exception)
                error_dialog.show()
                if self.map != None:
                    self.clean_map()
                    self.nextBtn.setEnabled(False)

    def clean_map(self):
        matrix = self.map.get_graph()
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                    old_lbl = self.mapGrd.itemAtPosition(i,j)
                    old_lbl = old_lbl.widget()
                    old_lbl = self.mapGrd.indexOf(old_lbl)
                    old_lbl = self.mapGrd.takeAt(old_lbl)
                    old_lbl.widget().deleteLater()
        self.map.destroy()

    def set_land(self,category,land,path):
        self.map.set_land_nodes(category,land,path)
        self.update_map(category, path)
        if self.map.is_complete():
            self.nextBtn.setEnabled(True)

    def load_map(self):
        matrix = self.map.get_graph()
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                node = row[j]
                node_lbl = NodeLbl(self,category=str(node.get_category()))
                if node.get_image() != None:
                    node_lbl.setPixmap(QPixmap(node.get_image()))
                    node_lbl.setScaledContents(True)
                node_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
                msg = f"Coordenadas : {node.get_name()}" +'\n' +f"Tipo : {node.get_category()}"
                node_lbl.setToolTip(msg)
                self.mapGrd.addWidget(node_lbl,i,j)
        
        if self.map.is_complete():
            self.nextBtn.setEnabled(True)

    def update_map(self, category, path):
        matrix = self.map.get_graph()
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                node = row[j] 
                if node.get_category() == category:

                    old_lbl = self.mapGrd.itemAtPosition(i,j)
                    old_lbl = old_lbl.widget()
                    old_lbl = self.mapGrd.indexOf(old_lbl)
                    old_lbl = self.mapGrd.takeAt(old_lbl)

                    old_lbl.widget().deleteLater()
  
                    node_lbl = NodeLbl(self,str(category))
                    node_lbl.setPixmap(QPixmap(path))
                    node_lbl.setScaledContents(True)
                    node_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
                    msg = f"Coordenadas : {node.get_name()}" +'\n' +f"Tipo : {node.get_category()}"
                    node_lbl.setToolTip(msg)
                    
                    self.mapGrd.addWidget(node_lbl,i,j)
    
    """
    LANDS
    """
    def load_lands(self):
        paths = get_images()
        for path in paths:   
            x=''
            if platform.system() == "Windows":
                x =  path.split('\x5c')
            else:
                x = path.split('/')

            name = x[-1]
            self.land_paths.append(path)
            itm = QListWidgetItem(QIcon(path), name) 
            itm.setData(Qt.UserRole,path)
            self.landLst.addItem(itm)

    def add_lands(self):
        if re.fullmatch(r"(([a-zA-Z]|[0-9]|_)+|\s)*",self.landTxt.text()):
            file_name = QFileDialog.getOpenFileName(self,"Images (*.png *.xpm *.jpg)", '.', 'PNG((*.png)')
            path =file_name[0] 
            path = copy_image(path,self.landTxt.text())  
            itm = QListWidgetItem(QIcon(path), self.landTxt.text())
            self.landLst.addItem(itm) 
            self.landLst.clear()
            self.load_lands()
            self.landTxt.setText("")

    def land_changed_textLine(self):
        land = self.landTxt.text()
        if re.fullmatch(r"\s+",land) or land == "":
            self.addLandBtn.setEnabled(False)
        else:
            self.addLandBtn.setEnabled(True)

class NodeLbl(QLabel):
    def __init__(self,MainWindow,category):
        super().__init__() 
        self.category = int(category)
        self.setText(category)
        self.mw = MainWindow
        self.setAcceptDrops(True) 
    
    def dragEnterEvent(self, event): 
        if event.mimeData().hasText():
            event.acceptProposedAction()
    
    def dropEvent(self, event):  
        land_path = event.mimeData().text()
        if platform.system() == "Windows":
            land =  land_path.split('\x5c')[-1]
        else:
            land = land_path.split('/')[-1]
        land = land.split('.')[0]
        event.acceptProposedAction()
        self.mw.set_land(self.category,land,land_path)


        

app = QApplication(sys.argv)
mainWin = MainWindow()
ret = app.exec_()
sys.exit(ret)