import sys
import re

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from views.character_selection import Ui_MainWindow

from models.map import Map
from models.character import Character

from characters.load import get_images
from characters.load import copy_image

class CharacterEditionWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,Map = Map(), characters=list(), land_Paths=list()):
        super(CharacterEditionWindow,self).__init__()
        self.setupUi(self)
        self.land_path = land_Paths
        self.Map = Map
        print(self.Map.get_available_lands()) 
        self.characters = characters
        self.actual_character = None
        self.characters_paths = list()
        if len(characters) == 0:
            self.characters.append(Character(name="NUEVO PERSONAJE",Map=self.Map))
        else:
            for e in self.characters:
                e.make_new_copy_of_map(self.Map)
        self.load_characters_layout()
        self.load_lands()
        self.assign_events()
        self.accept_btn.setDisabled(True)
        self.show()

    def assign_events(self):
        self.name_txt.textChanged.connect(self.character_changed_textLine)
        self.images_lst.itemSelectionChanged.connect(self.on_listWidget_clicked)
        self.accept_btn.clicked.connect(self.allow_change)
        self.go_back_btn.clicked.connect(self.go_back)
        self.search_img_btn.clicked.connect(self.add_images)

    def add_images(self):
        file_name = QFileDialog.getOpenFileName(self,"Images (*.png *.xpm *.jpg)",'.', 'PNG((*.png)')
        path =file_name[0]
        name , path = copy_image(path)
        itm =  QListWidgetItem(QIcon(path),name)
        self.images_lst.addItem(itm)
        self.characters_paths.append(path)

    def go_back(self):
        from scripts.map_configuration import TemplateWindow
        
        for e in self.characters:
            e.clear_lands()

        self.edition = TemplateWindow(graph=self.Map, characters=self.characters)
        self.close()

    def allow_change(self):
        print(self.actual_character.Map.print_matrix())
        self.actual_character.clear_visits()
        self.actual_character.Map.clear_visits()
        from scripts.simulation_configuration import SimulationConfiguration
        self.simulation = SimulationConfiguration(self.actual_character)
        #self.close()

    def modify_nameBtn(self,idx):
        group_btns = self.select_character_lyt.itemAt(idx).layout()
        print(group_btns)
        btn = group_btns.itemAt(1).widget()
        print(btn)
        char = self.characters[idx]
        btn.setText(char.get_name())
        
    def character_changed_textLine(self):
        self.actual_character.set_name(self.name_txt.text())
        print("nuevo : " , self.actual_character.get_name())
        for idx, e in enumerate(self.characters):
            if self.actual_character.get_name() == e.get_name():
                print(idx)
                print(e.get_name())
                self.modify_nameBtn(idx)
                break
            
    def load_characters_layout(self):
        print("memoria", self.characters)
        for e in self.characters: 
            add_btn,delete_btn,character_btn = self.get_buttons(e)
            hlyt = QHBoxLayout()
            hlyt.addWidget(add_btn)
            hlyt.addWidget(character_btn)
            hlyt.addWidget(delete_btn)
            self.select_character_lyt.addRow(hlyt)

    def get_buttons(self,ch):
        #add_btn = QPushButton("+")
        add_btn = AddBtn(self)
        #delete_btn = QPushButton("-")
        delete_btn = DeleteBtn(self,ch)
        character_btn = InfoBtn(ch,self)
        return add_btn, delete_btn,character_btn

    def get_cha_lyt(self):
        return self.select_character_lyt
    
    def add_character(self):
        if len(self.characters) ==5:
            return
        name = "NUEVO PERSONAJE"
        new_C = Character(name=name,Map=self.Map)
        self.characters.append(new_C)
        add_btn,delete_btn,character_btn = self.get_buttons(new_C)
        hlyt = QHBoxLayout()
        hlyt.addWidget(add_btn)
        hlyt.addWidget(character_btn)
        hlyt.addWidget(delete_btn)
        self.select_character_lyt.addRow(hlyt)

    def delete_character(self,ch):
        if len(self.characters) > 1:
            for idx, e in enumerate(self.characters):
                if e == ch: 
                    w = self.select_character_lyt.itemAt(idx).layout()
                    self.select_character_lyt.removeRow(w)
                    self.characters.remove(e)
                    break
    
    def load_lands(self):
        self.images_lst.setViewMode(QListView.IconMode)    
        self.images_lst.setIconSize(QSize(50,50))   
        self.images_lst.setDragEnabled(True)
        paths = get_images()
        for path in paths: 
            x = path.split('/')
            name = x[-1]
            self.characters_paths.append(path)
            itm = QListWidgetItem(QIcon(path), name)
            self.images_lst.addItem(itm)

    def assign_actual_character(self,character):
        
        if self.actual_character != None:
            self.clear_lands(len(self.Map.get_available_lands()))
            if self.actual_character.is_configuration_complete():
                self.accept_btn.setEnabled(True)
        if self.actual_character == None:
            self.accept_btn.setDisabled(True)

        print(self.character_edit_lyt.itemAt(0).widget())
        print(self.character_edit_lyt.itemAt(1).widget())
        print(self.character_edit_lyt.itemAt(2).widget())
        print(self.character_edit_lyt.itemAt(3).widget())
        print(self.character_edit_lyt.itemAt(4).widget())

        self.actual_character = character
        if not self.actual_character.is_configuration_complete():
                self.accept_btn.setEnabled(False)
        
        self.name_txt.setText(self.actual_character.get_name())
        if self.actual_character.get_path() != None:
            self.image_lbl.setPixmap(QPixmap(self.actual_character.get_path()))
            self.image_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)       
            self.image_lbl.setScaledContents(True)
        if self.actual_character.get_path() == None:
            self.image_lbl.setText("Imagen")
        
        ch_map = self.actual_character.get_map()

        lands = ch_map.get_available_lands()
        print(self.character_edit_lyt.count())
        
        for e in lands: 
            land_lbl = self.generate_land_lbl(e)
            check_bx = CostChBx(self.actual_character,e, self, self.character_edit_lyt.count())
            cost_txt = CostTxt(self.actual_character,e,self)

            cost = self.actual_character.Map.get_cost_of_land(e)
            Hlyt = QHBoxLayout(self)
            Hlyt.addWidget(land_lbl)
            Hlyt.addStretch()
            Hlyt.addWidget(check_bx)
            Hlyt.addStretch()
            Hlyt.addWidget(cost_txt)
            self.character_edit_lyt.addRow(Hlyt)

            print("COSTO", cost)
            if cost == None:
               check_bx.setChecked(True)
               cost_txt.setDisabled(True)
            elif cost != "":
                cost_txt.setText(str(cost))

            
        print(lands)
        print(self.character_edit_lyt.count())

    def get_form(self):
        return self.character_edit_lyt

    def clear_lands(self,rows):
        print("LIMPIANDO")
        print(self.character_edit_lyt.itemAt(0))
        print(self.character_edit_lyt.itemAt(1))
        print(self.character_edit_lyt.itemAt(2))
        print(self.character_edit_lyt.itemAt(3))
        print(self.character_edit_lyt.itemAt(4))
        print(self.character_edit_lyt.itemAt(5))
        print(self.character_edit_lyt.itemAt(6))
        print(self.character_edit_lyt.itemAt(7))
        print("LIMPIANDO ITEMS")
        for _ in range(rows):
            widget = self.character_edit_lyt.itemAt(self.character_edit_lyt.count() - 1).layout()
            print(widget)
            self.character_edit_lyt.removeRow(widget)
        print("TERMINE")

    def generate_land_lbl(self, land):
        path = ""
        for path in self.land_path:
            if re.search(land,path):
                break
        print("PATHH " ,path)
        image_lbl = QLabel()
        image_lbl.setPixmap(QPixmap(path))
        image_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
        image_lbl.setMinimumHeight(50)
        image_lbl.setMinimumWidth(50)
        image_lbl.setMaximumWidth(50)
        image_lbl.setScaledContents(True)
        return image_lbl
        
    def on_listWidget_clicked(self): 
        if self.actual_character != None:
            data = self.images_lst.selectedItems()[0]
            name = data.text()
            print("Obtuve ", name)
            print("Buscando en  : ",self.characters_paths )
            for path in self.characters_paths:
                if re.search(name,path):
                    self.actual_character.set_path(path)
                    break
            print("ACTUALIZANDO PATH =  " , self.actual_character)
            self.image_lbl.setPixmap(QPixmap(self.actual_character.get_path()))
            self.image_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
            self.image_lbl.setScaledContents(True)

            if self.actual_character.is_configuration_complete():
                edit_lyt = self.get_form()
                field = edit_lyt.itemAt(0).widget()
                field.setEnabled(True) 
        
