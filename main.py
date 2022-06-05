#IMPORT MODULES
import sys
import os

#IMPORT QT CORE
from qt_core import *

#IMPORT WINDOWS
#from gui.windows.login_window.ui_login_window import *
from gui.windows.main_window.ui_main_window import *

#IMPORT DATABASE FUNCTIONS
from database.db_crud import CrudDatabase

from gui.pages.adm_pages.ui_adm_pages import *


#CLASSE MAIN
class Main():
    def __init__(self):
        self.conexao = CrudDatabase.criando_conexao(self) #CRIANDO A CONEXÃO COM O BANCO DE DADOS
        self.schema =  CrudDatabase.create(self) #CRIANDO MINHAS TABELAS DO BANCO DE DADOS
        #self.insercoes = CrudDatabase.insercoes_iniciais(self) #REALIZANDO MINHAS INSERCOES INICIAIS NO BANCO DE DADOS
        self.vizualizar = CrudDatabase.vizualizar(self)

"""#LOGIN WINDOW
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        #SETUP MAIN WINDOW
        self.ui = UI_LoginWindow()
        self.ui.setup_ui(self)

        #EXIBIR A APLICAÇÃO
        self.show()"""

acesso = ('ADM', 1)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lá Papini - Cozinha Pedagógica")

        #SETUP MAIN WINDOW
        self.ui = UI_MainWindow(acesso)
        self.ui.setup_ui(self)
        UI_MainWindow.__init__(self, acesso) 
        
        #TOGGLE BUTTON
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        #ADM BUTTONS
        self.ui.home_adm .clicked.connect(self.show_page_adm_home)
        self.ui.orders_adm .clicked.connect(self.show_page_register_user)
        self.ui.users.clicked.connect(self.show_page_adm_users)

        #PÁGINA PRINCIPAL
        self.ui.ui_adm_pages.register_user_btn.clicked.connect(self.show_page_register_user)

            #PAGE USERS
        '''self.ui.ui_adm_pages.pushButton_1.clicked.connect(self.show_page_register_user)
        for item in range(4):
            self.ui.ui_adm_pages.pushButton[item].clicked.connect(self.show_page_user)
        '''
        #COZ BUTTONS
        self.ui.files.clicked.connect(self.show_page_coz_fichas)
        self.ui.orders_coz.clicked.connect(self.show_page_coz_orders)

        #COZ BUTTONS
        self.ui.stock.clicked.connect(self.show_page_est_vizualizar)
        self.ui.stock_closing.clicked.connect(self.show_page_est_fechamento)
        self.ui.food_registration.clicked.connect(self.show_page_est_cadastrar)
        self.ui.food_edit.clicked.connect(self.show_page_est_editar)
        self.ui.change_balance.clicked.connect(self.show_page_est_alterar)
        self.ui.food_exclude.clicked.connect(self.show_page_est_excluir)

        #SETTINGS BUTTON
        self.ui.settings_btn.clicked.connect(self.show_page_settings)

        #EXIBIR A APLICAÇÃO
        self.show()
        
    #SHOW ADM PAGES
    def show_page_adm_home(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_adm_pages.Page_home)
        
    def show_page_adm_orders(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_adm_pages.Page_orders)

    def show_page_adm_users(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_adm_pages.Page_users)
    
    def show_page_user(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_adm_pages.Page_user)
    
    def show_page_register_user(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_adm_pages.Page_registration)

    #SHOW COZ PAGES
    def show_page_coz_fichas(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_coz_pages.Page_fichas)

    def show_page_coz_orders(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_coz_pages.Page_orders)
        
    #SHOW EST PAGES
    def show_page_est_vizualizar(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_est_pages.Page_vizualizar)

    def show_page_est_fechamento(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_est_pages.Page_fechamento)

    def show_page_est_cadastrar(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_est_pages.Page_cadastrar)

    def show_page_est_editar(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_est_pages.Page_editar)
    
    def show_page_est_alterar(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_est_pages.Page_alterar)

    def show_page_est_excluir(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_est_pages.Page_excluir)

    #SHOW ALL USERS PAGES
    def show_page_settings(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_all_users_pages.Page_settings)    
        

    def toggle_button(self):
        #GET MENU WIDTH
        menu_width = self.ui.left_menu.width()
        
        #CHECK WIDTH
        width = 50
        if menu_width == 50:
            width = 240

        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(400)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

if __name__ == "__main__":
    conexão = Main() 
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())