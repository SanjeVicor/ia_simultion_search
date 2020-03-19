import sys 
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from views.main import Ui_MainWindow 

from utils.map_treatment import read_file

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self): 
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assign_widgets()
        self.show()

        self.file_path=""
        self.matrix = []        
    
    def assign_widgets(self):
        self.loadFileBtn.clicked.connect(self.file_dialog)
        self.loadBtn.clicked.connect(self.allow_change) 

    def allow_change(self):
        from scripts.map_configuration import TemplateWindow
        self.map_configuration_window = TemplateWindow(file_direction=self.file_path,graph=self.matrix) 
        self.close()

    def file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self,"Text files (*.txt)")
        self.fileDirectionLbl.setText(file_name[0])
        self.fileDirectionLbl.adjustSize()
        self.file_path = self.fileDirectionLbl.text()

        self.matrix, exception = read_file(self.file_path)
        if self.matrix:
            self.loadBtn.setEnabled(True)
        elif exception:
            error_dialog  = QErrorMessage(self)          
            error_dialog.setWindowTitle('Error al cargar mapa')
            error_dialog.showMessage(exception)
            error_dialog.show()

app = QApplication(sys.argv)
mainWin = MainWindow()
ret = app.exec_()
sys.exit(ret)