class CostTxt(QLineEdit):
    def __init__(self, character, name,MainWindow):
        super().__init__()
        self.setObjectName(name)
        self.MainWindow = MainWindow
        self.character = character
        print(self.character.get_name())
        self.textChanged.connect(self.text_changed)

    def text_changed(self):
        
        #if re.fullmatch(r"([0-9]+\x2e?[0-9]{0,2}|\x2e[0-9]{1,2})", self.text()):
        if re.fullmatch(r"(\s*[0-9]+\x2e?[0-9]{0,2}\s*|\s*\x2e[0-9]{1,2}\s*)", self.text()):
            print(self.objectName())
            print(self.character.get_name(), self.text())
            self.character.Map.generate_costs(self.objectName(),float(self.text()))
            if self.character.is_configuration_complete():
                edit_lyt = self.MainWindow.get_form()
                field = edit_lyt.itemAt(0).widget()
                field.setEnabled(True)
        else: 
            edit_lyt = self.MainWindow.get_form()
            field = edit_lyt.itemAt(0).widget()
            field.setDisabled(True)    

class CostChBx(QCheckBox):
    def __init__(self, character, name, MainWindow,idx):
        super().__init__()
        name = name + "_bx"
        self.setText("N/A")
        self.setObjectName(name)
        self.character = character
        self.MainWindow = MainWindow
        self.idx_lyt = idx
        self.stateChanged.connect(self.state_changed)

    def disable_txt_edit(self):
        edit_lyt = self.MainWindow.get_form()
        #edit_lyt = QFormLayout()
        print(self.idx_lyt)
        print(edit_lyt.itemAt(0))
        print(edit_lyt.itemAt(1))
        print(edit_lyt.itemAt(2))
        print(edit_lyt.itemAt(3))
        print(edit_lyt.itemAt(6))
        print(edit_lyt.itemAt(7))
        print(edit_lyt.itemAt(8))
        field = edit_lyt.itemAt(self.idx_lyt).layout()
        print(field.itemAt(0).widget())
        print(field.itemAt(1).widget())
        print(field.itemAt(2).widget())
        print(field.itemAt(3).widget())
        print(field.itemAt(4).widget())
        field = field.itemAt(field.count()-1).widget()
        field.setDisabled(True)

    def enable_txt_edit(self):
        edit_lyt = self.MainWindow.get_form()
        field = edit_lyt.itemAt(self.idx_lyt).layout()
        field = field.itemAt(field.count()-1).widget()
        field.setEnabled(True)
        field.setText("0")

    def state_changed(self):
        if self.isChecked():
            self.disable_txt_edit()
            land = self.objectName().replace("_bx","")
            self.character.Map.generate_costs(land,None)
        else:
            self.enable_txt_edit()
            land = self.objectName().replace("_bx","")
            #self.character.Map.generate_costs(land,0)
        if self.character.is_configuration_complete():
            edit_lyt = self.MainWindow.get_form()
            print("-------------")
            print(edit_lyt.itemAt(0).widget())
            print(edit_lyt.itemAt(1).widget())
            print(edit_lyt.itemAt(2).widget())
            print(edit_lyt.itemAt(3).widget())
            print(edit_lyt.itemAt(4).widget())
            field = edit_lyt.itemAt(0).widget()
            field.setEnabled(True)
        
class InfoBtn(QPushButton):
    def __init__(self,character,MainWindow):
        super().__init__(character.get_name()) 
        self.clicked.connect(self.get_info)
        self.character = character 
        self.MainWindow = MainWindow

    def get_info(self):
        print(self.character)
        #self.MainWindow.name_txt.setText(self.character.get_name())
        self.MainWindow.assign_actual_character(self.character)

class AddBtn(QPushButton):
    def __init__(self,MainWindow):
        super().__init__("+")
        self.window = MainWindow
        self.clicked.connect(self.add_newCharacter)
    
    def add_newCharacter(self):
        self.window.add_character()

class DeleteBtn(QPushButton):
    def __init__(self,MainWindow,character):
        super().__init__("-")
        self.window = MainWindow
        self.character = character
        self.clicked.connect(self.delete_character)
    
    def delete_character(self):
        self.window.delete_character(self.character)