#IMPORT QT CORE
from gui.pages.adm_pages.ui_pages import Ui_application_pages
from qt_core import *

# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton

#MAIN WINDOW
class UI_LoginWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("LoginWindow")

            #SET INITIAL PARAMETERS
            parent.resize(1024, 560)
            parent.setMinimumSize(960,540)
            parent.setStyleSheet("background-color: #95D8FF;")

            self.label = QLabel(parent)
            self.label.setObjectName("label")
            self.label.setGeometry(QRect(190, 30, 151, 141))
            self.label.setStyleSheet("background-color:None;")
            self.label.setPixmap(QPixmap("/gui/images/logo.png"))
            self.label.setScaledContents(True)
            
            self.retranslateUi(parent)
            
            #QMetaObject.connectSlotsByName(application_pages)

           
            
        