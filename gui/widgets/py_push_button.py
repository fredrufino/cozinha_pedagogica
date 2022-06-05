#IMPORTS
import os

#IMPORT QT CORE
from qt_core import *

class PyPushButton(QPushButton):
    def __init__(
        self,
        text = "",
        heigth = 40,
        minimum_width = 50,
        maximum_width = 50,
        text_padding = 55,
        text_color = "#6272A4" ,
        icon_path = "",
        icon_color = "#1D9EE8",
        btn_color = "#95D8FF",
        btn_hover = "#39B4FA",
        btn_pressed = "#39B4FA",
        btn_border = 0,
        is_btn_page = False,
        is_active = False
    ):      
        super().__init__()
        
        #SET DEFAULT PARAMETERS
        self.setText(text)
        self.setMaximumHeight(heigth)
        self.setMinimumHeight(heigth)
        self.setCursor(Qt.PointingHandCursor)
        
        # CUSTOM PARAMETERS
        self.minimum_width = minimum_width
        self.maximum_width= maximum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.btn_border = btn_border
        self.is_btn_page = is_btn_page
        self.is_active = is_active
        
        #SET STYLE
        self.set_style (
            text_padding = self.text_padding,
            text_color = self.text_color,
            maximum_width = self.maximum_width,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            btn_border = self.btn_border,
            is_btn_page= self.is_btn_page,
            is_active = self.is_active
            )
        
    def set_style(
        self,
        text_padding = 55,
        text_color = "#6272A4",
        maximum_width = 80,
        btn_color = "#95D8FF",
        btn_hover = "#39B4FA",
        btn_pressed = "#39B4FA",
        btn_border = 0,
        is_btn_page = False,
        is_active = False
    ):
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border-radius: {btn_border}px;
        }}
         QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """
        style_menu_pages = f"""
       QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: bottom;
            border-radius: {btn_border}px;
            font-family: "Impact";
        }}
         QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """

        active_style = f"""
        QPushButton {{
            background-color: {btn_hover};
            border-right: 5px solid "#FFFFFF";
        }}
        """
        if is_btn_page:
            self.setStyleSheet(style_menu_pages)
        elif not is_active:
            self.setStyleSheet(style)
        else: 
            self.setStyleSheet(style + active_style)
    
    def paintEvent(self, event):
        #RETURN DEFAULT STYLE
        QPushButton.paintEvent(self, event)
       
        #PAINTER
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        
        rect = QRect(0, 0, self.minimum_width, self.height())
        
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)
        
        qp.end()
    
    def draw_icon(self, qp, image, rect, color):
        #FORMAT PATH
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))
        
        #DRAW ICON
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()