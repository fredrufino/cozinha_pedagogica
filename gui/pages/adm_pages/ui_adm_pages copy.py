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
        self.gridLayout.setContentsMargins(0,0,0,0)
        self.gridLayout.setSpacing(0) 

        application_pages.addWidget(self.Page_home)
        
        self.acesso_rapido = QFrame(self.Page_home)
        self.acesso_rapido.setObjectName(u"acesso_rapido")
        self.acesso_rapido.setMaximumSize(QSize(514, 140))
        self.acesso_rapido.setMinimumSize(QSize(514, 140))
        self.acesso_rapido.setStyleSheet(u"background-color: rgb(240, 250, 255);")
        self.acesso_rapido.setFrameShape(QFrame.StyledPanel)
        self.acesso_rapido.setFrameShadow(QFrame.Raised)
        
        self.label_acesso_rapido = QLabel(self.acesso_rapido)
        self.label_acesso_rapido.setObjectName(u"label_acesso_rapido")
        self.label_acesso_rapido.setGeometry(QRect(30, 15, 141, 21))
        self.label_acesso_rapido.setStyleSheet(u"font: 700 12pt \"Berlin Sans FB Demi\";")
        
        self.cadastrar_usuario = QPushButton(self.acesso_rapido)
        '''self.cadastrar_usuario = PyPushButton(
                text= "Cadastrar usuário",
                icon_path= "icon_home.svg",
                icon_color= "#1D9EE8" ,
                btn_color=  "#D6F0FF"     
            )'''
        self.cadastrar_usuario.setGeometry(QRect(123, 40, 80, 85))
        
        self.gridLayout.addWidget(self.acesso_rapido, 0, 0, 1, 1)
        
        self.detalhes = QFrame(self.Page_home)
        self.detalhes.setObjectName(u"detalhes")
        self.detalhes.setMinimumSize(QSize(250, 200))
        self.detalhes.setMaximumSize(QSize(250, 400))
        self.detalhes.setStyleSheet(u"background-color: rgb(240, 250, 255);")
        self.detalhes.setFrameShape(QFrame.StyledPanel)
        self.detalhes.setFrameShadow(QFrame.Raised)
        self.label_detalhes = QLabel(self.detalhes)
        self.label_detalhes.setObjectName(u"label_detalhes")
        self.label_detalhes.setGeometry(QRect(30, 15, 71, 21))
        self.label_detalhes.setStyleSheet(u"font: 700 12pt \"Berlin Sans FB Demi\";")

        self.gridLayout.addWidget(self.detalhes, 0, 1, 2, 1)
        
        self.ultimas_alteracoes = QFrame(self.Page_home)
        self.ultimas_alteracoes.setObjectName(u"ultimas_alteracoes")
        self.ultimas_alteracoes.setMaximumSize(QSize(16777215, 230))
        self.ultimas_alteracoes.setStyleSheet(u"\n" "background-color: rgb(240, 250, 255);")
        self.ultimas_alteracoes.setFrameShape(QFrame.StyledPanel)
        self.ultimas_alteracoes.setFrameShadow(QFrame.Raised)
        self.label_alteracoes = QLabel(self.ultimas_alteracoes)
        self.label_alteracoes.setObjectName(u"label_alteracoes")
        self.label_alteracoes.setGeometry(QRect(30, 15, 181, 21))
        self.label_alteracoes.setStyleSheet(u"font: 700 12pt \"Berlin Sans FB Demi\";")
    
        self.gridLayout.addWidget(self.ultimas_alteracoes, 1, 0, 1, 1)

        self.cadastrar_usuario.clicked.connect(self.teste)

        self.retranslateUi(application_pages)
        QMetaObject.connectSlotsByName(application_pages)


    def teste(self):
        print(self.Page_home.size())     
    
        
    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label_acesso_rapido.setText(QCoreApplication.translate("Form", u"Acesso r\u00e1pido", None))
        '''self.label_detalhes.setText(QCoreApplication.translate("Form", u"Detalhes", None))
        self.label_alteracoes.setText(QCoreApplication.translate("Form", u"\u00daltimas altera\u00e7\u00f5es", None))'''
    # retranslateUi


