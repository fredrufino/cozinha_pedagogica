# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesErigwH.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

#IMPORT QT CORE
from qt_core import *

# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton

class Ui_application_est_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(769, 484)
        self.Page_vizualizar = QWidget()
        self.Page_vizualizar.setObjectName(u"Page_vizualizar")
        self.verticalLayout = QVBoxLayout(self.Page_vizualizar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.Page_vizualizar)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        application_pages.addWidget(self.Page_vizualizar)

        

        self.line = QFrame(self.Page_vizualizar)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(80, 200, 800, 500))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)


        #ADM BTNS
        self.card = PyPushButton(
        #text= "Ordens de compra",
        heigth= 100,
        icon_path= "icon_folder.svg",
        icon_color= "#FFFFFF"  
        #is_active= True     
        )
        self.card.setObjectName(u"card")
        self.card.setGeometry(QRect(10, 50, 91, 41))


        self.card_2 = PyPushButton(
        #text= "Ordens de compra",
        heigth= 100,
        icon_path= "icon_folder.svg",
        icon_color= "#FFFFFF"  
        #is_active= True     
        )
        self.card_3 = PyPushButton(
        #text= "Ordens de compra",
        heigth= 100,
        icon_path= "icon_folder.svg",
        icon_color= "#FFFFFF"  
        #is_active= True     
        )
        self.card_4 = PyPushButton(
        #text= "Ordens de compra",
        heigth= 100,
        icon_path= "icon_folder.svg",
        icon_color= "#FFFFFF"  
        #is_active= True     
        )
        self.card_5 = PyPushButton(
        #text= "Ordens de compra",
        heigth= 100,
        icon_path= "icon_folder.svg",
        icon_color= "#FFFFFF"  
        #is_active= True     
        )
        self.card_6 = PyPushButton(
        #text= "Ordens de compra",
        heigth= 100,
        icon_path= "icon_folder.svg",
        icon_color= "#FFFFFF"  
        #is_active= True     
        )

    
        #MENU SPACER
        self.spacer = QSpacerItem(10,10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        #self.verticalLayout.addWidget(self.card)
        #sself.verticalLayout.addItem(self.spacer)
        #self.verticalLayout.addWidget(self.card_2)
        """self.verticalLayout.addItem(self.spacer)
        self.verticalLayout.addWidget(self.card_3)
        self.verticalLayout.addItem(self.spacer)
        self.verticalLayout.addWidget(self.card_4)
        self.verticalLayout.addItem(self.spacer)
        self.verticalLayout.addWidget(self.card_5)
        self.verticalLayout.addItem(self.spacer)
        self.verticalLayout.addWidget(self.card_6)"""

        self.Page_fechamento = QWidget()
        self.Page_fechamento.setObjectName(u"Page_fechamento")
        self.verticalLayout_2 = QVBoxLayout(self.Page_fechamento)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.Page_fechamento)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        application_pages.addWidget(self.Page_fechamento)
        self.Page_cadastrar = QWidget()
        self.Page_cadastrar.setObjectName(u"Page_cadastrar")
        self.verticalLayout_3 = QVBoxLayout(self.Page_cadastrar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.Page_cadastrar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        application_pages.addWidget(self.Page_cadastrar)
        self.Page_editar = QWidget()
        self.Page_editar.setObjectName(u"Page_editar")
        self.verticalLayout_4 = QVBoxLayout(self.Page_editar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.Page_editar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        application_pages.addWidget(self.Page_editar)
        self.Page_alterar = QWidget()
        self.Page_alterar.setObjectName(u"Page_alterar")
        self.verticalLayout_5 = QVBoxLayout(self.Page_alterar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.Page_alterar)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        application_pages.addWidget(self.Page_alterar)
        self.Page_excluir = QWidget()
        self.Page_excluir.setObjectName(u"Page_excluir")
        self.verticalLayout_6 = QVBoxLayout(self.Page_excluir)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.Page_excluir)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        application_pages.addWidget(self.Page_excluir)

        self.retranslateUi(application_pages)

        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        #self.label.setText(QCoreApplication.translate("application_pages", u"Vizualizar estoque", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"Fechamento estoque", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"Cadastrar alimento", None))
        self.label_4.setText(QCoreApplication.translate("application_pages", u"Editar alimento", None))
        self.label_5.setText(QCoreApplication.translate("application_pages", u"Alterar saldo alimento", None))
        self.label_6.setText(QCoreApplication.translate("application_pages", u"Excluir alimento", None))
    # retranslateUi
