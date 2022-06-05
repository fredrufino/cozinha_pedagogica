#IMPORT QT CORE
from email.mime import image
from unicodedata import name
from gui.pages.all_users.ui_all_users_pages import Ui_application_pages
from gui.pages.adm_pages.ui_adm_pages import Ui_application_adm_pages
from gui.pages.coz_pages.ui_coz_pages import Ui_application_coz_pages
from gui.pages.est_pages.ui_est_pages import Ui_application_est_pages
from qt_core import *

# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton

import functions.menu_functions

#MAIN WINDOW
class UI_MainWindow(object):
    def __init__(self, acesso):
        self.acesso = acesso
        self.menu_functions = functions.menu_functions.MenuFunctions(self.acesso)

    def setup_ui(self, parent,):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

            #SET INITIAL PARAMETERS
            parent.resize(1024, 560)
            parent.setMinimumSize(960,540)

            #CREATE CENTRAL WIDGET
            self.central_frame = QFrame()
            #self.central_frame.setStyleSheet("background-color: #282a36")   

            #CREAT MAIN LAYOUT
            self.main_layout = (QHBoxLayout(self.central_frame))
            self.main_layout.setContentsMargins(0,0,0,0)
            self.main_layout.setSpacing(0)

            #LEFT MENU 
            self.left_menu = QFrame()
            self.left_menu.setStyleSheet("background-color: #95D8FF")
            self.left_menu.setMaximumWidth(50)
            self.left_menu.setMinimumWidth(50)

            #LEFT MENU LAYOUT
            self.left_menu_layout = QVBoxLayout(self.left_menu)
            self.left_menu_layout.setContentsMargins(0,0,0,0)
            self.left_menu_layout.setSpacing(0)            
                
            #TOP FRAME MENU
            self.left_menu_top_frame = QFrame()
            self.left_menu_top_frame.setMinimumHeight(40)
            self.left_menu_top_frame.setObjectName("left_menu_top_frame")
                
            #TOP FRAME LAYOUT 
            self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
            self.left_menu_top_layout.setContentsMargins(0,0,0,0)
            self.left_menu_top_layout.setSpacing(0) 
                
            #TOP BTN - MENU
            self.toggle_button = PyPushButton(
                text= "Ocultar menu",
                icon_color= "#1D9EE8",
                icon_path= "icon_menu.svg"     
            )
            #ADM BTNS
            
            self.home_adm = PyPushButton(
                text= "Página principal",
                icon_path= "icon_home.svg",
                icon_color= "#1D9EE8"  
                #is_active= True     
            )
            self.orders_adm = PyPushButton(
                text= "Ordens de compra",
                icon_path= "icon_folder.svg",
                icon_color= "#1D9EE8"  
                #is_active= True     
            )
            self.users = PyPushButton(
                text= "Usuários",
                icon_path= "icon_users.svg",   
                icon_color= "#1D9EE8"  
            )

            #COZ BTNS
            self.files = PyPushButton(
                text= "Fichas Técnicas",
                icon_path= "icon_ficha.svg",
                icon_color= "#1D9EE8",
                #is_active= True     
            )
            self.orders_coz = PyPushButton(
                text= "Ordens de compra",
                icon_path= "icon_folder.svg",
                icon_color= "#1D9EE8" 
            )

            #EST BTNS
            self.stock = PyPushButton(
                text= "Vizualizar estoque",
                icon_path= "icon_stock.svg",
                icon_color= "#1D9EE8"     
            )
            self.stock_closing = PyPushButton(
                text= "Fechamento estoque",
                icon_path= "icon_stock.svg",
                icon_color= "#1D9EE8"   
            )
            self.food_registration = PyPushButton(
                text= "Cadastrar alimento",
                icon_path= "icon_menu.svg" ,
                icon_color= "#1D9EE8"       
            )
            self.food_edit = PyPushButton(
                text= "Editar alimento",
                icon_path= "icon_menu.svg",
                icon_color= "#1D9EE8"        
            )
            self.change_balance = PyPushButton(
                text= "Alterar saldo",
                icon_path= "icon_menu.svg",
                icon_color= "#1D9EE8"        
            )
            self.food_exclude = PyPushButton(
                text= "Excluir alimento",
                icon_path= "icon_menu.svg",
                icon_color= "#1D9EE8"        
            )
                
            #ADD BTNS TO LAYOUT 
            self.left_menu_top_layout.addWidget(self.toggle_button)
            if self.acesso[0] == 'ADM':
                self.left_menu_top_layout.addWidget(self.home_adm)
                self.left_menu_top_layout.addWidget(self.users)
                self.left_menu_top_layout.addWidget(self.orders_adm)
            elif self.acesso[0] == 'COZ':
                self.left_menu_top_layout.addWidget(self.files)
                self.left_menu_top_layout.addWidget(self.orders_coz)
            else:
                self.left_menu_top_layout.addWidget(self.stock)
                self.left_menu_top_layout.addWidget(self.stock_closing)
                self.left_menu_top_layout.addWidget(self.food_registration)
                self.left_menu_top_layout.addWidget(self.food_edit)
                self.left_menu_top_layout.addWidget(self.change_balance)
                self.left_menu_top_layout.addWidget(self.food_exclude)
            
            #MENU SPACER
            self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)

            #BOTTOM FRAME MENU
            self.left_menu_bottom_frame = QFrame()
            self.left_menu_bottom_frame.setMinimumHeight(40)
            self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
            self.left_menu_bottom_frame.setStyleSheet("left_menu_bottom_frame")
                
            #BOTTOM FRAME LAYOUT 
            self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
            self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
            self.left_menu_bottom_layout.setSpacing(0) 

            #BOTTOM BTNS
            self.settings_btn = PyPushButton(
                text= "Configurações",
                icon_path= "icon_settings.svg"     
            )
                
            #ADD BTNS TO LAYOUT 
            self.left_menu_bottom_layout.addWidget(self.settings_btn)
                
            #LABEL VERSION
            self.left_menu_label_version = QLabel("v1.0.0")
            self.left_menu_label_version.setAlignment(Qt.AlignCenter)
            self.left_menu_label_version.setMaximumHeight(30)
            self.left_menu_label_version.setMinimumHeight(30)
            self.left_menu_label_version.setStyleSheet("color: #6272A4")

            #ADD TO LAYOUT 
            self.left_menu_layout.addWidget(self.left_menu_top_frame)
            self.left_menu_layout.addItem(self.left_menu_spacer)
            self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
            self.left_menu_layout.addWidget(self.left_menu_label_version)
        
            #CONTENT 
            self.content = QFrame()
            self.content.setStyleSheet("background-color: #FFFFFF")

            #CONTENT LAYOUT
            self.content_layout = (QVBoxLayout(self.content))
            self.content_layout.setContentsMargins(0,0,0,0)
            self.content_layout.setSpacing(0)

            #TOP BAR
            self.top_bar = QFrame()
            self.top_bar.setMinimumHeight(40)
            self.top_bar.setMaximumHeight(40)
            self.top_bar.setStyleSheet("background-color: #C6EAFF; color: #6272A4")
            self.top_bar_layout = QHBoxLayout(self.top_bar)
            self.top_bar_layout.setContentsMargins(10,0,10,0)

            #LEFT LABEL
            self.top_label_left = QLabel("Cozinha pedagógica - Lá Papini")

            #TOP SPACER
            self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Maximum)

            #RIGHT LABEL NAME USER
            data_user_id = self.menu_functions.search("USUARIO", "")
            name = data_user_id[0][0] +" " + data_user_id[0][1]
            self.top_label_right = QLabel(f"{name.upper()}")
            self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

            
            image_url = '\'' + data_user_id[0][2] + '\''
            
            self.user_image_frame = QFrame()
            self.user_image_frame.setObjectName(u"user_image_frame")
            self.user_image_frame.setMaximumHeight(36)
            self.user_image_frame.setMinimumWidth(36) 
            self.user_image_frame.setStyleSheet(f"background-image: url({image_url});""border-radius: 18px;") 
            self.user_image_frame.setFrameShape(QFrame.StyledPanel)
            self.user_image_frame.setFrameShadow(QFrame.Raised)

            #ADD TO LAYOUT 
            self.top_bar_layout.addWidget(self.top_label_left)
            self.top_bar_layout.addItem(self.top_spacer)
            self.top_bar_layout.addWidget(self.top_label_right)
            self.top_bar_layout.addWidget(self.user_image_frame)

            #QWIDGET PAGES
            self.pages = QStackedWidget()
            self.pages.setStyleSheet("font-size: 12pt; color: #6272A4")

            #APPLICATION ADM PAGES
            self.ui_adm_pages = Ui_application_adm_pages()
            self.ui_adm_pages.setupUi(self.pages)

            #APPLICATION COZ PAGES
            self.ui_coz_pages = Ui_application_coz_pages()
            self.ui_coz_pages.setupUi(self.pages)

            #APPLICATION EST PAGES
            self.ui_est_pages = Ui_application_est_pages()
            self.ui_est_pages.setupUi(self.pages)
            
            #APPLICATION ALL USERS PAGES
            self.ui_all_users_pages = Ui_application_pages()
            self.ui_all_users_pages.setupUi(self.pages)


            #BOTTOM BAR
            self.bottom_bar = QFrame()
            self.bottom_bar.setMinimumHeight(30)
            self.bottom_bar.setMaximumHeight(30)
            self.bottom_bar.setStyleSheet("background-color: #C6EAFF; color: #6272A4")
            self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
            self.bottom_bar_layout.setContentsMargins(10,0,10,0)

            #LEFT LABEL
            self.bottom_label_left = QLabel("Criado por: Frederico Rufino")

            #BOTTOM SPACER
            self.bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Maximum)
                
            #RIGHT LABEL
            self.bottom_label_right = QLabel("ⓒ 2022")

            #ADD TO LAYOUT 
            self.bottom_bar_layout.addWidget(self.bottom_label_left)
            self.bottom_bar_layout.addItem(self.bottom_spacer)
            self.bottom_bar_layout.addWidget(self.bottom_label_right)

            #ADD TO CONTENT LAYOUT
            self.content_layout.addWidget(self.top_bar)
            self.content_layout.addWidget(self.pages)
            self.content_layout.addWidget(self.bottom_bar)

            #ADD WIDGETS TO APP
            self.main_layout.addWidget(self.left_menu)
            self.main_layout.addWidget(self.content)
        
            #SET CENTRAL WIDGET
            parent.setCentralWidget(self.central_frame)