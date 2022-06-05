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
        
        
        #PAGE HOME
        self.Page_home = QWidget()
        self.Page_home.setObjectName(u"Page_home")
        self.gridLayout = QGridLayout(self.Page_home)
        self.gridLayout.setObjectName(u"gridLayout")

        application_pages.addWidget(self.Page_home)
        
        #PAGE ORDERS
        self.Page_orders = QWidget()
        self.Page_orders.setObjectName(u"Page_orders")
        self.gridLayout = QGridLayout(self.Page_orders)
        self.gridLayout.setObjectName(u"gridLayout")

        application_pages.addWidget(self.Page_orders)
        
        #PAGE USER
        self.Page_user = QWidget()
        self.Page_user.setObjectName(u"Page_user")
        
        self.pageUserLayout = QVBoxLayout(self.Page_user)
        self.pageUserLayout.setObjectName(u"pageUserLayout")
        self.pageUserLayout.setContentsMargins(70,20,70,20)

        application_pages.addWidget(self.Page_user)

        #PAGE USERS
        self.Page_users = QWidget()
        self.Page_users.setObjectName(u"Page_users")
        
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
        
        self.menu_functions = functions.menu_functions.MenuFunctions("ADM")
        self.user_search = self.menu_functions.subm_adm_usuarios_pesquisar("")
        
        self.num_cards = len(self.user_search)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        
        self.pushButton=[1,2,3,4,5]
        self.label = [1,2,3,4,5]
        self.label_2 = [1,2,3,4,5]
        self.label_3 = [1,2,3,4,5]
        self.label_4 = [1,2,3,4,5]
        self.label_5 = [1,2,3,4,5]
        self.label_6 = [1,2,3,4,5]
        self.label_7 = [1,2,3,4,5]
        self.frame = [1,2,3,4,5]
        self.card_user= [1,2,3,4,5]
        
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

        self.retranslateUi(application_pages)
        QMetaObject.connectSlotsByName(application_pages)

    def inserir_cards(self):
        linha = 0
        coluna = 1
        for item in range(len(self.user_search)):
                self.card_user[item] = QFrame(self.Page_users)
                self.card_user[item].setObjectName(u"card_user[item]")
                self.card_user[item].setMinimumSize(QSize(200, 250))
                self.card_user[item].setMaximumSize(QSize(200, 250))
                self.card_user[item].setStyleSheet(u"background-color: rgb(149, 216, 255);\n""border-radius: 5px;")
                self.card_user[item].setFrameShape(QFrame.StyledPanel)
                self.card_user[item].setFrameShadow(QFrame.Raised)
                
                self.frame[item] = QFrame(self.card_user[item])
                self.frame[item].setObjectName(u"frame")
                self.frame[item].setGeometry(QRect(70, 15, 60, 60))
                self.frame[item].setStyleSheet("background-color: #282a36")  
                self.frame[item].setStyleSheet("background-image: url('gui/images/users/default_user.png')") 
                self.frame[item].setFrameShape(QFrame.StyledPanel)
                self.frame[item].setFrameShadow(QFrame.Raised)
                
                self.label[item] = QLabel(self.card_user[item])
                self.label[item].setObjectName(u"label")
                self.label[item].setGeometry(QRect(0, 75, 200, 26))
                self.label[item].setAlignment(Qt.AlignHCenter)
                self.label[item].setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n")
                self.label_3[item] = QLabel(self.card_user[item])
                self.label_3[item].setObjectName(u"label_3")
                self.label_3[item].setGeometry(QRect(10, 145, 51, 21))
                self.label_3[item].setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
                self.label_4[item] = QLabel(self.card_user[item])
                self.label_4[item].setObjectName(u"label_4")
                self.label_4[item].setGeometry(QRect(10, 175, 51, 21))
                self.label_4[item].setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
                
                self.pushButton[item] = QPushButton(self.card_user[item])
                self.pushButton[item].setObjectName(u"pushButton")
                self.pushButton[item].setGeometry(QRect(70, 210, 70, 25))
                self.pushButton[item].setStyleSheet(u"background-color: rgb(0, 144, 255);\n""color: rgb(255, 255, 255);\n""border-radius: 5px;\n""")
                
                self.label_5[item] = QLabel(self.card_user[item])
                self.label_5[item].setObjectName(u"label_5")
                self.label_5[item].setGeometry(QRect(10, 115, 51, 21))
                self.label_5[item].setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
                self.label_2[item] = QLabel(self.card_user[item])
                self.label_2[item].setObjectName(u"label_2")
                self.label_2[item].setGeometry(QRect(70, 115, 120, 21))
                self.label_2[item].setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""margin-left: 2px;")
                self.label_6[item] = QLabel(self.card_user[item])
                self.label_6[item].setObjectName(u"label_6")
                self.label_6[item].setGeometry(QRect(70, 145, 120, 21))
                self.label_6[item].setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""margin-left: 2px;")
                self.label_7[item] = QLabel(self.card_user[item])
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
        
        '''for item in range(len(self.user_search)):
            self.pushButton[item].clicked.connect(self.show_user_page)'''

    def remover_cards(self):
        for item in range(len(self.user_search)):
                self.gridLayout_3.removeWidget(self.card_user[item])
                self.card_user[item].deleteLater()
                self.card_user[item] = None

    def search(self):
        self.remover_cards()
        str = self.lineEdit.text()
        self.user_search = self.menu_functions.subm_adm_usuarios_pesquisar(str)
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
   
    
        
    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"USU\u00c1RIOS", None))
        self.show_card_labels()
    # retranslateUi


