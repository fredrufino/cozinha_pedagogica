# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesErigwH.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
#IMPORTS


import os
import time
from functools import partial

#IMPORT QT CORE
from qt_core import *

# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton
import functions.menu_functions

class Ui_application_adm_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(769, 484)

        #APARÊNCIA BOTÕES *******************************************************************************
        self.style_save_btn = f"""
        QPushButton {{
            color: #FFFFFF;
            background-color: #008037;
            border-radius: 9px;
            font-family: "Impact";
        }}
         QPushButton:hover {{
            background-color: #0E6935;
        }}
        QPushButton:pressed {{
            background-color: #0E6935;
        }}
        """
        self.style_cancel_btn = f"""
        QPushButton {{
            color: #FFFFFF;
            background-color: #FF0000;
            border-radius: 9px;
            font-family: "Impact";
        }}
         QPushButton:hover {{
            background-color: #D70E0E;
        }}
        QPushButton:pressed {{
            background-color: #D70E0E;
        }}
        """
        self.style_load_btn = f"""
        QPushButton {{
            color: #FFFFFF;
            background-color: #004AAD;
            border-radius: 5px;
            font:  8pt \"Impact\";
            
        }}
         QPushButton:hover {{
            background-color: #0C4693;
        }}
        QPushButton:pressed {{
            background-color: #0C4693;
        }}
        """
        self.style_remove_btn = f"""
        QPushButton {{
            color: #FFFFFF;
            background-color: #FF0000;
            border-radius: 5px;
            font:  8pt \"Impact\";
            
        }}
         QPushButton:hover {{
            background-color: #D70E0E;
        }}
        QPushButton:pressed {{
            background-color: #D70E0E;
        }}
        """
        
        #FIM APARÊNCIA BOTÕES ***************************************************************************
        

        #PÁGINA PRINCIPAL ********************************************************************************
        self.Page_home = QWidget()
        self.Page_home.setObjectName(u"Page_home")

        #CRIANDO LAYOUT DA PÁGINA PRINCIPAL
        self.gridLayout_page_home = QGridLayout(self.Page_home)
        self.gridLayout_page_home.setObjectName(u"gridLayout_page_home")
        self.gridLayout_page_home.setContentsMargins(50,50,50,50)
        self.gridLayout_page_home.setSpacing(0) 

        application_pages.addWidget(self.Page_home)
        
        #CRIANDO A SIZEPOLICY
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.verticalLayout_aceso_ultimas = QVBoxLayout()
        self.verticalLayout_aceso_ultimas.setSpacing(0)
        self.verticalLayout_aceso_ultimas.setObjectName(u"verticalLayout_aceso_ultimas")

        #ACESSO RÁPIDO
        self.acesso_rapido = QFrame(self.Page_home)
        self.acesso_rapido.setObjectName(u"acesso_rapido")
        self.acesso_rapido.setMinimumSize(QSize(100, 140))
        self.acesso_rapido.setMaximumSize(QSize(16777215, 140))
        self.acesso_rapido.setStyleSheet(u"background-color: rgb(240, 250, 255);")
        self.acesso_rapido.setFrameShape(QFrame.StyledPanel)
        self.acesso_rapido.setFrameShadow(QFrame.Raised)

        self.acesso_rapido_label = QLabel(self.acesso_rapido)
        self.acesso_rapido_label.setObjectName(u"acesso_rapido_label")
        self.acesso_rapido_label.setGeometry(QRect(30, 15, 141, 21))
        self.acesso_rapido_label.setStyleSheet(u"font: 700 12pt \"Berlin Sans FB Demi\";")
        
        self.register_user_btn = PyPushButton(
            is_btn_page= True,
            heigth= 85,
            btn_border= 5,
            btn_color= "rgb(214, 240, 255)"
    
        )
        self.register_user_btn = QPushButton(self.acesso_rapido, PyPushButton(
            btn_color="black"
        ))

        self.register_user_btn.setMaximumWidth(80)
        #self.register_user_btn.setM


        

        self.pushButton_2 = QPushButton(self.acesso_rapido)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(123, 40, 80, 85))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(214, 240, 255);")
        self.pushButton_3 = QPushButton(self.acesso_rapido)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(216, 40, 80, 85))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(214, 240, 255);")
        self.pushButton_4 = QPushButton(self.acesso_rapido)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(309, 40, 80, 85))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(214, 240, 255);")

        self.verticalLayout_aceso_ultimas.addWidget(self.acesso_rapido, 0, Qt.AlignTop)


        #CRIANDO FRAME DETALHES
        self.detalhes = QFrame(self.Page_home)
        self.detalhes.setObjectName(u"detalhes")
        sizePolicy.setHeightForWidth(self.detalhes.sizePolicy().hasHeightForWidth())
        self.detalhes.setSizePolicy(sizePolicy)
        self.detalhes.setMinimumSize(QSize(250, 300))
        self.detalhes.setMaximumSize(QSize(300, 500))
        self.detalhes.setStyleSheet(u"background-color: rgb(240, 250, 255);") 
        self.detalhes.setFrameShape(QFrame.StyledPanel)
        self.detalhes.setFrameShadow(QFrame.Raised)

        self.detalhes_label = QLabel(self.detalhes)
        self.detalhes_label.setObjectName(u"detalhes_label")
        self.detalhes_label.setGeometry(QRect(30, 15, 71, 21))
        self.detalhes_label.setStyleSheet(u"font: 700 12pt \"Berlin Sans FB Demi\";")

        #ADICIONANDO DETALHES AO LAYOUT
        self.gridLayout_page_home.addWidget(self.detalhes, 1, 2, 1, 1)


        #CRIANDO FRAME ULTIMAS ALTEAÇÕES
        self.ultimas_alterações = QFrame(self.Page_home)
        self.ultimas_alterações.setObjectName(u"ultimas_alterações")
        self.ultimas_alterações.setMaximumSize(QSize(16777215, 230))
        self.ultimas_alterações.setStyleSheet(u"\n""background-color: rgb(240, 250, 255);")
        self.ultimas_alterações.setFrameShape(QFrame.StyledPanel)
        self.ultimas_alterações.setFrameShadow(QFrame.Raised)
        self.ultimas_alteracoes_label = QLabel(self.ultimas_alterações)
        self.ultimas_alteracoes_label.setObjectName(u"ultimas_alteracoes_label")
        self.ultimas_alteracoes_label.setGeometry(QRect(30, 15, 181, 21))
        self.ultimas_alteracoes_label.setStyleSheet(u"font: 700 12pt \"Berlin Sans FB Demi\";")
        
        #CRIANDO O WIDGET DAS ULTIMAS ALTERAÇÕE
        self.gridLayoutWidget_ultimas_alteracoes = QWidget(self.ultimas_alterações)
        self.gridLayoutWidget_ultimas_alteracoes.setObjectName(u"gridLayoutWidget_ultimas_alteracoes")
        self.gridLayoutWidget_ultimas_alteracoes.setGeometry(QRect(10, 70, 361, 151))

        self.gridLayout_ultimas_alteracoes = QGridLayout(self.gridLayoutWidget_ultimas_alteracoes)
        self.gridLayout_ultimas_alteracoes.setObjectName(u"gridLayout_ultimas_alteracoes")
        self.gridLayout_ultimas_alteracoes.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_aceso_ultimas.addWidget(self.ultimas_alterações)

        self.gridLayout_page_home.addLayout(self.verticalLayout_aceso_ultimas, 1, 0, 1, 1)

        #CRIANDO ESPAÇÃMENTO PARA DEIXAR CEBTRALIZADO
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_page_home.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        #FIM PÁGINA PRINCIPAL ****************************************************************************


        #PÁGINA USUÁRIOS *********************************************************************************
        self.Page_users = QWidget()
        self.Page_users.setObjectName(u"Page_users")
        
        #CRIANDO O LAYOUT DA PÁGINA DE USUÁRIOS
        self.pageUsersLayout = QVBoxLayout(self.Page_users)
        self.pageUsersLayout.setObjectName(u"pageUsersLayout")
        self.pageUsersLayout.setContentsMargins(70,20,70,20)

        application_pages.addWidget(self.Page_users)
        
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_8 = QLabel(self.Page_users)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: black;\n""font: 700 22pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_8)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.line = QFrame(self.Page_users)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(149, 216, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)
        self.pageUsersLayout.addLayout(self.verticalLayout)
        
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.setContentsMargins(0,20,0,20)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.lineEdit = QLineEdit(self.Page_users)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(150, 30))
        self.lineEdit.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_3.addWidget(self.lineEdit)
        
        self.pushButton_2 = QPushButton(self.Page_users)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(30, 30))
        self.pushButton_2.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_2.clicked.connect(self.search)

        self.pageUsersLayout.addLayout(self.horizontalLayout_3)
        
        #RESOLVER PROBLEMA - ADM
        self.menu_functions = functions.menu_functions.MenuFunctions("ADM")
        self.user_search = self.menu_functions.search("USUARIO-ALL", "")        
        
        self.num_cards = len(self.user_search)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        
        

        """self.pushButton=[1,2,3,4,5]
        self.label = [1,2,3,4,5]
        self.label_2 = [1,2,3,4,5]
        self.label_3 = [1,2,3,4,5]
        self.label_4 = [1,2,3,4,5]
        self.label_5 = [1,2,3,4,5]
        self.label_6 = [1,2,3,4,5]
        self.label_7 = [1,2,3,4,5]
        self.frame = [1,2,3,4,5]
        self.card_user= [1,2,3,4,5]"""
        
        ''' image = "default_user.png"
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/users"
        path = os.path.join(app_path, folder)
        image_path = os.path.normpath(os.path.join(path, image))
        url = folder + image_path'''
        
        self.inserir_cards()
        
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)
        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 5, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.pageUsersLayout.addLayout(self.verticalLayout_2)

        #FIM PÁGINA USUÁRIOS *****************************************************************************

        #PÁGINA CADASTRAR USUÁRIO ************************************************************************
        self.Page_registration = QWidget()
        self.Page_registration.setObjectName(u"Page_registration")
        
        #CRIANDO O LAYOUT DA PÁGINA DE USUÁRIOS
        self.pageRegistrationLayout = QVBoxLayout(self.Page_registration)
        self.pageRegistrationLayout.setObjectName(u"pageRegistrationLayout")
        self.pageRegistrationLayout.setContentsMargins(50, 20, 50, 50)
        self.pageRegistrationLayout.setSpacing(0)

        application_pages.addWidget(self.Page_registration)
        
        #verticalLayout_3 = pageRegistrationLayout
        #horizontalLayout = title_registrationLayout
        #verticalLayout_4 = dataLayout
        #horizontalLayout_2 = dataLayout_1
        
        self.title_registrationLayout = QVBoxLayout()
        self.title_registrationLayout.setObjectName(u"title_registrationLayout")
        self.Spacer_top_title = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.title_registrationLayout.addItem(self.Spacer_top_title)

        self.label_title_registration = QLabel(self.Page_registration)
        self.label_title_registration.setObjectName(u"label_title_registration")
        self.label_title_registration.setStyleSheet(u"color: black;\n""font: 700 22pt \"Segoe UI\";")

        self.title_registrationLayout.addWidget(self.label_title_registration)

        self.Spacer_bottom_title = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.title_registrationLayout.addItem(self.Spacer_bottom_title)

        self.line_registration = QFrame(self.Page_registration)
        self.line_registration.setObjectName(u"line_registration")
        self.line_registration.setStyleSheet(u"background-color: rgb(149, 216, 255);")
        self.line_registration.setFrameShape(QFrame.HLine)
        self.line_registration.setFrameShadow(QFrame.Sunken)

        self.title_registrationLayout.addWidget(self.line_registration)
        self.pageRegistrationLayout.addLayout(self.title_registrationLayout)

        self.dataLayout = QVBoxLayout()
        self.dataLayout.setSpacing(0)
        self.dataLayout.setObjectName(u"dataLayout")
        self.Spacer_top_data = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.dataLayout.addItem(self.Spacer_top_data)

        self.dataLayout_1 = QHBoxLayout()
        self.dataLayout_1.setSpacing(0)
        self.dataLayout_1.setObjectName(u"dataLayout_1")
        self.Spacer_left_data = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dataLayout_1.addItem(self.Spacer_left_data)

        self.frame_data_registration = QFrame(self.Page_registration)
        self.frame_data_registration.setObjectName(u"frame_data_registration")
        self.frame_data_registration.setMinimumSize(QSize(800, 400))
        self.frame_data_registration.setStyleSheet(u"")
        self.frame_data_registration.setFrameShape(QFrame.StyledPanel)
        self.frame_data_registration.setFrameShadow(QFrame.Raised)
        
        self.save_registration_btn = QPushButton(self.frame_data_registration)
        self.save_registration_btn.setObjectName(u"save_registration_btn")
        self.save_registration_btn.setGeometry(QRect(255, 350, 140, 24))
        self.save_registration_btn.setMinimumHeight(45)
        self.save_registration_btn.setStyleSheet(self.style_save_btn)
        
        self.label_registration_subtitle = QLabel(self.frame_data_registration)
        self.label_registration_subtitle.setObjectName(u"label_registration_subtitle")
        self.label_registration_subtitle.setGeometry(QRect(319, 5, 161, 31))
        self.label_registration_subtitle.setMinimumSize(QSize(161, 31))
        self.label_registration_subtitle.setMaximumSize(QSize(161, 31))
        self.label_registration_subtitle.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.label_registration_subtitle.setAlignment(Qt.AlignCenter)
        
        self.label_registration_email = QLabel(self.frame_data_registration)
        self.label_registration_email.setObjectName(u"label_registration_email")
        self.label_registration_email.setGeometry(QRect(70, 180, 80, 16))
        self.label_registration_email.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        
        self.label_registration_birth = QLabel(self.frame_data_registration)
        self.label_registration_birth.setObjectName(u"label_registration_birth")
        self.label_registration_birth.setGeometry(QRect(70, 140, 80, 16))
        self.label_registration_birth.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        
        self.label_registration_phone = QLabel(self.frame_data_registration)
        self.label_registration_phone.setObjectName(u"label_registration_phone")
        self.label_registration_phone.setGeometry(QRect(70, 220, 80, 16))
        self.label_registration_phone.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        
        self.label_registration_lastName = QLabel(self.frame_data_registration)
        self.label_registration_lastName.setObjectName(u"label_registration_lastName")
        self.label_registration_lastName.setGeometry(QRect(70, 100, 80, 16))
        self.label_registration_lastName.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        
        self.label_registration_state = QLabel(self.frame_data_registration)
        self.label_registration_state.setObjectName(u"label_registration_state")
        self.label_registration_state.setGeometry(QRect(470, 60, 80, 16))
        self.label_registration_state.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        
        self.label_registration_road = QLabel(self.frame_data_registration)
        self.label_registration_road.setObjectName(u"label_registration_road")
        self.label_registration_road.setGeometry(QRect(470, 140, 80, 16))
        self.label_registration_road.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        
        self.label_registration_city = QLabel(self.frame_data_registration)
        self.label_registration_city.setObjectName(u"label_registration_city")
        self.label_registration_city.setGeometry(QRect(470, 100, 80, 16))
        self.label_registration_city.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        
        self.label_registration_district = QLabel(self.frame_data_registration)
        self.label_registration_district.setObjectName(u"label_registration_district")
        self.label_registration_district.setGeometry(QRect(470, 180, 80, 16))
        self.label_registration_district.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.lineEdit_registration_name = QLineEdit(self.frame_data_registration)
        self.lineEdit_registration_name.setObjectName(u"lineEdit_registration_name")
        self.lineEdit_registration_name.setGeometry(QRect(150, 50, 180, 31))
        self.lineEdit_registration_lastName = QLineEdit(self.frame_data_registration)
        self.lineEdit_registration_lastName.setObjectName(u"lineEdit_registration_lastName")
        self.lineEdit_registration_lastName.setGeometry(QRect(150, 90, 180, 31))
        self.lineEdit_registration_email = QLineEdit(self.frame_data_registration)
        self.lineEdit_registration_email.setObjectName(u"lineEdit_registration_email")
        self.lineEdit_registration_email.setGeometry(QRect(150, 170, 180, 31))
        self.lineEdit_registration_phone = QLineEdit(self.frame_data_registration)
        self.lineEdit_registration_phone.setObjectName(u"lineEdit_registration_phone")
        self.lineEdit_registration_phone.setGeometry(QRect(150, 210, 180, 31))
        self.lineEdit_registration_district = QLineEdit(self.frame_data_registration)
        self.lineEdit_registration_district.setObjectName(u"lineEdit_registration_district")
        self.lineEdit_registration_district.setGeometry(QRect(550, 170, 180, 31))
        self.lineEdit_registration_road = QLineEdit(self.frame_data_registration)
        self.lineEdit_registration_road.setObjectName(u"lineEdit_registration_road")
        self.lineEdit_registration_road.setGeometry(QRect(550, 130, 180, 31))
        
        self.cancel_registration_btn = QPushButton(self.frame_data_registration)
        self.cancel_registration_btn.setObjectName(u"cancel_registration_btn")
        self.cancel_registration_btn.setGeometry(QRect(425, 350, 140, 24))
        self.cancel_registration_btn.setMinimumHeight(45)
        self.cancel_registration_btn.setStyleSheet(self.style_cancel_btn)
        
        self.frame_image_registration = QFrame(self.frame_data_registration)
        self.frame_image_registration.setObjectName(u"frame_image_registration")
        self.frame_image_registration.setGeometry(QRect(70, 260, 60, 60))
        self.frame_image_registration.setStyleSheet(u"background-color: rgb(0, 85, 255);\n""border-radius: 30px;")
        self.frame_image_registration.setFrameShape(QFrame.StyledPanel)
        self.frame_image_registration.setFrameShadow(QFrame.Raised)
        
        self.label_registration_actualPicture = QLabel(self.frame_data_registration)
        self.label_registration_actualPicture.setObjectName(u"label_registration_actualPicture")
        self.label_registration_actualPicture.setGeometry(QRect(140, 270, 71, 16))
        self.label_registration_actualPicture.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        
        self.load_registration_btn = QPushButton(self.frame_data_registration)
        self.load_registration_btn.setObjectName(u"load_registration_btn")
        self.load_registration_btn.setGeometry(QRect(140, 300, 61, 21))
        self.load_registration_btn.setMinimumHeight(15)
        self.load_registration_btn.setStyleSheet(self.style_load_btn)
        
        self.remove_registration_btn = QPushButton(self.frame_data_registration)
        self.remove_registration_btn.setObjectName(u"remove_registration_btn")
        self.remove_registration_btn.setGeometry(QRect(210, 300, 61, 21))
        self.remove_registration_btn.setMinimumHeight(15)
        self.remove_registration_btn.setStyleSheet(self.style_remove_btn)
        
        self.label_registration_nameActualPicture = QLabel(self.frame_data_registration)
        self.label_registration_nameActualPicture.setObjectName(u"label_registration_nameActualPicture")
        self.label_registration_nameActualPicture.setGeometry(QRect(210, 270, 71, 16))
        self.label_registration_nameActualPicture.setStyleSheet(u"")
        
        self.dateEdit_registration_birth = QDateEdit(self.frame_data_registration)
        self.dateEdit_registration_birth.setObjectName(u"dateEdit_registration_birth")
        self.dateEdit_registration_birth.setGeometry(QRect(150, 130, 180, 31))
        
        self.comboBox_registration_state = QComboBox(self.frame_data_registration)
        self.comboBox_registration_state.setObjectName(u"comboBox_registration_state")
        self.comboBox_registration_state.setGeometry(QRect(550, 50, 180, 31))
        
        self.comboBox_registration_state.addItem(f"----------")
        self.states = self.menu_functions.search("ESTADO", "")
        
        for item in range(len(self.states)):
            self.comboBox_registration_state.addItem(f"{self.states[item][0]}")
    

        self.comboBox_registration_city = QComboBox(self.frame_data_registration)
        self.comboBox_registration_city.setObjectName(u"comboBox_registration_city")
        self.comboBox_registration_city.setGeometry(QRect(550, 90, 180, 31))

        self.comboBox_registration_state.activated.connect(self.search_citys)
        
        self.label_registration_post = QLabel(self.frame_data_registration)
        self.label_registration_post.setObjectName(u"label_registration_post")
        self.label_registration_post.setGeometry(QRect(470, 220, 80, 16))
        self.label_registration_post.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")
        
        self.comboBox_registration_post = QComboBox(self.frame_data_registration)
        self.comboBox_registration_post.addItem("Administrador")
        self.comboBox_registration_post.addItem("Cozinheiro")
        self.comboBox_registration_post.addItem("Estoquista")
        self.comboBox_registration_post.setObjectName(u"comboBox_registration_post")
        self.comboBox_registration_post.setGeometry(QRect(550, 210, 180, 31))
        
        self.label_registration_name = QLabel(self.frame_data_registration)
        self.label_registration_name.setObjectName(u"label_registration_name")
        self.label_registration_name.setGeometry(QRect(70, 60, 80, 16))
        self.label_registration_name.setStyleSheet(u"font: 700 10pt \"Segoe UI\";")

        self.dataLayout_1.addWidget(self.frame_data_registration)

        self.Spacer_right_data = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dataLayout_1.addItem(self.Spacer_right_data)

        self.dataLayout.addLayout(self.dataLayout_1)

        self.pageRegistrationLayout.addLayout(self.dataLayout)

        self.Spacer_bottom_data = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.pageRegistrationLayout.addItem(self.Spacer_bottom_data)
        
        


        self.save_registration_btn.clicked.connect(self.register_user)
        #print(self.lineEdit_registration_name.text())
    
        #FIM PÁGINA CADASTRAR USUÁRIO ********************************************************************

        #PÁGINA ALTERAR USUÁRIO **************************************************************************
        #FIM PÁGINA ALTERAR USUÁRIO **********************************************************************


        self.retranslateUi(application_pages)
        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    

    #FUNÇÕES DA PÁGINA DE USUÁRIOS
    def inserir_cards(self):
        linha = 0
        coluna = 1

        self.pushButton=[]
        self.label = []
        self.label_2 = []
        self.label_3 = []
        self.label_4 = []
        self.label_5 = []
        self.label_6 = []
        self.label_7 = []
        self.frame = []
        self.card_user= []

        for item in range(len(self.user_search)):
                
                self.card_user.append(QFrame(self.Page_users))
                self.card_user[item].setObjectName(u"card_user")
                self.card_user[item].setMinimumSize(QSize(200, 250))
                self.card_user[item].setMaximumSize(QSize(200, 250))
                self.card_user[item].setStyleSheet(u"background-color: rgb(149, 216, 255);\n""border-radius: 5px;")
                self.card_user[item].setFrameShape(QFrame.StyledPanel)
                self.card_user[item].setFrameShadow(QFrame.Raised)
                
                self.frame.append(QFrame(self.card_user[item]))
                self.frame[item].setObjectName(u"frame")
                self.frame[item].setGeometry(QRect(70, 15, 60, 60))
                self.frame[item].setStyleSheet("background-color: #282a36")  
                self.frame[item].setStyleSheet("background-image: url('gui/images/users/default_user.png')") 
                self.frame[item].setFrameShape(QFrame.StyledPanel)
                self.frame[item].setFrameShadow(QFrame.Raised)
                
                self.label.append(QLabel(self.card_user[item]))
                self.label[item].setObjectName(u"label")
                self.label[item].setGeometry(QRect(0, 75, 200, 26))
                self.label[item].setAlignment(Qt.AlignHCenter)
                self.label[item].setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n")

                self.label_3.append(QLabel(self.card_user[item]))
                self.label_3[item].setObjectName(u"label_3")
                self.label_3[item].setGeometry(QRect(10, 145, 51, 21))
                self.label_3[item].setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

                self.label_4.append(QLabel(self.card_user[item]))
                self.label_4[item].setObjectName(u"label_4")
                self.label_4[item].setGeometry(QRect(10, 175, 51, 21))
                self.label_4[item].setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
                
                self.pushButton.append(QPushButton(self.card_user[item]))
                self.pushButton[item].setObjectName(u"pushButton")
                self.pushButton[item].setGeometry(QRect(70, 210, 70, 25))
                self.pushButton[item].setStyleSheet(u"background-color: rgb(0, 144, 255);\n""color: rgb(255, 255, 255);\n""border-radius: 5px;\n""")

                self.label_5.append(QLabel(self.card_user[item]))
                self.label_5[item].setObjectName(u"label_5")
                self.label_5[item].setGeometry(QRect(10, 115, 51, 21))
                self.label_5[item].setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

                self.label_2.append(QLabel(self.card_user[item]))
                self.label_2[item].setObjectName(u"label_2")
                self.label_2[item].setGeometry(QRect(70, 115, 120, 21))
                self.label_2[item].setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""margin-left: 2px;")
                
                self.label_6.append(QLabel(self.card_user[item]))
                self.label_6[item].setObjectName(u"label_6")
                self.label_6[item].setGeometry(QRect(70, 145, 120, 21))
                self.label_6[item].setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""margin-left: 2px;")
                
                self.label_7.append(QLabel(self.card_user[item]))
                self.label_7[item].setObjectName(u"label_7")
                self.label_7[item].setGeometry(QRect(70, 175, 120, 21))
                self.label_7[item].setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""margin-left: 2px;")
                
                if coluna == 5:
                        coluna = 1
                        linha = linha +1 
                self.gridLayout_3.addWidget(self.card_user[item], linha, coluna, 1, 1)
                coluna = coluna + 1
        self.pageUsersLayout.addLayout(self.gridLayout_3)
        self.show_card_labels()
        
        for item in range(len(self.user_search)):
            self.pushButton[item].clicked.connect(partial(self.show_user_page, self.user_search[item]))

    def remover_cards(self):
        for item in range(len(self.user_search)):
                self.gridLayout_3.removeWidget(self.card_user[item])
                self.card_user[item].deleteLater()
                self.card_user[item] = None

    def search(self):
        self.remover_cards()
        str = self.lineEdit.text()
        print(str)
        self.user_search = self.menu_functions.search("USUARIO-ALL", str)
        
        self.inserir_cards()
    
    def show_card_labels(self):
        for item in range(len(self.user_search)):
            self.label[item].setText(QCoreApplication.translate("Form", f"{self.user_search[item][1].strip().split(' ')[0]}", None))
            self.label_3[item].setText(QCoreApplication.translate("Form", u"Idade:", None))
            self.label_4[item].setText(QCoreApplication.translate("Form", u"Cargo:", None))
            self.pushButton[item].setText(QCoreApplication.translate("Form", u"Vizualizar", None))
            self.label_5[item].setText(QCoreApplication.translate("Form", u"Nome:", None))
            self.label_2[item].setText(QCoreApplication.translate("Form", f"{self.user_search[item][1]}", None))
            self.label_6[item].setText(QCoreApplication.translate("Form", u"19", None))
            self.label_7[item].setText(QCoreApplication.translate("Form", f"{self.user_search[item][2]}", None))         
    

    def show_user_page(self, user):
        print(user)
    #FIM FUNÇÕES DA PÁGINA DE USUÁRIOS

    #FUNÇÕES DA PÁGINA CADASTRO DE USUÁRIOS
    def search_citys(self):
        index_state = self.comboBox_registration_state.currentIndex()
        self.uf = self.states[index_state-1][1]
        self.citys = self.menu_functions.search("MUNICIPIO",self.uf)

        self.comboBox_registration_city.clear()
        
        for item in range(len(self.citys)):
            self.comboBox_registration_city.addItem(f"{self.citys[item][0]}")

    def register_user(self):
        name = self.lineEdit_registration_name.text(),
        Last_name = self.lineEdit_registration_lastName.text(),
        birth = self.dateEdit_registration_birth.date(),
        #birth = birth.toPython()
        email = self.lineEdit_registration_email.text(),
        phone = self.lineEdit_registration_phone.text(),
        state = self.comboBox_registration_state.currentText(),
        city = self.comboBox_registration_city.currentText(),
        district = self.lineEdit_registration_district.text(),
        road =  self.lineEdit_registration_road.text(),
        post = self.comboBox_registration_post.currentText()

        user = (name, Last_name, birth, email, phone, state, city, district, road, post)
        self.menu_functions.insert("USUARIO", user) 
        #print(user)
        
    
    
    
        
    #FIM FUNÇÕES DA PÁGINA CADASTRO DE USUÁRIOS


    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.acesso_rapido_label.setText(QCoreApplication.translate("Form", u"Acesso r\u00e1pido", None))
        self.detalhes_label.setText(QCoreApplication.translate("Form", u"Detalhes", None))
        self.ultimas_alteracoes_label.setText(QCoreApplication.translate("Form", u"\u00daltimas altera\u00e7\u00f5es", None))
        
        #REGISTER
        self.label_title_registration.setText(QCoreApplication.translate("Form", u"CADASTRO DE USU\u00c1RIO", None))
        
        self.save_registration_btn.setText(QCoreApplication.translate("Form", u"Cadastrar", None))
        self.cancel_registration_btn.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.load_registration_btn.setText(QCoreApplication.translate("Form", u"Carregar", None))
        self.remove_registration_btn.setText(QCoreApplication.translate("Form", u"Remover", None))
        
        self.label_registration_subtitle.setText(QCoreApplication.translate("Form", u"Dados pessoais:", None))
        self.label_registration_email.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.label_registration_birth.setText(QCoreApplication.translate("Form", u"Data Nasc:", None))
        self.label_registration_phone.setText(QCoreApplication.translate("Form", u"Celular:", None))
        self.label_registration_lastName.setText(QCoreApplication.translate("Form", u"Sobrenome:", None))
        self.label_registration_state.setText(QCoreApplication.translate("Form", u"Estado:", None))
        self.label_registration_road.setText(QCoreApplication.translate("Form", u"Rua:", None))
        self.label_registration_city.setText(QCoreApplication.translate("Form", u"Cidade:", None))
        self.label_registration_district.setText(QCoreApplication.translate("Form", u"Bairro:", None))
        self.label_registration_actualPicture.setText(QCoreApplication.translate("Form", u"Foto atual:", None))
        self.label_registration_nameActualPicture.setText(QCoreApplication.translate("Form", u"foto.png", None))
        self.label_registration_post.setText(QCoreApplication.translate("Form", u"Cargo:", None))
        self.label_registration_name.setText(QCoreApplication.translate("Form", u"Nome:", None))
    # retranslateUi
        
        