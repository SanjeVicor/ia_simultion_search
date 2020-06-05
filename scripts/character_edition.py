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

from lands.load import get_images as lands_get_images

import platform


class CharacterEditionWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,Map = Map(), characters=list()):
        super(CharacterEditionWindow,self).__init__()
        self.setupUi(self)
        #self.land_path = land_Paths
        self.Map = Map
        
        self.characters = characters
        self.actual_character = None
        self.characters_paths = list()
        self.images_lst.setMinimumHeight(100)
        if len(characters) == 0:
            self.characters.append(Character(name="NUEVO PERSONAJE",Map=self.Map))
        else:
            for e in self.characters:
                e.make_new_copy_of_map(self.Map)
        self.load_characters_layout()
        self.load_characters()
        self.assign_events()
        
        SecundaryBtnStyleEnabled = "QPushButton:enabled{background-color:#343a40;border-radius:6px;color:#ffffff;font-family:Verdana;text-decoration:none;}" 
        PrimaryBtnStyleEnabled = "QPushButton:enabled{background-color:#4e73df;border-radius:6px;color:#ffffff;font-family:Verdana;text-decoration:none;}" 
        btnStyleDisabled = " QPushButton:disabled{background-color:#949494;border-radius:6px;font-family:Verdana;text-decoration:none; }"
        
        clickEffect = "QPushButton:pressed{border-style:solid;border-width:1px;}"

        self.accept_btn.setStyleSheet(btnStyleDisabled + PrimaryBtnStyleEnabled + clickEffect)
        self.go_back_btn.setStyleSheet(btnStyleDisabled + SecundaryBtnStyleEnabled + clickEffect)
        self.accept_btn.setDisabled(True)
        
        self.name_txt.setPlaceholderText("Nombre de personaje")
        self.name_txt.setMaxLength(15)

        self.setStyleSheet("font-family:Verdana;")
        self.showMaximized()

    def assign_events(self):
        self.name_txt.textChanged.connect(self.character_changed_textLine)
        self.images_lst.itemSelectionChanged.connect(self.on_listWidget_clicked)
        self.accept_btn.clicked.connect(self.allow_change)
        self.go_back_btn.clicked.connect(self.go_back)
        self.search_img_btn.clicked.connect(self.add_images)

    def add_images(self):
        file_name = QFileDialog.getOpenFileName(self,"Images (*.png *.xpm *.jpg)",'.', 'PNG((*.png)')
        if file_name[0] != '':
            path =file_name[0]
            name , path = copy_image(path)
            itm =  QListWidgetItem(QIcon(path),name)
            self.images_lst.addItem(itm)
            self.characters_paths.append(path)

    def go_back(self):
        from scripts.main_window import MainWindow
        
        for e in self.characters:
            e.clear_lands()

        self.edition = MainWindow(graph=self.Map, characters=self.characters)
        self.close()

    def allow_change(self): 
        self.actual_character.clear_visits()
        self.actual_character.Map.clear_visits()
        from scripts.simulation_configuration import SimulationConfiguration
        self.simulation = SimulationConfiguration(self.actual_character) 

    def modify_nameBtn(self,idx):
        group_btns = self.select_character_lyt.itemAt(idx).layout()
        btn = group_btns.itemAt(1).widget()
        char = self.characters[idx]
        btn.setText(char.get_name())
        
    def character_changed_textLine(self):
        self.actual_character.set_name(self.name_txt.text())
        for idx, e in enumerate(self.characters):
            if self.actual_character == e:
                self.modify_nameBtn(idx)
                break
            
    def load_characters_layout(self):
        for e in self.characters: 
            add_btn,delete_btn,character_btn = self.get_buttons(e)
            hlyt = QHBoxLayout()
            hlyt.addWidget(add_btn)
            hlyt.addWidget(character_btn)
            hlyt.addWidget(delete_btn)
            self.select_character_lyt.addRow(hlyt)

    def get_buttons(self,ch):
        add_btn = AddBtn(self)
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
                    if self.actual_character == e:
                        self.assign_actual_character(self.characters[0])
                    break
    
    def load_characters(self):
        self.images_lst.setViewMode(QListView.IconMode)    
        self.images_lst.setIconSize(QSize(50,50))   
        self.images_lst.setDragEnabled(True)
        paths = get_images()
        for path in paths: 
            x=''
            if platform.system() == "Windows":
                x =  path.split('\x5c')
            else:
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
        for e in lands: 
            land_lbl = self.generate_land_lbl(e)
            check_bx = CostChBx(self.actual_character,e, self, self.character_edit_lyt.count())
            cost_txt = CostTxt(self.actual_character,e,self)
            cost = self.actual_character.Map.get_cost_of_land(e)
            Hlyt = QHBoxLayout()
            Hlyt.addWidget(land_lbl)
            Hlyt.addStretch()
            Hlyt.addWidget(check_bx)
            Hlyt.addStretch()
            Hlyt.addWidget(cost_txt)
            self.character_edit_lyt.addRow(Hlyt)
            if cost == None:
               check_bx.setChecked(True)
               cost_txt.setDisabled(True)
            elif cost != "":
                cost_txt.setText(str(cost))

    def get_form(self):
        return self.character_edit_lyt
    
    def get_accept_btn(self):
        return self.accept_btn

    def clear_lands(self,rows):
        for _ in range(rows):
            widget = self.character_edit_lyt.itemAt(self.character_edit_lyt.count() - 1).layout()
            self.character_edit_lyt.removeRow(widget) 

    def generate_land_lbl(self, land):
        path = ""
        land_path = lands_get_images()
        if platform.system() == "Windows":
            for path in land_path:  
                if re.search(re.escape(land),re.escape(path)):
                    break
        else:
            for path in land_path:  
                if re.search(land,path):
                    break
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
            
            for path in self.characters_paths:
                if re.search(name,path):
                    self.actual_character.set_path(path)
                    break
            
            self.image_lbl.setPixmap(QPixmap(self.actual_character.get_path()))
            self.image_lbl.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
            self.image_lbl.setScaledContents(True)

            if self.actual_character.is_configuration_complete(): 
                field = self.get_accept_btn()
                field.setEnabled(True) 
        
