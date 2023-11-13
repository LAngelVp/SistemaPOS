import sys
import Clases.img as img
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap, QMouseEvent
from RegistroPersonal import *
class Inicio(QMainWindow):
    def __init__(self):
        super(Inicio, self).__init__()
        self.ui = Ui_Registro_Personal()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.w_principal.setStyleSheet("border-radius: 12px;")
        self.ui.combobox_puesto.setStyleSheet("border-radius: 0px;")
        self.ui.img_empleado.setStyleSheet("border-radius: 0px;")
        # self.ui.panel_izquierda.setStyleSheet("background:#71c4ef; border-top-right-radius:0px; border-bottom-right-radius:0px;")
        self.ui.btn_cerrar.setIcon(QIcon(":/Source/img_cerrar.svg"))
        self.ui.btn_minimizar.setIcon(QIcon(":/Source/img_minimizar.svg"))
        # self.ui.img_fondo.setPixmap(QPixmap(":/Source/logo.svg"))
        # self.ui.img_login.setPixmap(QPixmap(":/Source/img_login.png"))
        self.ui.btn_cerrar.clicked.connect(self.cerrar)

    def cerrar(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Inicio()
    ui.show()
    sys.exit(app.exec_())