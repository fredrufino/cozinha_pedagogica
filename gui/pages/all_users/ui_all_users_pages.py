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

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(769, 484)
        self.Page_settings = QWidget()
        self.Page_settings.setObjectName(u"Page_settings")
        self.verticalLayout_3 = QVBoxLayout(self.Page_settings)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_settings = QLabel(self.Page_settings)
        self.label_settings.setObjectName(u"label_settings")
        self.label_settings.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_settings)

        application_pages.addWidget(self.Page_settings)

        self.retranslateUi(application_pages)

        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label_settings.setText(QCoreApplication.translate("application_pages", u"Configurações", None))
    # retranslateUi


