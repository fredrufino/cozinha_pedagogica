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

class Ui_application_coz_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(769, 484)
        self.Page_fichas = QWidget()
        self.Page_fichas.setObjectName(u"Page_fichas")
        self.verticalLayout = QVBoxLayout(self.Page_fichas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.Page_fichas)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        application_pages.addWidget(self.Page_fichas)
        self.Page_orders = QWidget()
        self.Page_orders.setObjectName(u"Page_orders")
        self.verticalLayout_2 = QVBoxLayout(self.Page_orders)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.Page_orders)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        application_pages.addWidget(self.Page_orders)

        self.retranslateUi(application_pages)

        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("application_pages", u"Fichas Técnicas", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"Ordens de compra", None))
    # retranslateUi