class CostTxt(QLineEdit):
    def __init__(self, character, name,MainWindow):
        super().__init__()
        self.setObjectName(name)
        self.MainWindow = MainWindow
        self.character = character
        
        self.textChanged.connect(self.text_changed)

    def text_changed(self):
        if re.fullmatch(r"(\s*[0-9]+\x2e?[0-9]*\s*|\s*\x2e[0-9]+\s*)", self.text()):            
            self.character.Map.generate_costs(self.objectName(),float(self.text()))
            if self.character.is_configuration_complete(): 
                field = self.MainWindow.get_accept_btn()
                field.setEnabled(True)
        else: 
            field = self.MainWindow.get_accept_btn()
            field.setEnabled(True)
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
        field = edit_lyt.itemAt(self.idx_lyt).layout()
        field = field.itemAt(field.count()-1).widget()
        field.setText("")
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
        if self.character.is_configuration_complete():
            field = self.MainWindow.get_accept_btn()
            field.setEnabled(True)

class InfoBtn(QPushButton):
    def __init__(self,character,MainWindow):
        super().__init__(character.get_name()) 
        infoStyle="QPushButton{background-color:#6c757d; color:#ffffff; }" 
        self.setStyleSheet(infoStyle)
        self.clicked.connect(self.get_info)
        self.character = character 
        self.MainWindow = MainWindow

    def get_info(self):
        self.MainWindow.assign_actual_character(self.character)

class AddBtn(QPushButton):
    def __init__(self,MainWindow):
        super().__init__("+")
        addStyle ="QPushButton{background-color:rgb(40, 167, 69);color:#ffffff; }" 
        self.setStyleSheet(addStyle)
        self.window = MainWindow
        self.clicked.connect(self.add_newCharacter)
    
    def add_newCharacter(self):
        self.window.add_character()

class DeleteBtn(QPushButton):
    def __init__(self,MainWindow,character):
        super().__init__("-")
        deleteStyle = "QPushButton{background-color:rgb(220, 53, 69);  color:#ffffff;}"
        self.setStyleSheet(deleteStyle)
        self.window = MainWindow
        self.character = character
        self.clicked.connect(self.delete_character)
    
    def delete_character(self):
        self.window.delete_character(self.character)